# import modules
import normalization
from normalization import wine_quality

import pandas as pd
from sklearn.model_selection import train_test_split

# devide data in train and test
X_train,X_test,y_train,y_test = train_test_split(wine_quality.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13]],wine_quality.iloc[:,[14]],test_size=0.1,random_state=1)

# view data
#print("Train data lenth:", len(X_train))
#print("Test data lenth:", len(X_test), "\n")
