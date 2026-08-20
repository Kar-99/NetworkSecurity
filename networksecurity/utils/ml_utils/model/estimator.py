from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e :
            raise NetworkSecurityException(e,sys)

    def predict(self,x) :
        try:
            print("A")
            print(type(x))

            x_transform = self.preprocessor.transform(x)
            print("B")
            print(type(x_transform))

            y_hat = self.model.predict(x_transform)
            print("C")
            print(type(y_hat))

            return y_hat
        except Exception:
            import traceback
            traceback.print_exc()
            raise
        