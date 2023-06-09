import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utils import export_collection_as_dataframe

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
        self.ingestion_configuration = DataIngestionConfig()

    def initiate_data_ingestioin(self):
        logging.info("Data Ingestion Mode START")

        try:
            df: pd.DataFrame = export_collection_as_dataframe(
                db_name="ML_project", collection_name="BreastCancer"
            )
            logging.info("Exported collection as dataframe")


            os.makedirs( os.path.dirname(self.ingestion_configuration.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_configuration.raw_data_path, index=False, header=True)
            logging.info("Raw Data is created")

            train_set, test_set = train_test_split(df, test_size=0.3, random_state=42)
            train_set.to_csv( self.ingestion_configuration.train_data_path, index=False, header=True )
            test_set.to_csv( self.ingestion_configuration.test_data_path, index=False, header=True )
            logging.info("train and test Data is created")

            return (
                self.ingestion_configuration.train_data_path,
                self.ingestion_configuration.test_data_path,
            )
        except Exception as e:
            logging.info("ERROR in DataIngestion Stage")
            raise CustomException(e, sys)