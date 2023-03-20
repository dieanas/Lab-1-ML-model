# import modules
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import train_test_devision
from train_test_devision import X_train, X_test, y_train, y_test
from feature_engineering import wine_quality
from normalization import names

# use decision tree classifier model
tree_model = DecisionTreeClassifier(max_depth=10)

# fit model
tree_model.fit(X_train,y_train)

# score x and y - test and train
print("Score the X-train with Y-train is :", tree_model.score(X_train,y_train))
print("Score the X-test  with Y-test  is :", tree_model.score(X_test,y_test))

# select important columns
importance = [names[:-1], tree_model.feature_importances_]
pd.set_option('display.max_columns', None)
print("The Important columns \n", pd.DataFrame(importance))

print("\nThe classes:",tree_model.classes_)
y_pred_T = tree_model.predict(X_test)

print("\nModel Evaluation Decision Tree - accuracy score:" , accuracy_score(y_test,y_pred_T))
