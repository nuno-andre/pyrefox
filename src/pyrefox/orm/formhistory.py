from ._sql import Column, ForeignKey, relationship, declarative_base
from ._types import Integer, String, Text, UnixTimeMicro

FormHistoryBase = declarative_base()


class DeletedFormHistoryOrm(FormHistoryBase):
    __tablename__ = 'moz_deleted_formhistory'

    id          = Column(Integer, primary_key=True)
    timeDeleted = Column(Integer)
    guid        = Column(Text)


class FormHistoryOrm(FormHistoryBase):
    __tablename__ = 'moz_formhistory'

    id        = Column(Integer, primary_key=True)
    fieldname = Column(Text, nullable=False, index=True)
    value     = Column(Text, nullable=False)
    timesUsed = Column(Integer)
    firstUsed = Column(UnixTimeMicro)
    lastUsed  = Column(UnixTimeMicro, index=True)
    guid      = Column(String(16), index=True)

    sources = relationship('SourceOrm', secondary='moz_history_to_sources')


class SourceOrm(FormHistoryBase):
    __tablename__ = 'moz_sources'

    id     = Column(Integer, primary_key=True)
    source = Column(Text, nullable=False)


class HistoryToSourcesOrm(FormHistoryBase):
    __tablename__ = 'moz_history_to_sources'

    history_id = Column(ForeignKey('moz_formhistory.id', ondelete='cascade'),
                        primary_key=True,
                        nullable=False)
    source_id  = Column(ForeignKey('moz_sources.id', ondelete='cascade'),
                        primary_key=True,
                        nullable=False)
