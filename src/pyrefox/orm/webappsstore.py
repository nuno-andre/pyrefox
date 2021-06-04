# from sqlalchemy import Table
from ._sql import Column, Index, PrimaryKeyConstraint, declarative_base
from ._types import Text

WebAppsStoreBase = declarative_base()


class WebAppsStoreOrm(WebAppsStoreBase):
    __tablename__ = 'webappsstore2'
    __table_args__ = (
        Index('origin_key_index', 'originAttributes', 'originKey', 'key', unique=True,),
        # XXX: pk not in the original table
        PrimaryKeyConstraint('originAttributes', 'originKey', 'key'),
    )

    originAttributes = Column(Text)
    originKey        = Column(Text)
    scope            = Column(Text)
    key              = Column(Text)
    value            = Column(Text)
