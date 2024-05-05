import os
import json
import shutil
from cdb.lib.properties import CheatProperty, VersionProperty

"""
Direcory structure:
    cdb/
        ...
    data/
        cheat_id_1/
            properties.json
            versions/
                version_id_1/
                    properties.json
                    comments.txt
                    sample/
                        ...
                version_id_2/
                    ...
                ...
        cheat_id_2/
            ...
"""


class FileSystem:
    def __init__(self) -> None:
        self.root = "data/"
        self.cheat_dir = self.root + "{}"
        self.cheat_properties = self.root + "{}/properties.json"
        self.cheat_version_properties = self.root + "{}/versions/{}/properties.json"
        self.cheat_version = self.root + "{}/versions/{}"
        self.cheat_version_dir = self.root + "{}/versions"
        self.cheat_version_sample = self.root + "{}/versions/{}/sample"
        self.cheat_version_comments = self.root + "{}/versions/{}/comments.txt"
        # check if structure exists
        if not os.path.exists(self.root):
            os.makedirs(self.root)

    def get_comment_path(self, id: str, version: str) -> str:
        # check if cheat exists
        if not os.path.exists(self.cheat_dir.format(id)):
            raise FileNotFoundError("Cheat {} not found".format(id))
        # check if version exists
        if not os.path.exists(self.cheat_version.format(id, version)):
            raise FileNotFoundError("Cheat {} version {} not found".format(id, version))
        return self.cheat_version_comments.format(id, version)

    def get_properties_path(self, id: str, version: str = None) -> str:
        if version is None:
            return self.cheat_properties.format(id)
        return self.cheat_version_properties.format(id, version)

    def get_all_cheats(self) -> list:
        return os.listdir(self.root)

    def get_all_versions(self, id: str) -> list:
        # check if cheat exists
        if not os.path.exists(self.cheat_dir.format(id)):
            raise FileNotFoundError("Cheat {} not found".format(id))

        # check if versions directory exists
        if not os.path.exists(self.cheat_version_dir.format(id)):
            return []

        return os.listdir(self.cheat_version_dir.format(id))

    def load_cheat_properties(self, id: str) -> any:
        property_file = self.cheat_properties.format(id)
        if not os.path.exists(property_file):
            raise FileNotFoundError("Properties file for cheat {} not found".format(id))
        with open(property_file, "r") as f:
            return json.load(f)

    def load_cheat_version_properties(self, id: str, version: str) -> any:
        property_file = self.cheat_version_properties.format(id, version)
        if not os.path.exists(property_file):
            raise FileNotFoundError(
                "Properties file for cheat {} version {} not found".format(id, version)
            )
        with open(property_file, "r") as f:
            return json.load(f)

    def save_cheat_properties(self, id, properties: CheatProperty) -> None:
        properties_file = self.cheat_properties.format(id)
        with open(properties_file, "w") as f:
            json.dump(properties.properties, f, indent=4)

    def save_cheat_version_properties(
        self, id, version, properties: VersionProperty
    ) -> None:
        properties_file = self.cheat_version_properties.format(id, version)
        with open(properties_file, "w") as f:
            json.dump(properties.properties, f, indent=4)

    def new_cheat(self, id: str, properties: CheatProperty) -> None:
        cheat_dir = self.cheat_dir.format(id)
        if os.path.exists(cheat_dir):
            raise FileExistsError("Cheat {} already exists".format(id))
        os.makedirs(cheat_dir)
        self.save_cheat_properties(id, properties)

    def new_cheat_version(
        self, id: str, version: str, path: str, properties: VersionProperty
    ) -> None:
        cheat_dir = self.cheat_dir.format(id)
        if not os.path.exists(cheat_dir):
            raise FileNotFoundError("Cheat {} not found".format(id))
        version_dir = self.cheat_version.format(id, version)
        sample_dir = self.cheat_version_sample.format(id, version)
        if os.path.exists(version_dir):
            raise FileExistsError(
                "Cheat {} version {} already exists".format(id, version)
            )
        os.makedirs(version_dir)
        self.save_cheat_version_properties(id, version, properties)
        # check if path is a file or directory
        if os.path.isfile(path):
            os.makedirs(sample_dir)
            shutil.copy(path, sample_dir + "/")
        else:
            shutil.copytree(path, sample_dir)

    def delete_cheat(self, id: str) -> None:
        cheat_dir = self.cheat_dir.format(id)
        if not os.path.exists(cheat_dir):
            raise FileNotFoundError("Cheat {} not found".format(id))
        shutil.rmtree(cheat_dir)

    def delete_cheat_version(self, id: str, version: str) -> None:
        cheat_dir = self.cheat_dir.format(id)
        if not os.path.exists(cheat_dir):
            raise FileNotFoundError("Cheat {} not found".format(id))
        version_dir = self.cheat_version.format(id, version)
        if not os.path.exists(version_dir):
            raise FileNotFoundError("Cheat {} version {} not found".format(id, version))
        shutil.rmtree(version_dir)

    def is_dir(self, path: str) -> bool:
        return os.path.isdir(path)
