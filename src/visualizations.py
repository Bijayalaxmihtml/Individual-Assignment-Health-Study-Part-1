"""Reusable plots for the health study."""
import matplotlib.pyplot as plt

def plot_histogram(data, column, ax=None):
    """Plot a histogram for one numeric variable."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 4))
    ax.hist(data[column].dropna(), bins=20, edgecolor="black")
    ax.set(title=f"Distribution of {column}", xlabel=column, ylabel="Frequency")
    return ax

def plot_boxplot(data, group_column, value_column, ax=None):
    """Plot a boxplot of a numeric variable across groups."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 4))
    data.boxplot(column=value_column, by=group_column, ax=ax)
    ax.set(title=f"{value_column} by {group_column}", xlabel=group_column, ylabel=value_column)
    return ax

def plot_scatter(data, x_column, y_column, ax=None):
    """Plot the relationship between two numeric variables."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(data[x_column], data[y_column], alpha=0.6)
    ax.set(title=f"{y_column} versus {x_column}", xlabel=x_column, ylabel=y_column)
    return ax
