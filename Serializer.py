import json_parser
import pickle_parser
import toml_parser
import yaml_parser


class Serializer:
    def create_serializer(format):
        if format == "JSON":
            return json_parser.Json
        elif format == "TOML":
            return toml_parser.Toml
        elif format == "YAML":
            return yaml_parser.Yaml
        else:
            return pickle_parser.Pickle
