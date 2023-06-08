import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split

import sys, os
from dataclasses import dataclass

## Initialize the Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts', 'train.csv')
    test_data_path=os.path.join('artifacts', 'test.csv')
    raw_data_path=os.path.join('artifacts', 'raw.csv')

## Creating data Ingestion calss
class DataIngestion:
    def __init__(self):
        self.ingestion_configuration = DataIngestion()

    def initiate_data_ingestioin(self):
        logging.info("Data Ingestion Mode START")

        try:
            pass
        except Exception as e:
            logging.info("ERROR in DataIngestion Stage")
            raise CustomException(e, sys)