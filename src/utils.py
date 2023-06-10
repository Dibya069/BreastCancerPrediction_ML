import os, sys
import pandas as pd
import numpy as np
import pickle

from src.logger import logging
from src.exception import CustomException

from pymongo import MongoClient
from sklearn.metrics import r2_score

## ======================================================================================================================

def export_collection_as_dataframe(collection_name, db_name):
    try:
        mongo_client = MongoClient("mongodb+srv://mohanty:RAM@cluster0.1owxeev.mongodb.net/?retryWrites=true&w=majority")
        collection = mongo_client[db_name][collection_name]

        # Print debug information
        print("Connection string:", mongo_client)
        print("Database name:", db_name)
        print("Collection name:", collection_name)

        num_samples = collection.count_documents({})  # Count the number of documents in the collection
        if num_samples == 0:
            raise ValueError("The collection is empty. Please ensure there are samples in the collection.")
        

        df = pd.DataFrame(list(collection.find()))

        if "_id" in df.columns.to_list():
            df = df.drop(columns=["_id"], axis=1)

        df.replace({"na": np.nan}, inplace=True)

        return df

    except Exception as e:
        raise CustomException(e, sys)

## ======================================================================================================================

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
## ======================================================================================================================

def evaluate_mdoel( x_train, y_train, x_test, y_test, models ):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            ## train model
            model.fit(x_train, y_train)

            ## predict model
            y_test_pred = model.predict(x_test)
            test_mdoel_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_mdoel_score
        return report
    except Exception as e:
        raise CustomException(e, sys)
    
## ======================================================================================================================

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)