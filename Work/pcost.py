# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(file_name):
    fn = file_name
    total = 0

    with open(fn, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            # print(record)
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                total = total + num_shares*price
            except ValueError:
                print(f'Row {rowno}: Could not parse: {row}')

    return total

if len(sys.argv) == 2:
    print(sys.argv)
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    

cost = portfolio_cost(filename)
print("Total Cost: ", cost)
