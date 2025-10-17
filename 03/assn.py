# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Assn-3
#
# **Goal**: Use Jupyter to reproduce the figures below including:
#
# * Colors
# * Labels
# * etc.

# %% [markdown]
# ___
#
# ### Figure 1
#
# Use `data-fig1.npy` for this figure.

# %%
# %matplotlib inline

import numpy as np
from matplotlib import pyplot as plt

# enter additional commands here to reproduce the figure below

# NOTE!
# - Entering commands and running the cell may cause the figure to disapper
# - If the figure disappears, use Assn-3.html as a reference

# %%

a = np.load("data-fig1.npy")
x = np.linspace(0, len(a) - 1, len(a))
plt.xlabel("Time")
plt.ylabel("value")
plt.plot(x, a, "o-", c="black")
plt.show()

# %% [markdown]
# ___
#
# ### Figure 2
#
# Use `data-fig2.npy` for this figure.

# %%
a = np.load("data-fig2.npy")
x = np.linspace(0, len(a[:, 0]) - 1, len(a[:, 0]))

plt.plot(x, a[:, 0], c="Red", label="Red")
plt.plot(x, a[:, 1], c="Green", label="Green")
plt.plot(x, a[:, 2], c="Blue", label="Blue")

plt.xlabel("X value")
plt.ylabel("Y value")
plt.legend()
plt.show()

# %% [markdown]
# ___
#
# ### Figure 3
#
# Use `data-fig3.npy` for this figure.
a = np.load("data-fig3.npy")
plt.scatter(a[:, 0], a[:, 1], c="blue", alpha=0.5, marker="o", s=200)
plt.xlabel("X value")
plt.ylabel("Y value")
plt.show()

print(a)

# %%

# %% [markdown]
# ___
#
# ### Figure 4
#
# Use `data-fig4.npy` for this figure.

# %%
a = np.load("data-fig4.npy")
print(a)
label = ["A", "B", "C", "D", "E"]
left = np.arange(len(label))
plt.bar(left, a, tick_label=label, color="gray")

# %% [markdown]
# ___
#
# ### Figure 5
#
# Use `data-fig5.npy` for this figure.
#
# *Hint*: Use 2D visualization and the "RdBu" colormap.

# %%

# %% [markdown]
# ___
#
# ### UNGRADED BONUS QUESTION
#
# (This question is an *optional*, *ungraded* bonus problem.)
#
# Use `data-fig-bonus-X.npy`, `data-fig-bonus-Y.npy` and `data-fig-bonus-Z.npy` for this figure.
#
# *Hint*: Search Matplotlib's online examples.

# %%
