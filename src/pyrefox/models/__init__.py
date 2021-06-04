from typing import Union

from ..types import (
    DynamicModel, Model, Object,
    AboutUri, FileUri, HttpUrl, ResourceUri, MozExtensionUri, ViewSourceAnyUrl,
    datetime, date,
)
from ..utils import _camel
from .enums import EventType, PermissionType, SameSite
from .extensions import AddOnsStartUp, Extensions
from .places import Bookmark, Place


class SearchEngine(DynamicModel):
    name:            str
    is_app_provided: bool
    meta_data:       Object

    class Config:
        alias_generator = _camel


class SearchEngines(Model):
    version:   int
    engines:   list[SearchEngine]
    meta_data: Object  # TODO


class Event(Model):
    id:        int
    type:      EventType
    count:     int
    timestamp: date


class Permission(Model):
    id:                int
    origin:            Union[HttpUrl, AboutUri, FileUri, ResourceUri, MozExtensionUri, ViewSourceAnyUrl]
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


__all__ = [
    'AddOnsStartUp',
    'Bookmark',
    'Event',
    'Extensions',
    'Place',
]
