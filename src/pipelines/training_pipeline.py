import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngesion

if __name__ == '__main__':
    obj=DataIngesion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
