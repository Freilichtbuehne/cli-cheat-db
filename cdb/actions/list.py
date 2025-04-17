from cdb.lib.fs import FileSystem
from cdb.lib.properties import CheatProperty, VersionProperty, Color, colorize

fs = FileSystem()


def list_cheats(args: any) -> None:
    all_cheats = fs.get_all_cheats()
    for cheat in all_cheats:
        # get properties
        properties = fs.load_cheat_properties(cheat)
        cp = CheatProperty()
        cp.load(cheat, properties)

        print(
            colorize(f"[{cp.id}] ", Color.CYAN) + (cp.properties["description"] or "") + (f" {cp.properties['url']}" if cp.properties["url"] else "")
        )

        # print all versions
        for version in fs.get_all_versions(cheat):
            properties = fs.load_cheat_version_properties(cheat, version)
            vp = VersionProperty()
            vp.load(cheat, version, properties)
            detected = vp.properties["detected"]
            print(
                "\t"
                + colorize(f"[{vp.version}] ", Color.GREEN if detected else Color.RED)
                + "\t" + (vp.properties["description"] or "")
                + f"\tFiletype: {vp.properties['filetype']}"
                + f"\t({colorize('detected', Color.GREEN) if detected else colorize('undetected', Color.RED)})"
            )


def list_versions(args: any) -> None:
    all_versions = fs.get_all_versions(args.id)
    for version in all_versions:
        properties = fs.load_cheat_version_properties(args.id, version)
        vp = VersionProperty()
        vp.load(args.id, version, properties)
        detected = vp.properties["detected"]
        print(
            colorize(f"[{vp.version}] ", Color.GREEN if detected else Color.RED)
            + "\t" + (vp.properties["description"] or "")
            + f"\tFiletype: {vp.properties['filetype']}"
            + "\t" + (f"Arch: {vp.properties['arch']}" if vp.properties["arch"] != 'any' else "")
            + f"\tPaid: {vp.properties['paid']}"
            + f"\t({colorize('detected', Color.GREEN) if detected else colorize('undetected', Color.RED)})"
        )


def search(args: any) -> None:
    if 'id' in args and args.id:
        list_versions(args)
    else:
        list_cheats(args)
