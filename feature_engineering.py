# import modules
import pandas as pd
import numpy as np

import clean_data
from clean_data import wine_quality

# ignore warnings
import warnings
warnings.filterwarnings('ignore')

# remove quality before adding new features
temp_quality = wine_quality["quality"]
wine_quality = wine_quality.drop("quality", axis="columns")

# add fixed volatile acidity ratio
wine_quality["fix_vol_acidity_ratio"] = wine_quality.apply(lambda row: row.volatile_acidity / row.fixed_acidity, axis=1)

# add free total sulfur dioxide ratio
wine_quality["free_total_suldio_ratio"] = wine_quality.apply(lambda row: row.free_sulfur_dioxide / row.total_sulfur_dioxide, axis=1)

# add ph density ratio 
wine_quality["pH_density_ratio"] = wine_quality.apply(lambda row: row.pH / row.density, axis=1)

# move quality back to the end of the table
wine_quality["quality"] = temp_quality

#print('\nData after feature engineering:')
#print(wine_quality.head())