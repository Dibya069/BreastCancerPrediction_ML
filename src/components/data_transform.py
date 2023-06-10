import pandas as ps
import numpy as np
import sys, os

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

from sklearn.impute import SimpleImputer ##Handle Missing value
from sklearn.preprocessing import StandardScaler    ## Handel Features scaling
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

@dataclass
class DataTranformationConfig:
    preprocessro_obj_file_path = os.path.join("artifacts", "Preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = Dat