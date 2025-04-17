import webbrowser
import os
import hashlib

from cdb.lib.fs import FileSystem
from cdb.lib.config import load_config
from cdb.lib.properties import Color, colorize

fs = FileSystem()
config = load_config()

def choose_file(id: str, version: str) -> str:
    """
    Interactively choose a file from the cheat directory.
    Print every file in the directory with numbers.
    Ask the user to choose a file by number.
    """
    directory = fs.get_directory(id, version)
    # List all files in the directory and subdirectories
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    
    # Print all files with numbers
    for i, file in enumerate(files):
        print(f"{colorize(f"[{i}] ", Color.CYAN)}{file}")
    # Ask the user to choose a file by number
    while True:
        try:
            choice = int(input("Choose a file by number: "))
            if 0 <= choice < len(files):
                return files[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def checksum(file_path: str, method: str = "sha1") -> str:
    """
    Calculate the checksum of a file using the specified method.
    """
    hash_obj = None
    if method == "sha1":
        hash_obj = hashlib.sha1()
    elif method == "md5":
        hash_obj = hashlib.md5()
    else:
        raise ValueError(f"Unsupported hash method: {method}")

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()

def open_cmd(param: str) -> None:
    """
    Run a command interactively in the terminal.
    Pipe all output to the terminal.
    Print the command before executing it.
    """
    print_msg = "The following command will be executed:\n"
    print_msg += colorize(param, Color.CYAN) + "\n"
    print_msg += "Do you want to continue? [Y/n]: "
    if input(print_msg).lower() != "n":
        os.system(param)
    else:
        print("Command execution aborted.")

def open_url(param: str) -> None:
    """
    Open a URL in the default web browser.
    """
    print(f"Opening URL: {colorize(param, Color.CYAN)}\n")
    webbrowser.open(param)

def analyze(method, id, version=None) -> None:
    """
    Analyze a cheat using the specified method.
    """

    # check if method is valid
    chosen_method = next((m for m in config["analyze"] if m["name"] == method), None)
    if not chosen_method:
        raise ValueError(f"Method {method} not found")
    
    # check if cheat exists
    if not fs.cheat_exists(id):
        raise FileNotFoundError(f"Cheat {id} not found")
    
    # check if version exists
    if version and not fs.cheat_exists(id, version):
        raise FileNotFoundError(f"Cheat {id} version {version} not found")

    file_path = None
    file_hash = None
    file_dir = None

    # check required parameters
    for req in chosen_method["requires"]:
        if req in ["file", "hash"] and not version:
            raise ValueError(f"Method {method} requires a version")
        
        if req == "dir" and not file_dir:
            file_dir = fs.get_directory(id, version)
            # check if directory exists
            if not os.path.exists(file_dir):
                raise FileNotFoundError(f"Directory {file_dir} not found")

        if req in ["file", "hash"] and not file_path:
            file_path = choose_file(id, version)
            # check if file is a directory
            if not os.path.isfile(file_path):
                raise ValueError(f"File {file_path} is not a file")
        
        if req == "hash" and not file_hash:
            file_hash = checksum(file_path)
            # check if hash is valid
            if not file_hash:
                raise ValueError(f"Hash {file_hash} is not valid")
            
    # insert parameters
    param = chosen_method["param"].format(
        id=id,
        version=version,
        file=file_path,
        hash=file_hash,
        dir=file_dir,
    )

    # get the method
    if chosen_method["type"] == "CMD":
        open_cmd(param)
    elif chosen_method["type"] == "URL":
        open_url(param)
