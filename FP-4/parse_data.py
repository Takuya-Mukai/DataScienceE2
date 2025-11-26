# %% id="7DYALWa-"
import pandas as pd

df0 = pd.read_csv("./housing.csv")

# %% id="Kdz8cEyz"

df = df0[
    [
        "median_house_value",
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
    ]
]

# %% id="3Jn1-UhE"
df = df.rename(
    columns={
        "total_rooms": "rooms",
        "total_bedrooms": "bedrooms",
    }
)


def main():
    df.describe()


# %% id="Tdr4vwT7"
if __name__ == "__main__":
    main()
