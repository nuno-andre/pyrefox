from typing import Optional, Union, Any, Literal
from ..types import (
    Model, Object, validator, datetime,
    HttpUrl, ResourceUri, AnyUrl, Path,
)
from .enums import (
    AddOnTypes,
    ApiPermissions,
    InstallTelemetryMethods,
    InstallTelemetrySources,
    RecommendationStates,
)


# region `extensions.json`
# TODO: data types
class DefaultLocale(Model):
    name:         str
    description:  Optional[str]
    creator:      Optional[str]
    homepage_url: Optional[HttpUrl]
    developers:   Optional[Any]
    translators:  Optional[Any]
    contributors: Optional[Any]


class Locale(DefaultLocale):
    locales: list[str]


class TargetApplication(Model):
    id:          str
    min_version: Optional[str]
    max_version: Optional[str]


class Permissions(Model):
    permissions: list[ApiPermissions]
    origins:     list[str]  # TODO


# TODO:
# dict: {incognito: Opt, tabId: Opt, types: Opt[list[str]], urls: list[str], windowId: Opt}
# list[str] -> enum {blocking, requestHeaders}
class PersistentListener(Model):
    web_request: dict[str, list[list[Union[Object, list[str]]]]]


class StartupData(Model):
    persistent_listeners: Optional[PersistentListener]

    @validator('persistent_listeners', pre=True)
    def validate_persistent_listeners(cls, v: Optional[dict]) -> Optional[dict]:
        return v or None


class InstallTelemetryInfo(Model):
    source:     InstallTelemetrySources
    source_url: Optional[str]
    method:     Optional[InstallTelemetryMethods]


class RecommendationState(Model):
    valid_not_after:  datetime
    valid_not_before: datetime
    states:           list[RecommendationStates]


# TODO: data types
class AnyAddOn(Model):
    id:                       str
    sync_guid:                str
    version:                  str
    type:                     AddOnTypes
    loader:                   Optional[str]
    update_url:               Optional[str]
    options_url:              Optional[str]
    options_type:             Optional[int]
    options_browser_style:    bool
    about_url:                Optional[str]
    default_locale:           Optional[DefaultLocale]
    visible:                  bool
    active:                   bool
    user_disabled:            bool
    app_disabled:             bool
    embedder_disabled:        bool
    install_date:             datetime
    update_date:              Optional[datetime]
    apply_background_updates: int
    path:                     Optional[Path]
    skinnable:                bool
    source_uri:               Optional[HttpUrl]
    release_notes_uri:        Optional[HttpUrl]
    soft_disabled:            bool
    foreign_install:          bool
    strict_compatibility:     bool
    locales:                  list[Locale]
    target_applications:      list[TargetApplication]
    target_platforms:         list[Any]  # TODO
    signed_state:             Optional[int]
    signed_date:              Optional[datetime]
    seen:                     bool
    dependencies:             list[Any]  # TODO
    incognito:                Optional[str]
    user_permissions:         Optional[Permissions]
    optional_permissions:     Optional[Permissions]
    icons:                    dict[int, Path]
    icon_url:                 Optional[str]
    blocklist_state:          int
    blocklist_url:            Optional[str]
    startup_data:             Optional[StartupData]
    hidden:                   bool
    install_telemetry_info:   Optional[InstallTelemetryInfo]
    recommendation_state:     Optional[RecommendationState]

    @validator('startup_data', pre=True)
    def validate_startup_data(cls, v: Optional[dict]) -> Optional[dict]:
        return v or None

    def dict(self, **kwargs):
        dct = super().dict(**kwargs)
        if 'icons' in dct:
            dct['icons'] = {str(k): str(v) for k, v in dct['icons'].items()}
        return dct


class AppBuiltin(AnyAddOn):
    root_uri: ResourceUri
    location: Literal['app-builtin']


class AppProfile(AnyAddOn):
    root_uri: str  # TODO: pydantic AnyUrl fails to identify jar scheme
    location: Literal['app-profile']


class AppSystemDefaults(AnyAddOn):
    root_uri: str  # TODO
    location: Literal['app-system-defaults']


AddOn = Union[AppBuiltin, AppProfile, AppSystemDefaults]


class Extensions(Model):
    schema_version: int
    addons:         list[AddOn]
# endregion


# region `addonStartup.json.lz4`
# TODO: compare with AnyAddOn
class AddOnStartUp(Model):
    type:               Optional[str]
    dependencies:       list[Any]
    enabled:            bool
    last_modified_time: Optional[datetime]
    loader:             Optional[Any]
    path:               Optional[str]
    root_uri:           str
    run_in_safe_mode:   bool
    signed_state:       Optional[int]
    signed_date:        Optional[datetime]
    telemetry_key:      str
    version:            str
    startup_data:       Optional[dict]


class AnyAddOnStartUp(Model):
    addons: dict[str, AddOnStartUp]
    staged: dict


class AppProfileStartUp(AnyAddOnStartUp):
    path: Path


class AppSystemDefaultsStartUp(AnyAddOnStartUp):
    path: Path


class AppBuiltinStartUp(AnyAddOnStartUp):
    ...


class AddOnsStartUp(Model):
    app_profile:         AppProfileStartUp
    app_system_defaults: AppSystemDefaultsStartUp
    app_builtin:         AppBuiltinStartUp

    class Config:
        alias_generator = lambda x: x.replace('_', '-')  # noqa: E731
# endregion
