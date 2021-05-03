import pandas as pd
import os
import re

Data = pd.read_csv('./WikiHow-Dataset/all_train.txt')
Data = Data.astype(str)
print(Data.head())