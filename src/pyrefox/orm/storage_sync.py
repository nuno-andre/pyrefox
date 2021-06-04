from ._sql import Column, Index, PrimaryKeyConstraint, declarative_base
from ._types import Integer, JSON, Text

StorageSyncBase = declarative_base()


class CollectionDatumOrm(StorageSyncBase):
    __tablename__ = 'collection_data'
    __table_args__ = (
        Index('unique_collection_record', 'collection_name', 'record_id', unique=True),
        # XXX: pk not in the original table
        PrimaryKeyConstraint('collection_name', 'record_id'),
    )

    collection_name = Column(Text)
    record_id       = Column(Text)
    record          = Column(JSON)  # Column(Text)


class CollectionMetadatumOrm(StorageSyncBase):
    __tablename__ = 'collection_metadata'

    collection_name = Column(Text, primary_key=True)
    last_modified   = Column(Integer)
    metadata_       = Column('metadata', Text)
