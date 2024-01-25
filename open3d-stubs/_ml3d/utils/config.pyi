"""
This type stub file was generated by pyright.
"""

from addict import dict

class ConfigDict(dict):
    def __missing__(self, name): # -> NoReturn:
        ...
    
    def __getattr__(self, name):
        ...
    


def add_args(parser, cfg, prefix=...):
    ...

class Config:
    def __init__(self, cfg_dict=...) -> None:
        ...
    
    def dump(self, *args, **kwargs): # -> None:
        """Dump to a string."""
        ...
    
    @staticmethod
    def merge_cfg_file(cfg, args, extra_dict): # -> tuple[Unknown, Unknown, Unknown]:
        """Merge args and extra_dict from the input arguments.

        Merge the dict parsed by MultipleKVAction into this cfg.
        """
        ...
    
    @staticmethod
    def merge_module_cfg_file(args, extra_dict): # -> tuple[dict[Unknown, Unknown], dict[Unknown, Unknown], dict[Unknown, Unknown]]:
        """Merge args and extra_dict from the input arguments.

        Merge the dict parsed by MultipleKVAction into this cfg.
        """
        ...
    
    def merge_from_dict(self, new_dict): # -> Config:
        """Merge a new into cfg_dict.

        Args:
            new_dict (dict): a dict of configs.
        """
        ...
    
    @staticmethod
    def load_from_file(filename): # -> Config:
        ...
    
    def __getattr__(self, name): # -> Any:
        ...
    
    def __getitem__(self, name): # -> Any:
        ...
    


