#!/usr/bin/python
import argparse
import configparser
from pathlib import Path
from JptySerializer.Serializer import Serializer


def serialize(dest_format, path_file):
    serializer = Serializer.create_serializer(dest_format)
    src_format = Path(path_file).suffix
    if src_format == dest_format:
        return
    deserializer = Serializer.create_serializer(src_format)
    abs_path = Path(path_file)
    loaded = deserializer.load(path_file)
    serializer.dump(loaded, Path(abs_path.parent, f"{abs_path.stem}{dest_format}"))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--config", dest="config_file", help="Path for the configuration file")
    parser.add_argument("-f", "--format", dest="dest_format", help="New file format")
    parser.add_argument("-p", "--path", dest="path_file", help="Path for the input file")
    args = parser.parse_args()

    if args.config_file is not None:
        config = configparser.ConfigParser()
        config.read(args.config_file)
        serialize(config["settings"]["dest_format"], config["settings"]["path_file"])
    else :
        serialize(args.dest_format, args.path_file)


main()
