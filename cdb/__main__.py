import argparse
from cdb.actions.add import add
from cdb.actions.new import new
from cdb.actions.update import update
from cdb.actions.comment import comment

from cdb.lib.validators import ReValidator

def main():
    version_validator = ReValidator(r"^[a-zA-Z0-9_-]+$")
    id_validator = ReValidator(r"^[a-zA-Z0-9_-]+$")

    parser = argparse.ArgumentParser(description="Store and manage your cheats locally via CLI")

    parser.add_argument("-v", "--verbose",  action='store_true', help="Increase output verbosity")

    subparsers = parser.add_subparsers(title="actions", dest='actions')
    parser_new = subparsers.add_parser("new",
                                        add_help=False,
                                        description="Creates a new cheat",
                                        help="When created, samples of this cheat can be added using 'add'")
    parser_new.add_argument("id", type=id_validator, help="Identifier for the cheat")
    parser_new.add_argument("--url", type=str, help="URL to the resource to download the cheat")
    parser_new.add_argument("--description", type=str, help="Description of the cheat")


    parser_new = subparsers.add_parser("add",
                                        add_help=False,
                                        description="Add a new sample to a cheat",
                                        help="The cheat must be first defined with the 'new' action")
    parser_new.add_argument("id", type=id_validator, help="Identifier for the cheat")
    parser_new.add_argument("version", type=version_validator, help="Identifier for this version of the cheat (e.g. v1)")
    parser_new.add_argument("path", type=str, help="Path to the file or directory to add")
    parser_new.add_argument("--file-type", choices = [ "Lua", "DLL", "EXE" ], default = None, help="File type of the cheat")
    parser_new.add_argument("--arch", choices = [ "64", "32", "any" ], default = "any", help="Architecture of the cheat")
    parser_new.add_argument("--paid", action='store_true', help="Cheats that require a subscription or payment")
    parser_new.add_argument("--free", action='store_true', help="Cheats that are free")
    parser_new.add_argument("--detected", action='store_true', help="Cheat is undetected")
    parser_new.add_argument("--undetected", action='store_true', help="Cheat is detected")
    parser_new.add_argument("--description", type=str, help="Description of this sample")
    parser_new.add_argument("--url", type=str, help="URL to this sample")

    parser_update = subparsers.add_parser("update",
                                        add_help=False,
                                        description="The update parser",
                                        help="Update specific information of a cheat")
    parser_update.add_argument("id", type=id_validator, help="Identifier for the cheat") # TODO regex
    parser_update.add_argument("version", type=version_validator, help="Identifier for this version of the cheat (e.g. v1)")
    parser_update.add_argument("--url", type=str, help="URL to the resource to download the cheat")
    parser_update.add_argument("--description", type=str, help="Description of the cheat")
    parser_update.add_argument("--undetected", action='store_true', help="Cheat is detected")
    parser_update.add_argument("--detected", action='store_true', help="Cheat is undetected")
    parser_update.add_argument("--file-type", choices = [ "Lua", "DLL", "EXE" ], default = None, help="File type of the cheat")
    parser_update.add_argument("--arch", choices = [ "64", "32", "any" ], default = "any", help="Architecture of the cheat")
    parser_update.add_argument("--paid", action='store_true', help="Cheats that require a subscription or payment")
    parser_update.add_argument("--free", action='store_true', help="Cheats that are free")

    parser_comment = subparsers.add_parser("comment",
                                        add_help=False,
                                        description="Add a comment to a sample",
                                        help="Add a comment to a sample")
    parser_comment.add_argument("id", type=id_validator, help="Identifier for the cheat") # TODO regex
    parser_comment.add_argument("version", type=version_validator, help="Identifier for this version of the cheat") # TODO regex


    parsers_list = subparsers.add_parser("list",
                                        add_help=False,
                                        description="List all cheats",
                                        help="List all cheats")
    parsers_list.add_argument("--id", type=id_validator, help="Identifier for the cheat")
    parsers_list.add_argument("--undetected", action='store_true', help="Cheat is detected")
    # TODO: more filters

    args = parser.parse_args()

    if args.actions == "new":
        new(args)
    elif args.actions == "add":
        add(args)
    elif args.actions == "update":
        update(args)
    elif args.actions == "comment":
        comment(args)

if __name__ == "__main__":
    main()
