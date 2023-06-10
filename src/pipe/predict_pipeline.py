import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj, load_object

from dataclasses import dataclass

@dataclass
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "Preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.info("Exception does in Prediction")
            raise CustomException(e, sys)
        
    
class CustomData:
    def __init__(self):
        pass

    def get_data_as_dataframe(self):
        try:
            pass
        except Exception as e:
            logging.info("Exception does in Prediction Pipeline")
            raise CustomException(e, sys)
