class Color:
    # define console colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"


def colorize(string: str, color: str) -> str:
    return color + string + Color.RESET


class CheatProperty:
    def __init__(self, args: any = None) -> None:
        self.id = None
        self.properties = {}

        # load from args
        if args is not None:
            self.new(args)

    def new(self, args: any) -> None:
        self.id = args.id
        self.properties = {"url": args.url, "description": args.description}

    def load(self, id: str, json_properties: any) -> None:
        self.id = id
        self.properties = json_properties


class VersionProperty:
    def __init__(self, args: any = None):
        self.id = None
        self.version = None
        self.properties = {}

        # load from args
        if args is not None:
            self.new(args)

    def new(self, args: any) -> None:
        self.id = args.id
        self.version = args.version
        self.properties = {
            "path": args.path,
            "filetype": args.filetype,
            "arch": args.arch,
            "paid": args.paid and True or False,
            "free": args.free and True or False,
            "detected": args.detected and True or False,
            "undetected": args.undetected and True or False,
            "description": args.description,
            "url": args.url,
        }

    def load(self, id: str, version: str, json_properties: any) -> None:
        self.id = id
        self.version = version
        self.properties = json_properties

    def update(self, args: any) -> None:
        if args.url is not None:
            self.properties["url"] = args.url
        if args.description is not None:
            self.properties["description"] = args.description
        if args.detected is True:
            self.properties["detected"] = True
            self.properties["undetected"] = False
        if args.undetected is True:
            self.properties["detected"] = False
            self.properties["undetected"] = True
        if args.filetype is not None:
            self.properties["filetype"] = args.filetype
        if args.arch is not None:
            self.properties["arch"] = args.arch
        if args.paid is True:
            self.properties["paid"] = True
            self.properties["free"] = False
        if args.free is True:
            self.properties["paid"] = False
            self.properties["free"] = True
