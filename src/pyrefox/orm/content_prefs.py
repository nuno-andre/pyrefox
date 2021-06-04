from ._sql import (Column, ForeignKey, Index,
                   declarative_base, relationship, text)
from ._types import Integer, LargeBinary, Text, UnixTime

ContentPrefsBase = declarative_base()


class GroupOrm(ContentPrefsBase):
    __tablename__ = 'groups'

    id   = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, index=True)


class SettingOrm(ContentPrefsBase):
    __tablename__ = 'settings'

    id   = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, index=True)


class PrefOrm(ContentPrefsBase):
    __tablename__ = 'prefs'
    __table_args__ = (
        Index('prefs_idx', 'timestamp', 'groupID', 'settingID'),
    )

    id        = Column(Integer, primary_key=True)
    groupID   = Column(ForeignKey('groups.id'))
    settingID = Column(ForeignKey('settings.id'), nullable=False)
    value     = Column(LargeBinary)
    timestamp = Column(UnixTime, nullable=False, server_default=text('0'))  # TODO

    group   = relationship('GroupOrm')
    setting = relationship('SettingOrm')
