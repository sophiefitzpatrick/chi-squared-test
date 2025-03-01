import csv
import json
import os
import pdb
from datetime import datetime
from scipy.stats import chi2


def convert_csv_to_json():
    # read from the input csv
    with open('input.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # return the csv data as json data
    return data

def calculate_expected_value(row_total, column_total, total_observations):
    return (row_total * column_total) / total_observations

def calculate_chi_square_value(observed_cell_value, expected_cell_value):
    # (O-E)2/E
    return ((observed_cell_value - expected_cell_value) ** 2) / expected_cell_value

def look_up_critical_value(df, significance_level):
    significance_level_index = {
        'df': 0,
        '0.995': 1,
        '0.975': 2,
        '0.2': 3,
        '0.1': 4,
        '0.05': 5,
        '0.025': 6,
        '0.02': 7,
        '0.01': 8,
        '0.005': 9,
        '0.002': 10,
        '0.001': 11
    }
    significance_index = significance_level_index.get(str(significance_level))

    with open('chi_squared_distribution.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            if line[0] == 'df':
                # if this value is a table header continue the loop
                continue

            if int(line[0]) == df:
                critical_value = line[significance_index]

    return critical_value

def calculate_chi_square(significance_level=0.05):
    json_table = convert_csv_to_json()
    column_totals = json_table[-1]  # get row of totals
    json_table.pop()  # remove row of totals from data

    total_observations = int(column_totals.get('total'))

    cells = []
    for row in json_table:
        cell_data = {
            "row_name": row.get(''),
            "row_total": int(row.get('total')),
            "column_name": None,
            'column_total': None,
            "expected_cell_value": None,
            "observed_cell_value": None,
            "chi_squared_value": None
        }

        row.pop('')
        row.pop('total')

        for column in row:
            cell_data = cell_data.copy()
            cell_data['column_name'] = column
            cell_data['observed_cell_value'] = int(row.get(column))
            cells.append(cell_data)

    chi_squared_values = []
    for cell in cells:
        for key, _ in cell.items():
            if key == "column_total":
                column_name = cell.get('column_name')
                column_total = int(column_totals.get(column_name))
            elif key == "expected_cell_value":
                row_total = cell.get('row_total')
                expected_cell_value = calculate_expected_value(row_total=row_total, column_total=column_total, total_observations=total_observations)
            elif key == "chi_squared_value":
                observed_cell_value = cell.get("observed_cell_value")
                chi_squared_value = calculate_chi_square_value(observed_cell_value, expected_cell_value)

        cell['column_total'] = column_total
        cell['expected_cell_value'] = round(expected_cell_value, 2)
        cell['chi_squared_value'] = round(chi_squared_value, 2)
        chi_squared_values.append(round(chi_squared_value, 2))

    chi_squared_stat = round(sum(chi_squared_values), 2)  # sums up all chi_squared_values
    df = len(cells)  # degree of freedom (number of rows * columns)
    critical_value = float(look_up_critical_value(df, significance_level))
    hypotheses = ["null: there is no relationship between x and y", "alt: there is a relationship between x and y"]
    p_value = round(1 - chi2.cdf(chi_squared_stat, df), 2)

    returned_data = {
        'chi_squared_statistic': chi_squared_stat,
        'df': df,
        'critical_value': critical_value,
        'p-value': p_value,
        'hypotheses': hypotheses,
        'cell_data': cells,
    }

    current_datetime = datetime.now()
    file_name = current_datetime.strftime('%m.%d.%Y_%H:%M:%S')
    file_name = "%s.json" % file_name

    with open(file_name, 'w') as f:
        json.dump(returned_data, f)


calculate_chi_square()
