import yaml
import os
import logging
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(cur_dir))
config_dir = os.path.join(project_dir, "config")
config_file = os.path.join(config_dir, "config.yaml")

cached_config = None

def load_config() -> dict:
    global cached_config
    if cached_config:
        return cached_config

    if not os.path.isfile(config_file):
        logging.error(f"File {config_file} does not exist. Did you rename the config.yaml.example to config.yaml?")
        sys.exit(1)

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    cached_config = config
    
    return config
