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
# # Assignment 02:  Python basics
#
# The purpose of this assignment is learn the fundamentals of Python programming, including:
#
# 1. Basic math
# 1. Variables
# 1. Lists, tuples and arrays
# 1. Packages: `math` and `numpy`
# 1. Functions
#

# %% [markdown]
# ___
#
# ### Example problem
#
# Q. Use Python to calculate and print the result of:
#
# <br>
#
# <center>$\begin{eqnarray*}
#     4 \times 5
# \end{eqnarray*}$</center>
#
# ### Answer to example problem:

# %%
print( 4 * 5 )

# %% [markdown]
# ___
#
# # (1)  Basic math

# %% [markdown]
# Q. Use Python to calculate and print the result of:
#
# <br>
#
# <center>$\begin{eqnarray*}
#     (3 + 1) \times 2
# \end{eqnarray*}$</center>

# %%
print( (3 + 1) * 2 )

# %% [markdown]
# Q. Use Python to calculate and print the result of:
#
# <br>
#
# <center>$\begin{eqnarray*}
#     (4 + 6) ^ 2
# \end{eqnarray*}$</center>

# %%
print( (4 + 6) ^ 2)

# %% [markdown]
# Q. Use Python to calculate and print the result of:
#
# <br>
#
# <center>$\begin{eqnarray*}
#     \frac{ (3 + 1) \times 2 }{ (4 + 6) ^ 2 }
# \end{eqnarray*}$</center>

# %%
print((3+1)*2/(4+6)**2)
# %% [markdown]
# ___
#
# # (2)  Variables

# %% [markdown]
# Q. Use Python to calculate then print the value of `y`.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& 5 \\
#     y &=& (x^2 + 1)
# \end{eqnarray*}$</center>

# %%
x = 5
y = (x**2 + 1)
print(y)



# %% [markdown]
# Q. Use Python to calculate then print the value of `y`.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     a &=& 5 \\
#     b &=& 10 \\
#     c &=& 20 \\
#     x &=& -1 \\
#     y &=& (ax^2 + bx + c)
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use Python to calculate then print the value of `y`.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x_0 &=& 50 \\
#     x_1 &=& 3 x_0 - 50\\
#     y &=& \left(\frac{x_0}{x_1}\right)^2
# \end{eqnarray*}$</center>

# %% [markdown]
# ___
#
# # (3) Lists and tuples

# %% [markdown]
# Q. Use Python to construct `x` as a **list**, then print its **second** value.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}10 & 8 & 20 & 6 & 30\end{bmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use Python to construct `x` as a **tuple**, then print its **last** value.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{pmatrix}5 & 2 & 1\end{pmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use Python to construct `x` as a **list** of **tuples**, then print the **last** tuple.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}\begin{pmatrix}5 & 2 & 1\end{pmatrix}, \begin{pmatrix}1 & 3 & 3\end{pmatrix}, \begin{pmatrix}0 & -1 & -2\end{pmatrix}\end{bmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use Python to create an empty list `x`, then use three `append` commands to create and print the following list. 
#
# **NOTE!**: your Python code should have **five** commands including three `append` commands and one `print` command.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}5 & \begin{pmatrix}1 & 2\end{pmatrix}  & \begin{bmatrix}4 & 5 & 6\end{bmatrix}\end{bmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# ___
#
# # (4) Packages: math and numpy
#
# ### `math`

# %% [markdown]
# Q. Use the `math` package to calculate `x`. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \sin(\pi/2) - \cos(\pi) 
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use the `math` package to calculate `y`. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x_0 &=& 3\\
#     x_1 &=& 4\\
#     y &=& \sqrt{x_0^2 + x_1^2}
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use the `math` package to calculate `x`. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& e ^ {\log(10) }
# \end{eqnarray*}$</center>

# %% [markdown]
# ### `numpy`

# %% [markdown]
# Q.  Use the `numpy` package to construct the following 1D array. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}5 & 2 & 1\end{bmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# Q.  Use the `numpy` package to construct the following 2D array. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}5 & 2 & 1\\ 1 & 3 & 3\\ 0 & -1 & -2\end{bmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use the `numpy` package to compute `x`. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}5\\2\\1\end{bmatrix} + 1
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Use the `numpy` package to compute `x`. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     x &=& \begin{bmatrix}5\\2\\1\end{bmatrix} + \begin{bmatrix}3\\-4\\8\end{bmatrix}
# \end{eqnarray*}$</center>

# %% [markdown]
# ___
#
# # (5) Functions

# %% [markdown]
# Q. Create a function called `myfunction` that calculates $f(x)$. Use this function to calculate $f(x)$ for $x=5$. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     f(x) &=& 2(x - 1) + 5
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Create a function called `two_argument_function` that calculates $f(a, b)$. Use this function to calculate $f(a, b)$ for $a=3$ and $b=2$. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     f(a, b) &=& b^a + 1
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Create a function called `add_vectors` that calculates $f(\boldsymbol{x}_0, \boldsymbol{x}_1)$. Use this function to calculate $f(\boldsymbol{x}_0, \boldsymbol{x}_1)$ for $\boldsymbol{x}_0=\begin{bmatrix}5\\2\\1\end{bmatrix}$ and $\boldsymbol{x}_1=\begin{bmatrix}1\\2\\10\end{bmatrix}$. Print the result.
#
# <br>
#
# <center>$\begin{eqnarray*}
#     f(\boldsymbol{x}_0, \boldsymbol{x}_1) &=&  \boldsymbol{x}_0 + \boldsymbol{x}_1
# \end{eqnarray*}$</center>

# %% [markdown]
# Q. Create a Python function that represent the following mathematical function:
#
# <br> 
#
# <center>$\begin{eqnarray*}
#     f(\boldsymbol{a}, b, c) &=& b\boldsymbol{a} + \begin{bmatrix}0\\c\\0\end{bmatrix}
# \end{eqnarray*}$</center>
#
# <br> 
#
# Note that $\boldsymbol{a}$ is a vector, and that $b$ and $c$ are scalars.
#
# <br>
#
# Use the function you created to calculate $f(\boldsymbol{a},b,c)$ for: $\boldsymbol{a} = \begin{bmatrix}1\\0\\2\end{bmatrix}$, $b=5$ and $c$=10.
#
# Print your solution.
#
# <br> 
#
#
