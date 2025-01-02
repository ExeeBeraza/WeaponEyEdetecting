import logging

import yaml


class Loader:
    def __init__(self):
        self.loader = yaml.SafeLoader

    def load_configs(self):
        file_name = 'default.yml'
        try:
            file = open('config/' + file_name, 'r')
            return yaml.safe_load(file), None
        except FileNotFoundError:
            return None, FileNotFoundError("No such file " + file_name)
