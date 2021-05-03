import pandas as pd
import os
import re

# TODO(zbamberger): We cannot read the entire CSV on a windows system due to memory issues.
#  The `nrows` parameter works as a temporary solution, but we should converge on a more robust solution.
Data = pd.read_csv('./WikiHow-Dataset/wikihowAll.csv', nrows=100)
Data = Data.astype(str)
print(Data.head())