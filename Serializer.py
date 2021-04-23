import json_parser
import pickle_parser
import toml_parser
import yaml_parser


class Serializer:
    def create_serializer(ext):
        if ext == ".json":
            return json_parser.Json
        elif ext == ".toml":
            return toml_parser.Toml
        elif ext == ".yaml":
            return yaml_parser.Yaml
        else:
            return pickle_parser.Pickle
