from ..types import StrEnum, IntEnum


class BookmarkType(IntEnum):
    BOOKMARK  = 1
    FOLDER    = 2
    SEPARATOR = 3


class SyncStatus(IntEnum):
    UNKNOWN = 0
    NEW     = 1
    NORMAL  = 2


class SpecialGuid(StrEnum):
    ROOT    = 'root________'
    MENU    = 'menu________'
    TAGS    = 'tags________'
    MOBILE  = 'mobile______'
    TOOLBAR = 'toolbar_____'
    UNFILED = 'unfiled_____'


class OriginSchemes(StrEnum):
    ABOUT      = 'about:'
    FILE       = 'file://'
    FTP        = 'ftp://'
    HTTP       = 'http://'
    HTTPS      = 'https://'
    JAVASCRIPT = 'javascript:'
    PLACE      = 'place:'
    RESOURCE   = 'resource://'


class StorageRepository(IntEnum):
    PERSISTENT = 0
    TEMPORARY  = 1
    DEFAULT    = 2


class AuthType(IntEnum):
    HTML   = 0
    BASIC  = 1
    DIGEST = 2


class SameSite(IntEnum):
    NONE   = 0
    LAX    = 1
    STRICT = 2


class EventType(IntEnum):
    OTHER_COOKIES_BLOCKED_ID = 0
    TRACKERS_ID              = 1
    TRACKING_COOKIES_ID      = 2
    CRYPTOMINERS_ID          = 3
    FINGERPRINTERS_ID        = 4
    SOCIAL_ID                = 5


class PermissionType(StrEnum):
    INDEXED_DB                      = 'indexedDB'
    PERSISTENT_STORAGE              = 'persistent-storage'
    POPUP                           = 'popup'
    STORAGE_ACCESS_API              = 'storageAccessAPI'
    WEBEXTENSIONS_UNLIMITED_STORAGE = 'WebExtensions-unlimitedStorage'


class AddOnTypes(StrEnum):
    EXTENSION = 'extension'
    THEME     = 'theme'


class ApiPermissions(StrEnum):
    '''
    https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions
    '''
    ACTIVE_TAB            = 'activeTab'
    ALARMS                = 'alarms'
    BACKGROUND            = 'background'
    BOOKMARKS             = 'bookmarks'
    BROWSER_SETTINGS      = 'browserSettings'
    BROWSING_DATA         = 'browsingData'
    CAPTIVE_PORTAL        = 'captivePortal'
    CLIPBOARD_READ        = 'clipboardRead'
    CLIPBOARD_WRITE       = 'clipboardWrite'
    CONTENT_SETTINGS      = 'contentSettings'
    CONTEXT_MENUS         = 'contextMenus'
    CONTEXTUAL_IDENTITIES = 'contextualIdentities'
    COOKIES               = 'cookies'
    DEBUGGER              = 'debugger'
    DEVTOOLS              = 'devtools'
    DNS                   = 'dns'
    DOWNLOADS             = 'downloads'
    DOWNLOADS_OPEN        = 'downloads.open'
    FIND                  = 'find'
    GEOLOCATION           = 'geolocation'
    HISTORY               = 'history'
    IDENTITY              = 'identity'
    IDLE                  = 'idle'
    MANAGEMENT            = 'management'
    NATIVE_MESSAGING      = 'nativeMessaging'
    NOTIFICATIONS         = 'notifications'
    PAGE_CAPTURE          = 'pageCapture'
    PKCS11                = 'pkcs11'
    PRIVACY               = 'privacy'
    PROXY                 = 'proxy'
    SEARCH                = 'search'
    SESSIONS              = 'sessions'
    STORAGE               = 'storage'
    TAB_HIDE              = 'tabHide'
    TABS                  = 'tabs'
    THEME                 = 'theme'
    TOP_SITES             = 'topSites'
    UNLIMITED_STORAGE     = 'unlimitedStorage'
    WEB_NAVIGATION        = 'webNavigation'
    WEB_REQUEST           = 'webRequest'
    WEB_REQUEST_BLOCKING  = 'webRequestBlocking'


class RecommendationStates(StrEnum):
    LINE                = 'line'
    RECOMMENDED         = 'recommended'
    RECOMMENDED_ANDROID = 'recommended-android'


class InstallTelemetrySources(StrEnum):
    AMO     = 'amo'  # addons.mozilla.org
    DISCO   = 'disco'
    UNKNOWN = 'unknown'


class InstallTelemetryMethods(StrEnum):
    AM_WEB_API      = 'amWebAPI'
    INSTALL_TRIGGER = 'installTrigger'
    LINK            = 'link'
