"""Small tests for the reusable analysis functions."""
import pandas as pd
from src.data_processing import disease_prevalence
from src.statistics_analysis import mean_confidence_interval, compare_smokers

def sample_data():
    return pd.DataFrame({"disease":[1,0,0,1], "smoker":["yes","yes","no","no"],
                         "systolic_bp":[150,160,130,140]})

def test_disease_prevalence():
    result = disease_prevalence(sample_data())
    assert result["cases"] == 2 and result["total"] == 4
    assert result["percentage"] == 50.0

def test_mean_confidence_interval_contains_sample_mean():
    mean, lower, upper = mean_confidence_interval([1,2,3,4,5])
    assert lower <= mean <= upper

def test_smoker_comparison_returns_valid_p_value():
    result = compare_smokers(sample_data())
    assert 0 <= result["p_value_one_sided"] <= 1
