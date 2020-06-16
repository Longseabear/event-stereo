import yaml
import os
import weakref
from pathlib import Path
import torch
import pickle

class ConfigMember(dict):
    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ConfigMember(value)
        return value

    def __setattr__(self, attr, val):
        if attr in vars(self):
            self.set_inst_attr(attr,val)
        else:
            self.__setitem__(attr, val)

class Config(dict):
    def __init__(self, file_path):
        super(Config, self).__init__()
        assert os.path.exists(file_path), "FILE NOT FOUND ERROR: Config File doesn't exist. : {}".format(file_path)
        if Path(file_path).suffix == '.tar':
            print('load checkpoint file') #AcfRefine -> checkpoint
            state_dict = torch.load(file_path)
            super().__setattr__('member', pickle.loads(state_dict['config']))
            self.member['LOAD_CHECKPOINT_PATH'] = file_path
            self.member['MODEL_NAME'] = Path(file_path).name
        else:
            try:
                with open(file_path, 'r') as f:
                    super().__setattr__('member', yaml.load(f))
            except:
                assert False

    def keys(self):
        return self.member.keys()

    def __getitem__(self, key):
        return self.member[key]

    def __setitem__(self, key, value):
        self.member[key] = value

    def set_inst_attr(self, attr, val):
        if attr == 'member':
            raise Exception("attr exception")
        super().__setattr__(attr,val)

    def __setattr__(self, attr, val):
        if attr in vars(self):
            self.set_inst_attr(attr, val)
        else:
            self.__setitem__(attr, val)

    def __contains__(self, item):
        return self.member.__contains__(item)

    def __getattr__(self, name):
        value = self.member[name]
        if isinstance(value, dict):
            value = ConfigMember(value)
        return value

    def __getstate__(self):
        d = self.member
        return d

    def __setstate__(self, state):
        super().__setattr__('member', state)
        return self

    def __str__(self):
        return str(self.member)