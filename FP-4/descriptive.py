# %% id="rXhdijH7"
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import Markdown, display  # ,HTML
from matplotlib import pyplot as plt
from scipy import stats

import parse_data


class Title:
    def __init__(self):
        self.num = 1

    def titledisplay(self, s: str, pref="Figure", center=False):
        ctag = "center" if center else "p"
        s = f'<{ctag}><span style="font-size: 1.2em;"><b>{pref} {self.num}</b>: {s}</span></{ctag}>'
        if pref == "Figure":
            s = f"{s}<br><br>"
        else:
            s = f"<br><br>{s}"
        display(Markdown(s))
        self.num += 1


# %% id="J_J-bpow"

# proccess data
df = parse_data.df
df.describe()
df = df.dropna()

# remove outliers
df = df[df["median_house_value"] < 500001]
df = df[df["housing_median_age"] < 52]

df = df.select_dtypes(include="number")
columns = df.columns.tolist()
thresholds = df[columns].quantile(0.99)

df = df[(df[columns] < thresholds).all(axis=1)]


# %% id="Rh4ZJCfN"
def central(x):
    mean = np.mean(x)
    median = np.median(x)
    mode = stats.mode(x).mode
    return mean, median, mode


def dispersion(x):
    std = np.std(x)
    min_val = np.min(x)
    max_val = np.max(x)
    rng = max_val - min_val
    q25 = np.percentile(x, 25)
    q75 = np.percentile(x, 75)
    iqr = q75 - q25
    return std, min_val, max_val, rng, q25, q75, iqr


# %% id="qUv1uv_K"
title = Title()


def display_central_tendency_table():
    title.titledisplay(
        "Central tendency summary statistics.", pref="Table", center=False
    )
    df_central = df.apply(lambda x: central(x), axis=0)
    # round_dict = {'quality': 3, 'acidity': 3, 'density': 6, 'sugar': 3}
    df_central = df_central.round(1)
    row_labels = "mean", "median", "mode"
    df_central.index = row_labels
    display(df_central)


def display_dispersion_table():
    title.titledisplay("Dispersion summary statistics.", pref="Table", center=False)

    df_disp = df.apply(lambda x: dispersion(x), axis=0)
    df_disp.index = ["std", "min", "max", "range", "q25", "q75", "iqr"]
    display(df_disp)


# %% id="wZfNKr6l"
def plot_housing_data(ax, name: str) -> None:
    sc = ax.scatter(
        df["longitude"],
        df["latitude"],
        c=df[name],
        cmap="viridis",
        s=5,
        alpha=0.2,
    )
    plt.colorbar(sc, ax=ax, label=name)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")


def histogram(
    ax,
    name: str,
    bins: int,
) -> None:
    x = df[name]
    sns.histplot(x, bins=bins, ax=ax)
    ax.set_xlabel(name)
    ax.set_ylabel("Count")
    ax.set_title(f"Histogram of {name}")


def plot_regression_line(ax, name1: str, name2: str) -> None:
    x = df[name1]
    y = df[name2]
    m, b = np.polyfit(x, y, 1)
    x_min, x_max = min(x), max(x)
    y_min, y_max = m * x_min + b, m * x_max + b
    ax.plot([x_min, x_max], [y_min, y_max], color="black", linestyle="--")
    ax.text(
        x_max * 3 / 4,
        y_max,
        f"r = {m:.2g}",
        color="black",
        bbox=dict(color="0.8", alpha=0.7),
        alpha=0.7,
    )


def correlation_map(ax, name1: str, name2: str) -> None:
    x = df[name1]
    y = df[name2]
    corr = np.corrcoef(x, y)[0, 1]
    ax.scatter(x, y, s=5, alpha=0.2)
    plot_regression_line(ax, name1, name2)
    ax.set_xlabel(name1)
    ax.set_ylabel(name2)
    ax.set_title(f"Correlation: {corr:.2g}")
    ax.grid()


# %% id="RtH-bMPA"
def main():
    display_central_tendency_table()
    display_dispersion_table()

    # drop cols for graph
    drop_cols = ["median_house_value", "longitude", "latitude"]
    df_dropped = df.drop(columns=drop_cols)

    column_list = df_dropped.columns.tolist()

    # plot maps
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    axs = axs.flatten()
    for i, name in enumerate(column_list):
        plot_housing_data(axs[i], name)
    plt.tight_layout()
    plt.show()

    # plot correlation
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    axs = axs.flatten()
    for i, name in enumerate(column_list):
        correlation_map(axs[i], name, "median_house_value")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
