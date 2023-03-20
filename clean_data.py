# import modules
import pandas as pd
import numpy as np

import read_data
from read_data import wine_quality
from read_data import columns_names

# remove duplicates
wine_quality = wine_quality.drop_duplicates(keep="first")

# view data 
# print(wine_quality.head())
# print("DF lenth after removing duplicates:", len(wine_quality), "\n")

# check presents of null data
# print(wine_quality.isna().any(), "\n")
