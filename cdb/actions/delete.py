from cdb.lib.fs import FileSystem
from cdb.lib.properties import CheatProperty, VersionProperty, Color, colorize

fs = FileSystem()

def delete_cheat(args: any) -> None:
    fs.delete_cheat(args.id)

def delete_version(args: any) -> None:
    fs.delete_cheat_version(args.id, args.version)

def delete(args: any) -> None:
    if not args.force:
        if args.version:
            print_msg = "Are you sure you want to delete version {} from cheat {}?".format(args.version, args.id)
        else:
            print_msg = "Are you sure you want to delete cheat {} and all its versions?".format(args.id)
        if input(print_msg + " [y/N]: ").lower() != "y":
            return

    if args.version:
        delete_version(args)
    else:
        delete_cheat(args)
