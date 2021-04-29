import configparser
from pathlib import Path
import json

class LoadFile:
    def __init__(self, folder_name = "configs", file_name = "config.ini"):
        self.file_name = file_name
        # Path(__file__) return the whole path of the current files
        # .parent.parent is similar to ../
        self.path = ((Path(__file__).parent.parent) / folder_name / file_name).resolve()
        
    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.path)
        return config
    
    def path_str(self):
        return str(self.path)
        