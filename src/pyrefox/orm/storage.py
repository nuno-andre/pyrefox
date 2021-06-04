from sqlalchemy import Table
from ._sql import (
    Column, ForeignKey, text, relationship, declarative_base,
)
from ._types import Integer, String, Text

StorageBase = declarative_base()
metadata = StorageBase.metadata


t_cache = Table(
    'cache', metadata,
    Column('valid', Integer, nullable=False, server_default=text('0')),
    # format: YYYYMMDDHHMMSS
    Column('build_id', String(14), nullable=False, server_default=text("''"))
)


t_database = Table(
    'database', metadata,
    Column('cache_version', Integer, nullable=False, server_default=text('0'))
)


class RepositoryOrm(StorageBase):
    __tablename__ = 'repository'

    id   = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class OriginOrm(StorageBase):
    __tablename__ = 'origin'

    repository_id    = Column(ForeignKey('repository.id'), primary_key=True, nullable=False)
    origin           = Column(Text, primary_key=True, nullable=False)
    group_           = Column(Text, nullable=False)
    client_usages    = Column(Text, nullable=False)
    usage            = Column(Integer, nullable=False)
    last_access_time = Column(Integer, nullable=False)
    accessed         = Column(Integer, nullable=False)
    persisted        = Column(Integer, nullable=False)
    suffix           = Column(Text)

    repository = relationship('RepositoryOrm')
