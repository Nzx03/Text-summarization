import os
import sys
from box.exceptions import BoxValueError
import yaml
from src.logging import logging
from src.exception import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations 
def read_yaml_file(path_to_yaml:Path) -> ConfigBox:#config box allows to access keys as attributes

    try:
        with open(path_to_yaml) as file:
            content=yaml.safe_load(file)
            logging.info(f"yaml file: {path_to_yaml} has been loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)
    

@ensure_annotations
def create_dir(path_to_dir:list,verbose=True):
    
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
           logging.info(f"Created directory at:{path}")


@ensure_annotations
def get_size(path:Path)-> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f" {size_in_kb} KB"