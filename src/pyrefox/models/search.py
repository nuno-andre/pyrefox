from typing import Union, Optional, Any, Literal, List

from ..types import Model, AnyHttpUrl, datetime
from ..utils import _camel


class SearchEngineUrlParameter(Model):
    name:  str
    value: str


class SearchEngineUrl(Model):
    params:   List[SearchEngineUrlParameter]
    rels:     List[Any]  # TODO
    template: AnyHttpUrl
    type:     Optional[str]  # TODO: mime type


class SearchEngineMetadata(Model):
    alias:          Optional[str]
    order:          Optional[int]
    load_path_hash: Optional[str]  # TODO: base64?


class SearchEngine(Model):
    '''App provided search engine.
    '''
    name:            str
    is_app_provided: Literal[True]
    meta_data:       SearchEngineMetadata

    class Config:
        alias_generator = _camel


# TODO
class OpenSearchEngine(SearchEngine):
    is_app_provided: Literal[False]
    description:     Optional[str]
    urls:            Optional[List[SearchEngineUrl]]
    defined_aliases: Optional[List[Any]]
    order_hint:      Optional[Any]
    file_path:       Optional[Any]
    load_path:       Optional[Any]
    icon_url:        Optional[Any]
    locale:          Optional[Any]
    telemetry_id:    Optional[Any]
    # non-OpenSearch elements
    search_form:     Optional[AnyHttpUrl]
    update_url:      Optional[Any]
    update_interval: Optional[Any]
    icon_update_url: Optional[Any]
    extension_id:    Optional[Any]

    class Config:
        fields = {'search_form': '__searchForm', 'extension_id': '_extensionID'}


class SearchEnginesMetadata(Model):
    search_default:               str  # TODO: it must be a SearchEngine name
    search_default_hash:          str  # base64
    visible_default_engines:      str  # comma-list of SearchEngine names
    visible_default_engines_hash: str  # base64
    search_default_expir:         datetime
    use_saved_order:              bool


class SearchEngines(Model):
    version:   int
    engines:   list[Union[SearchEngine, OpenSearchEngine]]
    meta_data: SearchEnginesMetadata
