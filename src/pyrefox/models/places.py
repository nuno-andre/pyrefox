from typing import Optional, Union
from ..types import LooseModel, Model, AnyUrl, datetime
from .enums import BookmarkType, OriginSchemes, SpecialGuid, SyncStatus


class AnnotationAttribute(Model):
    id:   int
    name: str


class Annotation(LooseModel):
    id:            int
    content:       str
    flags:         int
    expiration:    int
    type:          int
    date_added:    datetime
    last_modified: datetime
    attribute:     AnnotationAttribute


class Origin(Model):
    id:       int
    prefix:   OriginSchemes
    host:     str
    frecency: int


class Place(LooseModel):
    id:                int
    url:               Union[AnyUrl, str]  # FIXME
    title:             Optional[str]
    rev_host:          str
    visit_count:       int
    hidden:            bool
    typed:             bool
    frecency:          int
    last_visit_date:   Optional[datetime]
    guid:              str
    foreign_count:     int
    url_hash:          int
    description:       Optional[str]
    preview_image_url: Optional[Union[AnyUrl, str]]  # FIXME
    origin:            Origin
    annotations:       list[Annotation]


class Bookmark(Model):
    '''
    Attrs:
        index: position in the parent folder.
    '''
    id:                  int
    type:                BookmarkType
    fk:                  Optional[int]
    parent:              int
    position:            int
    title:               Optional[str]
    keyword_id:          Optional[int]
    folder_type:         Optional[str]
    date_added:          datetime
    last_modified:       datetime
    guid:                Union[SpecialGuid, str]  # TODO: len == 12
    sync_status:         SyncStatus
    sync_change_counter: int
