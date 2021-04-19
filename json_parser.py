from io import FileIO
from typing import Any, IO
import json
from Utilities import convert, deconvert


class Json:

    def dump(obj, file="test.json"):
        f = open(file, 'w')
        f.write(Json.dumps(obj))
        f.close()

    def dumps(obj):
        packed = convert(obj)
        return json.dumps(packed)

    def load(file="test.json"):
        f = open(file, 'r')
        packed = Json.loads(f.read())
        unpacked = deconvert(packed)
        f.close()
        return unpacked

    def loads(src):
        packed = json.loads(src)
        return deconvert(packed)
