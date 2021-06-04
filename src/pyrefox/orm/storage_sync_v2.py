from ._sql import CheckConstraint, Column, text, declarative_base
from ._types import Integer, JSON, NullType, Text

StorageSync2Base = declarative_base()


class MetaOrm(StorageSync2Base):
    __tablename__ = 'meta'

    key   = Column(Text, primary_key=True)
    value = Column(NullType, nullable=False)


class DatumOrm(StorageSync2Base):
    __tablename__ = 'storage_sync_data'

    ext_id              = Column(Text, primary_key=True)
    data                = Column(JSON)
    sync_change_counter = Column(Integer, nullable=False, server_default=text('1'))


class MirrorOrm(StorageSync2Base):
    __tablename__ = 'storage_sync_mirror'
    __table_args__ = CheckConstraint('(ext_id is null and data is null) or '
                                     '(ext_id is not null and data is not null)'),

    guid   = Column(Text, primary_key=True)
    ext_id = Column(Text)
    data   = Column(Text)
