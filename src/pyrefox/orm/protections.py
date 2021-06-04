from ._sql import Column, declarative_base
from ._types import Date, Integer

ProtectionsBase = declarative_base()


class EventOrm(ProtectionsBase):
    __tablename__ = 'events'

    id        = Column(Integer, primary_key=True)
    type      = Column(Integer, nullable=False)
    count     = Column(Integer, nullable=False)
    timestamp = Column(Date)
