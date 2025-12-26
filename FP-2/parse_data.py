# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # parse_data.ipynb
#
# This notebook parses the data files used for the FP-2 assignment. 
#
# <br>
# <br>
#
# First let's read the attached data file:

# %%
import pandas as pd
df0 = pd.read_csv('./housing.csv')
df0.head()

# %% [markdown]
# <br>
# <br>
#
# The dependent and independent variables variables (DVs and IVs) that we are interested in are:
#
# **DVs**:
# - House value ("median_house_value" column in the CSV file)
#
# **IVs**:
# - Longitude ("longitude" column in the CSV file)
# - Latitude ("latitude" column in the CSV file)
# - Housing median age ("housing_median_age" column in the CSV file)
# - Total rooms ("total_rooms" column in the CSV file)
# - Total bedrooms ("total_bedrooms" column in the CSV file)
# - Population ("population" column in the CSV file)
# - Households ("households" column in the CSV file)
# - Median income ("median_income" column in the CSV file)
#
#
# <br>
# <br>
#
# Let's extract the relevant columns:

# %%

df = df0[[
    'median_house_value',
    'longitude',
    'latitude',
    'housing_median_age',
    'total_rooms',
    'total_bedrooms',
    'population',
    'households',
    'median_income',
]]

df.describe()


# %% [markdown]
# <br>
# <br>
#
# Next let's use the `rename` function to give the columns simpler variable names:

# %%
df = df.rename(columns={
    'total_rooms':'rooms',
    'total_bedrooms':'bedrooms',
})

df.describe()
