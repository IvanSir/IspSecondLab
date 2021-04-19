import yaml
from Utilities import convert, deconvert


class Yaml:

    def dump(obj, file="test.json"):
        f = open(file, 'w')
        f.write(Yaml.dumps(obj))
        f.close()

    def dumps(obj):
        packed = convert(obj)
        return yaml.dump(packed)

    def load(file="test.json"):
        f = open(file, 'r')
        packed = Yaml.loads(f.read())
        unpacked = deconvert(packed)
        f.close()
        return unpacked

    def loads(src):
        packed = yaml.load(src, Loader=yaml.FullLoader)
        return deconvert(packed)
