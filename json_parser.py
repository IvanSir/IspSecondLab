import json
from Utilities import convert, deconvert


class Json:

    def dump(obj, file="format_files/testjson.json"):
        with open(file, 'w') as fw:
            fw.write(Json.dumps(obj))

    def dumps(obj):
        packed = convert(obj)
        return json.dumps(packed)

    def load(file="format_files/testjson.json"):
        with open(file, 'r') as fr:
            data = fr.read()
            unpacked = Json.loads(data)
        return unpacked

    def loads(src):
        packed = json.loads(src)
        return deconvert(packed)
