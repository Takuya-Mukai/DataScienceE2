import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

import parse_data

df = parse_data.df.dropna()
X = df.drop(columns=["median_house_value", "longitude", "latitude"])
y = df["median_house_value"]
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

# train 上での評価（= validation なし評価の代替）
rmse_train = np.sqrt(mean_squared_error(y_train, dt.predict(X_train)))

# test 上での評価（= 正しい評価）
rmse_test = np.sqrt(mean_squared_error(y_test, dt.predict(X_test)))

print("RMSE (train only, invalid evaluation):", rmse_train)
print("RMSE (with validation):", rmse_test)
