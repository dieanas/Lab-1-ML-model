# import modules
import pandas as pd

import feature_engineering
from feature_engineering import wine_quality

# save new columns names
names = wine_quality.columns.tolist()

# normalization 
columns_for_normalization = wine_quality.columns.tolist()[:-1]
for i in columns_for_normalization:
	wine_quality[i] = (wine_quality[i] - wine_quality[i].min()) / (wine_quality[i].max() - wine_quality[i].min())

wine_quality = pd.DataFrame(wine_quality, columns=names)

# view data 
#print('\nData after normalization:')
#print(wine_quality.head())
