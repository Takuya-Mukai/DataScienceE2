# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
#
# ## Predicting Term Deposit Subscriptions: An Analysis of Bank Marketing Data
#
# * **Name**:  Takuya Mukai
# * **Student number**:  0500345373
#
# ### Purpose:
#
# - The purpose of this Final Project is to determine the factors that contribute to a client subscribing to a term deposit.
# - The key **dependent variable** (DV) is `y`, a binary "yes" or "no" indicating if the client subscribed.
# - Key **independent variables** (IVs) include:
#     - `longitude`
#     - `latitude`
#     - `housing_median_age`
#     - `total_rooms`
#     - `total_bedrooms`
#     - `population`
#     - `households`
#     - `median_income`
#     - `median_house_value`
#     - `ocean_proximity`
# - This dataset contains 20640 cases. Each client has values for all IVs as well as the DV.

# %% [markdown]
#
# ### Dataset source:
#
# The data come from the [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices) dataset, originally based on data from the 1990 California census.
#
# The data are available for download [here](https://www.kaggle.com/datasets/camnugent/california-housing-prices).
#
# This dataset was initially featured in the following paper: Pace & Barry (1997).
#
# #### References:
#
# Pace, R. Kelley, and Ronald Barry (1997). "Sparse spatial autoregressions." Statistics & Probability Letters 33.3: 291-297.
#
# doi: 10.1016/S0167-7152(96)00140-X
