# cli-cheat-db
Simple CLI tool to assist creating cheat detections

# Installation

```
git clone https://github.com/Freilichtbuehne/cli-cheat-db.git`
cd cli-cheat-db

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Edit config.yaml
cp config/config.yaml.example config/config.yaml
nano config/config.yaml
```

# Usage

**Create a new cheat:**

`./cdb.py new <name>`

`./cdb.py new <name> --url "https://..." --description "this cheat is bad"`


**Add a sample (version) to a cheat:**

`./cdb.py add <name> <version> <folder_or_file>`

`./cdb.py add <name> <version> <folder_or_file> --undetected --free --arch 32 --filetype dll`

**Update a sample (version) of a cheat:**

`./cdb.py update <name> <version> --detected`

**Comment on a sample (version) of a cheat (will open an editor to write the comment):**

`./cdb.py comment <name> <version>`
