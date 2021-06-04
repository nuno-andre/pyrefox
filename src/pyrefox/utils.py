from os import PathLike
import json

import lz4.block

MOZLZ4_MAGIC = b'mozLz40\0'


def read_mozlz4(filepath: PathLike) -> dict:
    with open(filepath, 'rb') as f:
        if f.read(8) != MOZLZ4_MAGIC:
            raise OSError(f'Not a mozlz4 file: {filepath}')
        s = lz4.block.decompress(f.read())
        return json.loads(s)


def write_mozlz4(dct: str, filepath: PathLike) -> None:
    s = json.dumps(dct, separators=(',', ':'))
    with open(filepath, 'wb') as f:
        f.write(MOZLZ4_MAGIC + lz4.block.compress(s))


def read_json(filepath: PathLike) -> dict:
    with open(filepath) as f:
        return json.loads(f.read())


CAPS = {'Guid': 'GUID', 'Uri': 'URI', 'Url': 'URL'}


def camel(string: str) -> str:
    first, *rest = string.split('_')
    return first + ''.join(CAPS.get(w, w) for w in map(str.capitalize, rest))


def _camel(string: str) -> str:
    return '_' + camel(string)
