import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

import parse_data

# data preparation
df = parse_data.df.dropna()
X = df.drop(columns=["median_house_value", "longitude", "latitude"])
y = df["median_house_value"]
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# %% id="wWeJmcbupWdK"


def compare():
    depths = range(1, 31)
    rmse_train = []
    rmse_test = []

    for d in depths:
        dt = DecisionTreeRegressor(max_depth=d, random_state=42)
        dt.fit(X_train, y_train)

        rmse_train.append(np.sqrt(mean_squared_error(y_train, dt.predict(X_train))))
        rmse_test.append(np.sqrt(mean_squared_error(y_test, dt.predict(X_test))))

    plt.figure(figsize=(7, 5))
    plt.plot(depths, rmse_train, label="Train RMSE")
    plt.plot(depths, rmse_test, label="Validation RMSE")
    plt.xlabel("Tree Depth")
    plt.ylabel("RMSE")
    plt.title("Overfitting in Decision Tree")
    plt.legend()
    plt.grid(True)
    plt.show()
    return rmse_train, rmse_test, depths


# %% id="0aa1UKx3ZgHi"
def gap(rmse_train, rmse_test, depths):
    gap = np.array(rmse_test) - np.array(rmse_train)

    plt.figure()
    plt.plot(depths, gap)
    plt.xlabel("Tree Depth")
    plt.ylabel("RMSE Gap (test - train)")
    plt.title("Generalization Gap")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    rmse_train, rmse_test, depths = compare()
    gap(rmse_train, rmse_test, depths)
