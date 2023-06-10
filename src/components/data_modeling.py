import sys, os
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj, evaluate_mdoel

from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

@dataclass
class DataModelTrainConfig:
    train_model_path = os.path.join("artifacts", "model.pkl")

class ModelTrainig:
    def __init__(self):
        self.model_training_config = DataModelTrainConfig()

    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("Splitting Dependent and Independet variable form train and test data")
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )

            ## Automation model training process
            models = {
                "Random Forest": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Gradient Classification": GradientBoostingClassifier()
            }

            model_report: dict = evaluate_mdoel(x_train, x_test, y_train, y_test, models)
            print("\n=======================================================================")
            logging.info(f"Model Reports: {model_report}")

            ## To get the best model score forom the deictionary
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            print(f"best model found, model name: {best_model_name}, R2_score: {best_model_score}")
            print("\n=========================================================================")
            logging.info(f"best model found, model name: {best_model_name}, R2_score: {best_model_score}")

            save_obj(
                file_path=self.model_training_config.train_model_path,
                obj=best_model
            )



        except Exception as e:
            logging.info("The error is Rasised in Data Model Training Stage")
            raise CustomException(e, sys)