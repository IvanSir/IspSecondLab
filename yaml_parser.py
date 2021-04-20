import yaml
from Utilities import convert, deconvert


class Yaml:

    def dump(obj, file="../format_files/testyaml.yaml"):
        packed = convert(obj)
        with open(file, 'w') as fw:
            yaml.dump(packed, fw)

    def dumps(obj):
        packed = convert(obj)
        return yaml.dump(packed)

    def load(file="../format_files/testyaml.yaml"):
        with open(file, 'r') as fr:
            packed = yaml.load(fr, Loader=yaml.FullLoader)
        return deconvert(packed)

    def loads(src):
        packed = yaml.load(src, Loader=yaml.FullLoader)
        return deconvert(packed)
