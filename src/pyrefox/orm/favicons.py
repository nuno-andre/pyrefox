from ._sql import (
    Column, ForeignKey, PrimaryKeyConstraint,
    declarative_base, relationship, text,
)
from ._types import Integer, LargeBinary, NullType, Text, UnixTimeMili

FaviconsBase = declarative_base()


class IconOrm(FaviconsBase):
    __tablename__ = 'moz_icons'

    id                  = Column(Integer, primary_key=True)
    icon_url            = Column(Text, nullable=False)
    fixed_icon_url_hash = Column(Integer, nullable=False, index=True)
    width               = Column(Integer, nullable=False, server_default=text('0'))
    root                = Column(Integer, nullable=False, server_default=text('0'))
    color               = Column(Integer)
    expire_ms           = Column(UnixTimeMili, nullable=False, server_default=text('0'))
    data                = Column(LargeBinary)


class PageWithIconOrm(FaviconsBase):
    __tablename__ = 'moz_pages_w_icons'

    id            = Column(Integer, primary_key=True)
    page_url      = Column(Text, nullable=False)
    page_url_hash = Column(Integer, nullable=False, index=True)


class IconToPage(FaviconsBase):
    __tablename__ = 'moz_icons_to_pages'

    page_id   = Column(ForeignKey('moz_pages_w_icons.id'), primary_key=True, nullable=False)
    icon_id   = Column(ForeignKey('moz_icons.id'), primary_key=True, nullable=False)
    expire_ms = Column(Integer, nullable=False, server_default=text('0'))

    icon = relationship('IconOrm')
    page = relationship('PageWithIconOrm')


class Stat(FaviconsBase):
    __tablename__ = 'sqlite_stat1'
    __table_args__ = PrimaryKeyConstraint('tbl', 'idx', 'stat'),

    tbl  = Column(NullType)
    idx  = Column(NullType)
    stat = Column(NullType)
