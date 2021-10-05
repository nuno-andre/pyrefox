from datetime import datetime, date
from enum import Enum, IntEnum
from pathlib import Path
from typing import Any
import re

from pydantic import BaseModel, validator
from pydantic import AnyUrl, AnyHttpUrl, HttpUrl, ConstrainedStr

from .utils import camel

Object = dict[str, Any]


class StrEnum(str, Enum):
    pass


# TODO: uris that subclass ConstrainedStr fail with AnyUrl

class AboutUri(ConstrainedStr):
    regex = re.compile('^about:[A-Za-z]*$')


class ViewSourceAnyUrl(ConstrainedStr):
    regex = re.compile(r'^view-source:\S*$')


class JarAnyUrl(ConstrainedStr):
    regex = re.compile(r'^jar:\S*$')


class FileUri(ConstrainedStr):
    regex = re.compile(r'^file:\S*$')


class ResourceUri(AnyUrl):
    __slots__ = ()

    allowed_schemes = {'resource'}


class MozExtensionUri(AnyUrl):
    __slots__ = ()

    allowed_schemes = {'moz-extension'}


class Model(BaseModel):
    class Config:
        alias_generator = camel
        allow_population_by_field_name = True
        extra = 'forbid'
        orm_mode = True
        # use_enum_values = True
        validate_assignment = True


class LooseModel(Model):
    class Config:
        extra = 'ignore'


class DynamicModel(Model):
    class Config:
        extra = 'allow'


# class OrmModel(Model):
#     class Config:
#         orm_mode = True

#     @classmethod
#     def from_orm(cls, obj: tuple[Any]) -> 'Model':
#         return cls(**dict(zip(cls.__fields__, obj)))


__all__ = [
    'AnyUrl',
    'AnyHttpUrl',
    'HttpUrl',
    'IntEnum',
    'Path',
    'StrEnum',
    'camel',
    'date',
    'datetime',
    'validator',
]
