
"""Descriptive and inferential statistical functions."""

import pandas as pd
from scipy import stats


NUMERIC_COLUMNS = [
    "age",
    "weight",
    "height",
    "systolic_bp",
    "cholesterol"
]


def descriptive_statistics(data, columns=None):
    """Return count, mean, standard deviation, quartiles and range."""
    selected_columns = columns or NUMERIC_COLUMNS
    return data[selected_columns].describe().T


def mean_confidence_interval(values, confidence=0.95):
    """Calculate a two-sided t confidence interval for a population mean."""
    values = pd.Series(values).dropna().astype(float)
    n = len(values)

    if n < 2:
        raise ValueError("At least two valid observations are required.")

    if not 0 < confidence < 1:
        raise ValueError("Confidence must be between 0 and 1.")

    mean = values.mean()

    margin = (
        stats.t.ppf((1 + confidence) / 2, n - 1)
        * stats.sem(values)
    )

    return mean, mean - margin, mean + margin


def compare_smokers(data):
    """Welch t-test for the one-sided question: smokers have higher mean BP."""

    flag = data["smoker"].astype(str).str.lower()

    smokers = data.loc[
        flag.isin(["yes", "1", "true"]),
        "systolic_bp"
    ].dropna()

    non_smokers = data.loc[
        flag.isin(["no", "0", "false"]),
        "systolic_bp"
    ].dropna()

    if len(smokers) < 2 or len(non_smokers) < 2:
        raise ValueError(
            "At least two valid observations are required in each group."
        )

    result = stats.ttest_ind(
        smokers,
        non_smokers,
        equal_var=False,
        alternative="greater"
    )

    return {
        "smoker_n": len(smokers),
        "non_smoker_n": len(non_smokers),
        "smoker_mean": float(smokers.mean()),
        "non_smoker_mean": float(non_smokers.mean()),
        "t_statistic": float(result.statistic),
        "p_value_one_sided": float(result.pvalue)
    }
