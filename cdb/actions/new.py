from cdb.lib.fs import FileSystem
from cdb.lib.properties import CheatProperty, VersionProperty

fs = FileSystem()


def new(args: any) -> None:
    fs.new_cheat(args.id, CheatProperty(args))
