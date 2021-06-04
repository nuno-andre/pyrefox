from ._sql import Column, declarative_base
from ._types import Boolean, Integer, Text, UnixTimeMicro

PermissionsBase = declarative_base()


class HostOrm(PermissionsBase):
    __tablename__ = 'moz_hosts'

    id                 = Column(Integer, primary_key=True)
    host               = Column(Text)
    type               = Column(Text)
    permission         = Column(Integer)
    expireType         = Column(Integer)
    expireTime         = Column(UnixTimeMicro)
    modificationTime   = Column(UnixTimeMicro)
    isInBrowserElement = Column(Integer)


class PermissionOrm(PermissionsBase):
    __tablename__ = 'moz_perms'

    id               = Column(Integer, primary_key=True)
    origin           = Column(Text)
    type             = Column(Text)
    permission       = Column(Boolean)
    expireType       = Column(Integer)
    expireTime       = Column(UnixTimeMicro)
    modificationTime = Column(UnixTimeMicro)
