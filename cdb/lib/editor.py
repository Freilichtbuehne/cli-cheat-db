import os
import shutil

editors = {"posix": ["nano", "vim", "mimeopen -d"], "nt": ["notepad.exe"]}


class Editor:
    def __init__(self) -> None:
        # get operating system
        self.os = os.name

    @property
    def editors(self) -> dict:
        return editors[self.os]

    def open(self, path: str) -> None:
        # run first available editor
        for editor in self.editors:
            if shutil.which(editor):
                # os command injection is out of scope for this project
                os.system("{} {}".format(editor, path))
                break
        else:
            raise FileNotFoundError("No editor found")
