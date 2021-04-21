import json_parser
import pickle_parser
import toml_parser
import yaml_parser


class Serializer:
    def create_serializer(format):
        if format == ".json":
            return json_parser.Json
        elif format == ".toml":
            return toml_parser.Toml
        elif format == ".yaml":
            return yaml_parser.Yaml
        else:
            return pickle_parser.Pickle
