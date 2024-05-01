from cdb.lib.fs import FileSystem
from cdb.lib.editor import Editor

fs = FileSystem()


def comment(args: any) -> None:
    comment_path = fs.get_comment_path(args.id, args.version)
    # open this file with editor
    editor = Editor()
    editor.open(comment_path)
