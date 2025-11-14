import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("./housing.csv")
df = df[df["median_house_value"] < 500001]
df = df[df["housing_median_age"] < 52]


def mapping(name):
    x = df["longitude"]
    y = df["latitude"]
    z = df[name]

    plt.figure()
    plt.scatter(x, y, c=z, cmap="viridis", alpha=0.4, s=10)
    plt.colorbar(label=name)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Housing Prices by Location")
    plt.show(block=True)


def corr_matrix(name1, name2):
    x = df[name1]
    y = df[name2]
    corr = np.corrcoef(x, y)[0, 1]
    plt.figure()
    plt.scatter(x, y, alpha=0.1, s=10)
    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.title(f"Scatter Plot of {name1} vs {name2}")
    plt.show(block=True)
    return corr


if __name__ == "__main__":
    mapping("median_house_value")
    mapping("median_income")
    mapping("housing_median_age")
    mapping("total_rooms")
    corr_matrix("median_house_value", "median_income")
    corr_matrix("median_house_value", "housing_median_age")
    corr_matrix("median_house_value", "total_rooms")
    corr_matrix("median_income", "housing_median_age")
    corr_matrix("median_income", "total_rooms")
    corr_matrix("housing_median_age", "total_rooms")
