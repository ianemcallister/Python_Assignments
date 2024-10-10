# Define dependencies
import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import ttest_ind
import statsmodels.api as sm
import warnings

# Load dataset
dataset = pd.read_csv('dataset_1.csv')

# Data analysis
num_rows, num_cols = dataset.shape
print(f"Number of rows: {num_rows}")
print(f"Number of cols: {num_cols}")

# Descriptitve statistics
summary_stats = dataset.describe()
print('Descriptive Statistics:')
print(summary_stats)

# Probability calculation
if len(dataset) >= 8:
    prob = norm.cdf(2.5, loc=dataset['column_1'].mean(), scale=dataset['column_1'].std())
    print(f"Probability: {prob}")
else:
    print('Insufficient data for probability calculation.')


# Hypothesis testing
warnings.filterwarnings("ignore") # ifnore the warning for the small sample size
group_a_data = dataset[dataset['group'] == 'A']['column_2']
group_b_data = dataset[dataset['group'] == 'B']['column_2']
if len(group_a_data) >= 8 and len(group_b_data) >= 8:
    t_stat, p_value = ttest_ind(group_a_data, group_b_data)
    print(f"T-statistics: {t_stat}")
    print(f"P value: {p_value}")
else:
    print("Insufficient data for hypothesis testing.")

# Regression analysis
if len(dataset) >= 8:
    X = dataset[['column_1', 'column_2', 'feature_1', 'feature_2']]
    y = dataset['target']
    x = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())
else:
    print('Insufficent data for regression analysis.')