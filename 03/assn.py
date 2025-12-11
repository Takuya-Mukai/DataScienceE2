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
%matplotlib inline

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
x = np.arange(len(a[:, 0]))

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

# %%
a = np.load("data-fig3.npy")
plt.scatter(a[:, 0], a[:, 1], c="blue", alpha=0.3, marker="o", s=200)
plt.xlabel("X value")
plt.ylabel("Y value")
plt.show()


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
a = np.load("data-fig5.npy")
map = plt.pcolor(a, cmap="RdBu", vmin = -1.0, vmax = 1.0)
plt.colorbar(map)
plt.show()

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
x = np.load("data-fig-bonus-X.npy")
y = np.load("data-fig-bonus-Y.npy")
z = np.load("data-fig-bonus-Z.npy")

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.contourf(x, y, z, levels=20, cmap='RdBu_r')
