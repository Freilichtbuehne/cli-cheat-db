from cdb.lib.fs import FileSystem
from cdb.lib.properties import CheatProperty, VersionProperty

fs = FileSystem()


def update(args: any) -> None:
    # load properties
    json_properties = fs.load_cheat_version_properties(args.id, args.version)

    properties = VersionProperty()
    properties.load(args.id, args.version, json_properties)
    properties.update(args)

    # save properties
    fs.save_cheat_version_properties(args.id, args.version, properties)
