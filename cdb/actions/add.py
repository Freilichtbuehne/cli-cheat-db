from cdb.lib.fs import FileSystem
from cdb.lib.properties import CheatProperty, VersionProperty

fs = FileSystem()


def add(args: any) -> None:
    properties = VersionProperty(args)
    fs.new_cheat_version(args.id, args.version, args.path, properties)
