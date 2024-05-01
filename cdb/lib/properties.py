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

    def __str__(self):
        # TODO: return a string representation of the object
        return print(self.id, self.properties)


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
            "file-type": args.file_type,
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
        if args.file_type is not None:
            self.properties["file-type"] = args.file_type
        if args.arch is not None:
            self.properties["arch"] = args.arch
        if args.paid is True:
            self.properties["paid"] = True
            self.properties["free"] = False
        if args.free is True:
            self.properties["paid"] = False
            self.properties["free"] = True
