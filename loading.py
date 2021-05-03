import pandas as pd
import os
import re

Data = pd.read_csv('./WikiHow-Dataset/wikihowAll.csv')
Data = Data.astype(str)
print(Data.head())