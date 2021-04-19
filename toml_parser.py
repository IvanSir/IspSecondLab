from io import FileIO
from typing import Any, IO
import pytomlpp
from Utilities import convert, deconvert


class Toml:

    def dump(obj, file="test.json"):
        f = open(file, 'w')
        f.write(Toml.dumps(obj))
        f.close()

    def dumps(obj):
        packed = convert(obj)
        return pytomlpp.dumps(packed)

    def load(file="test.json"):
        f = open(file, 'r')
        packed = Toml.loads(f.read())
        unpacked = deconvert(packed)
        f.close()
        return unpacked

    def loads(src):
        packed = pytomlpp.loads(src)
        return deconvert(packed)
