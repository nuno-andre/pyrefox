from pathlib import Path
from os import PathLike

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .content_prefs import ContentPrefsBase
from .cookies import CookiesBase, CookieOrm
from .favicons import FaviconsBase
from .formhistory import FormHistoryBase, FormHistoryOrm, HistoryToSourcesOrm
from .permissions import PermissionsBase, PermissionOrm
from .places import PlacesBase, BookmarkOrm, AnnotationOrm, PlaceOrm
from .protections import ProtectionsBase, EventOrm
from .storage import StorageBase
from .storage_sync import StorageSyncBase, CollectionDatumOrm
from .storage_sync_v2 import StorageSync2Base, DatumOrm
from .webappsstore import WebAppsStoreBase, WebAppsStoreOrm


class Orm:
    connect_args = {'check_same_thread': False}

    def __init__(self, path: PathLike):
        dbpath = Path(path).joinpath(f'{self.database}.sqlite')
        self.path = dbpath.as_uri().replace('file:', 'sqlite:')
        self.engine = create_engine(self.path, connect_args=self.connect_args)
        self.session = Session(self.engine)


class ContentPrefs(Orm):
    database = 'content-prefs'
    base = ContentPrefsBase


class Cookies(Orm):
    database = 'cookies'
    base = CookiesBase

    @property
    def cookies(self):
        return self.session.query(CookieOrm)


class Favicons(Orm):
    database = 'favicons'
    base = FaviconsBase


class FormHistory(Orm):
    database = 'formhistory'
    base = FormHistoryBase

    @property
    def form_history(self):
        return self.session.query(FormHistoryOrm)

    @property
    def history_to_sources(self):
        return self.session.query(HistoryToSourcesOrm)


class Permissions(Orm):
    database = 'permissions'
    base = PermissionsBase

    @property
    def permissions(self):
        return self.session.query(PermissionOrm)


class Places(Orm):
    database = 'places'
    base = PlacesBase

    @property
    def annotations(self):
        return self.session.query(AnnotationOrm)

    @property
    def bookmarks(self):
        return self.session.query(BookmarkOrm)

    @property
    def places(self):
        return self.session.query(PlaceOrm)


class Protections(Orm):
    database = 'protections'
    base = ProtectionsBase

    @property
    def events(self):
        return self.session.query(EventOrm)


class Storage(Orm):
    database = 'storage'
    base = StorageBase


class StorageSync(Orm):
    database = 'storage-sync'
    base = StorageSyncBase

    @property
    def collection_data(self):
        return self.session.query(CollectionDatumOrm)


class StorageSync2(Orm):
    database = 'storage-sync-v2'
    base = StorageSync2Base

    @property
    def data(self):
        return self.session.query(DatumOrm)


class WebAppsStore(Orm):
    database = 'webappsstore'
    base = WebAppsStoreBase

    @property
    def web_apps_store(self):
        return self.session.query(WebAppsStoreOrm)
