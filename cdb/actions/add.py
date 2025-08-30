#import pefile

from cdb.lib.fs import FileSystem
from cdb.lib.properties import CheatProperty, VersionProperty

fs = FileSystem()


def add(args: any) -> None:
    is_dir = fs.is_dir(args.path)

    # auto-detect the properties
    if not is_dir:
        # filetype
        if args.path.endswith(".lua"):
            args.filetype = "lua"
        elif args.path.endswith(".dll"):
            args.filetype = "dll"
        elif args.path.endswith(".exe"):
            args.filetype = "exe"
    
    if not is_dir and not args.filetype:
        raise ValueError("File type not specified, failed to auto-detect")

    properties = VersionProperty(args)
    fs.new_cheat_version(args.id, args.version, args.path, properties)
