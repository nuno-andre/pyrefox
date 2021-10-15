from typing import Iterator
from contextvars import Context, ContextVar
from os import PathLike, getenv
from platform import system
from pathlib import Path
import json

from .orm import (
    Cookies,
    FormHistory,
    Permissions,
    Places,
    Protections,
    StorageSync,
    StorageSync2,
    WebAppsStore,
)
from .utils import read_json, read_mozlz4
from .models import (
    AddOnsStartUp,
    Bookmark,
    Cookie,
    Event,
    Extensions,
    Permission,
    Place,
    SearchEngines,
)
from .types import datetime


# user_prefs helpers
false = False
true = True


def user_pref(key, value):
    var = ContextVar(key)
    var.set(value)


class Profile:

    def __init__(self, path: PathLike) -> None:
        self.path = Path(path)
        self.ctx = Context()
        self.places_db = Places(self.path)
        self.cookies_db = Cookies(self.path)
        self.form_history = FormHistory(self.path)
        self.web_apps_store = WebAppsStore(self.path)
        self.permissions_db = Permissions(self.path)
        self.protections = Protections(self.path)
        self.storage_sync = StorageSync(self.path)
        self.storage_sync_v2 = StorageSync2(self.path)

    def __repr__(self) -> str:
        return f'FirefoxProfile<{self.path.name}>'

    @property
    def is_dev_edition(self) -> bool:
        return 'dev-edition' in self.path.suffix

    @property
    def modified(self) -> datetime:
        return datetime.fromtimestamp(self.path.stat().st_mtime)

    @property
    def search_engines(self):
        return SearchEngines(**read_mozlz4(self.path / 'search.json.mozlz4'))

    @property
    def extensions(self) -> Extensions:
        return Extensions(**read_json(self.path / 'extensions.json'))

    @property
    def addon_startup(self):
        return AddOnsStartUp(**read_mozlz4(self.path / 'addonStartup.json.lz4'))

    @property
    def bookmarks(self) -> Iterator[Bookmark]:
        for bookmark in self.places_db.bookmarks:
            yield Bookmark.from_orm(bookmark)

    @property
    def cookies(self) -> Iterator[Cookie]:
        for cookie in self.cookies_db.cookies:
            yield Cookie.from_orm(cookie)

    @property
    def events(self) -> Iterator[Event]:
        for event in self.protections.events:
            yield Event.from_orm(event)

    @property
    def permissions(self) -> Iterator[Permission]:
        for perm in self.permissions_db.permissions:
            yield Permission.from_orm(perm)

    @property
    def places(self) -> Iterator[Place]:
        for place in self.places_db.places:
            yield Place.from_orm(place)

    @property
    def user_prefs(self):
        with open(self.path / 'prefs.js') as p:
            for line in p:
                line = line.strip()
                if line and line[0:2] != '//':
                    self.ctx.run(lambda: eval(line.rstrip(';')))
        # return {k.name: v for k, v in self.ctx.items()}
        return dict(sorted((k.name, v) for k, v in self.ctx.items()))

    @property
    def xulstore(self):
        with open(self.path / 'xulstore.json') as f:
            return json.loads(f.read())


class Pyrefox:
    __slots__ = '_profiles',

    is_win: bool = system() == 'Windows'

    def __init__(self) -> None:
        self._profiles = None

    @property
    def basedirs(self) -> Iterator[PathLike]:
        if self.is_win:
            return map(Path(getenv('APPDATA')).joinpath,
                       ('Mozilla/Firefox', 'LibreWolf'))
        else:
            return map(Path.home().joinpath,
                       ('.mozilla/firefox', '.librewolf'))

    @property
    def profiles(self) -> list[Profile]:
        if self._profiles is None:
            if self.is_win:
                pdirs = (d / 'Profiles' for d in self.basedirs)
            else:
                pdirs = self.basedirs

            self._profiles = sorted(
                (Profile(d) for p in pdirs
                    for d in p.glob('*default*') if d.is_dir()),
                key=lambda x: x.modified,
                reverse=True,
            )
        return self._profiles
