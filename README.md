# Chi Squared Test

A chi-squared test is a statistical test used to determine if there is a significant association between two categorical variables or if a sample data matches an expected distribution.

<img width="202" alt="image" src="https://github.com/user-attachments/assets/accb8ab1-f981-40fb-90e7-0db8c179f8b5" />

The script pulls the data from a csv saved in the root of this repo. I've added an example `input.csv` but do replace this with the data you want to perform the Chi Squared Test on.

<img width="524" alt="image" src="https://github.com/user-attachments/assets/a53d6131-49d4-4630-8f0d-638fa312a6e8" />



Here is the exported csv:
```
,responded,not_responded,total
treated,35,15,50
not_treated,26,29,55
total,61,44,105
```

The script returns a .json in the following format (with examples):

```
{'chi_square_statistic': 5.56, 'df': 4, 'critical_value': 9.488, 'p-value': 0.23, 'hypotheses': ['null: there is no relationship between x and y', 'alt: there is a relationship between x and y'], 'cell_data': [{'row_name': 'treated', 'row_total': 50, 'column_name': 'no_responded_to_treatment', 'column_total': 61, 'expected_cell_value': 29.05, 'observed_cell_value': 35, 'chi_squared_value': 1.22}, {'row_name': 'treated', 'row_total': 50, 'column_name': 'no_did_not_respond_to_treatment', 'column_total': 44, 'expected_cell_value': 20.95, 'observed_cell_value': 15, 'chi_squared_value': 1.69}, {'row_name': 'not_treated', 'row_total': 55, 'column_name': 'no_responded_to_treatment', 'column_total': 61, 'expected_cell_value': 31.95, 'observed_cell_value': 26, 'chi_squared_value': 1.11}, {'row_name': 'not_treated', 'row_total': 55, 'column_name': 'no_did_not_respond_to_treatment', 'column_total': 44, 'expected_cell_value': 23.05, 'observed_cell_value': 29, 'chi_squared_value': 1.54}]}
```

    
# Considerations:
The significance level is set in `run()`, but this can be changed before running.

Save a csv of the input table data as `input.csv` in the root of this repo.

# How to run:
1. Clone this repo `git@github.com:sophiefitzpatrick/chi-squared-test.git`
2. Run `pip install -r requirements.txt`
3. `python run.py`
