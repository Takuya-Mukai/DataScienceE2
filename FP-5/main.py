# %% [markdown]
# basic stats and null check
# values seem ok, but some columns have max repeated a lot → likely outliers

# %% id="OhBi2xQkDcT3"
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

import parse_data

df = parse_data.df

print(df.describe())
print(df.isnull().sum())
print(df.shape)

# %% id="mwiKrn-tpq0k"
# count how many times each column hits max → checking for possible outliers
columns = df.columns.tolist()
check_max = {}

for column in columns:
    count_of_max = (df[column] == df[column].max()).sum()
    check_max[column] = count_of_max

for i in check_max:
    print(f"{i}: {check_max[i]}")

# %% [markdown]
# several columns have repeated max → treat as outliers
# housing_median_age, median_income, median_house_value

# %% id="S1H8aXL52NT0"
# remove outliers (just drop rows equal to max)
outlier_columns = ["housing_median_age", "median_income", "median_house_value"]
for i in outlier_columns:
    df = df[df[i] < df[i].max()]

# %% id="2V3-MMpDEIpH"
# bedrooms null vs not-null → check price difference
price_null = df[df["bedrooms"].isnull()]["median_house_value"]
price_not_null = df[df["bedrooms"].notnull()]["median_house_value"]

u_statistic, p_value = stats.mannwhitneyu(
    price_null, price_not_null, alternative="two-sided"
)

print(f"Mann-Whitney U Test P-value: {p_value:.5f}")
print(f"median of null: {price_null.median():.2f}")
print(f"median of non-null: {price_not_null.median():.2f}")

# %% [markdown]
# p>0.05 → no strong difference between null and not-null groups
# so dropping rows with null bedrooms likely ok.

# %% id="ljTGQBNazO32"
df = df.dropna()

# %% [markdown]
# check log-normality using Q-Q plots


# %% id="vHvllZaJMDkP"
def qq_plot(column):
    data = np.log(df[column])
    sm.qqplot(data, line="s")
    plt.title(column)
    plt.show()


qq_list = ["median_house_value", "housing_median_age", "population", "median_income"]
for i in qq_list:
    qq_plot(i)

# %% [markdown]
# From Q-Q plot: median_house_value and median_income look log-normal
# (almost linear between theoretical quantiles −2 to +2)

# %% id="B0XKQ547Wx-p"
# some engineered features
df["avg_rooms_per_hh"] = df["rooms"] / df["households"]
df["avg_people_per_hh"] = df["population"] / df["households"]
df["median_income_log"] = np.log(df["median_income"])
df["median_house_value_log"] = np.log(df["median_house_value"])

# %% id="TwV4giMJ_Qpn"
# compare correlations by income groups (top 25% vs others)
q3_income = df["median_income"].quantile(0.75)

df_high_income = df[df["median_income"] >= q3_income]
df_other_income = df[df["median_income"] < q3_income]

print(
    f"high-income N={len(df_high_income)}, low&middle-income N={len(df_other_income)}"
)


# %% id="QJOQGm6dvGZh"
def calculate_and_compare_corr(df1, df2, label1, label2):
    results = {}
    for feature in ["median_income_log", "avg_rooms_per_hh", "avg_people_per_hh"]:
        corr1, p1 = stats.pearsonr(df1["median_house_value_log"], df1[feature])
        corr2, p2 = stats.pearsonr(df2["median_house_value_log"], df2[feature])

        results[feature] = {
            f"{label1} Corr": corr1,
            f"{label1} P": p1,
            f"{label2} Corr": corr2,
            f"{label2} P": p2,
        }
    return pd.DataFrame(results).T


corr_results = calculate_and_compare_corr(
    df_high_income, df_other_income, "High Income", "Other Income"
)

print("\ncorrelation of income")
print(corr_results)

# %% [markdown]
# ## correlation results:
#
# + median_income_log: strongest correlation with house value in both groups
#   (P extremely small: not random)
#   + Higher median income areas tend to have higher house values, suggesting that
#     neighborhood wealth strongly drives property prices. It also implies that
#     local economic conditions may matter more than individual household size or rooms.

# + avg_rooms_per_hh: almost no relation in high income, but negative in other group
#   (may reflect resource dilution / housing quality)
#   + In lower/middle-income areas, more rooms per household might indicate
#     larger, older, or lower-quality housing where income per person is diluted.
#     High-income households may have uniformly large, high-quality homes, so the
#     number of rooms doesn't differentiate house values much.

# + avg_people_per_hh: weak negative in both groups
#   (larger households slightly lower house value)
#   + Larger households may put pressure on financial resources, leading to lower
#     property values per capita. Alternatively, densely populated households
#     could correlate with smaller or less desirable homes.

# p-values small in most → correlations unlikely random and statistically reliable
