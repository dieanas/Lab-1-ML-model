# import modules
import pandas as pd

# read data
wine_quality  = pd.read_csv("wine_qt.csv")

# set column names
columns_names = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol", "quality"]
wine_quality.columns = columns_names

# view data
#print('Data:')
#print(wine_quality.head())
#print("DF lenth before removing duplicates:", len(wine_quality))
