import os
import urllib.request as request  
import zipfile
from src.logging import logging
from src.utils.modular import get_size
from pathlib import Path
from src.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} dowmloaded with following info; {headers}")

        else:

            logging.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as file:
            file.extractall(unzip_path)