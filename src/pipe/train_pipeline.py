import sys, os
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestioin()
    print(train_data_path, test_data_path)
