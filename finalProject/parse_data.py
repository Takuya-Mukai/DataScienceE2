# %%
import pandas as pd

df0 = pd.read_csv("./housing.csv")
df0.head()

# %%

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

df = df.rename(
    columns={
        "total_rooms": "rooms",
        "total_bedrooms": "bedrooms",
    }
)
