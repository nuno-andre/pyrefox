from ._sql import Column, UniqueConstraint, text, declarative_base
from ._types import Boolean, Integer, Text, UnixTimeMicro

CookiesBase = declarative_base()


class CookieOrm(CookiesBase):
    __tablename__ = 'moz_cookies'
    __table_args__ = UniqueConstraint('name', 'host', 'path', 'originAttributes'),

    id               = Column(Integer, primary_key=True)
    originAttributes = Column(Text, nullable=False, server_default=text("''"))
    name             = Column(Text)
    value            = Column(Text)
    host             = Column(Text)
    path             = Column(Text)
    expiry           = Column(Integer)  # TODO: invalid values as unix time (sec)
    lastAccessed     = Column(UnixTimeMicro)
    creationTime     = Column(UnixTimeMicro)
    isSecure         = Column(Boolean)
    isHttpOnly       = Column(Boolean)
    inBrowserElement = Column(Boolean, server_default=text('0'))
    sameSite         = Column(Integer, server_default=text('0'))
    rawSameSite      = Column(Integer, server_default=text('0'))
    schemeMap        = Column(Integer, server_default=text('0'))
