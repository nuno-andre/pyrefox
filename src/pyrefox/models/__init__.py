from typing import Union
from http.cookies import SimpleCookie

from ..types import (
    Model, AboutUri, FileUri, HttpUrl,
    ResourceUri, MozExtensionUri, ViewSourceAnyUrl,
    datetime, date,
)
from .enums import EventType, PermissionType, SameSite
from .extensions import AddOnsStartUp, Extensions
from .places import Bookmark, Place
from .search import SearchEngines


class Event(Model):
    id:        int
    type:      EventType
    count:     int
    timestamp: date


class Permission(Model):
    id:                int
    origin:            Union[HttpUrl, AboutUri, FileUri, ResourceUri, MozExtensionUri, ViewSourceAnyUrl]  # noqa: E501
    type:              PermissionType
    permission:        bool
    expire_type:       int
    expire_time:       datetime
    modification_time: datetime


class Cookie(Model):
    id:                 int
    origin_attributes:  str
    name:               str
    value:              str
    host:               str
    path:               str
    expiry:             datetime
    last_accessed:      datetime
    creation_time:      datetime
    is_secure:          bool
    is_http_only:       bool
    in_browser_element: bool
    same_site:          SameSite
    raw_same_site:      SameSite
    scheme_map:         int

    @property
    def header(self) -> SimpleCookie:
        cookie = SimpleCookie()
        cookie[self.name] = self.value
        cookie[self.name]['expires'] = self.expiry
        cookie[self.name]['path'] = self.path
        cookie[self.name]['domain'] = self.host
        cookie[self.name]['secure'] = self.is_secure
        cookie[self.name]['httponly'] = self.is_http_only
        cookie[self.name]['samesite'] = self.same_site.name.capitalize()
        return cookie


__all__ = [
    'AddOnsStartUp',
    'Bookmark',
    'Event',
    'Extensions',
    'Place',
    'SearchEngines',
]
