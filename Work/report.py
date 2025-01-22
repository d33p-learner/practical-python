# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    
    portfolio = []

    with open(filename, 'rt') as file:
        next(file)
        rows = csv.reader(file)
        for row in rows:
            portfolio.append({"name":row[0], "shares": int(row[1]),"price": float(row[2])})
    
    return portfolio

def read_prices(filename):
    prices = dict()
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        try:
            for row in rows:
                prices[row[0]] = float(row[1])
        except IndexError:
            print("Empty list", row)
    
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)

def make_report(portfolio, prices):
    summary = []
    for row in portfolio:
        summary.append((row['name'], row['shares'],'$' + str(prices[row['name']]), prices[row['name']] - row['price']))

    return summary

report = make_report(portfolio, prices)

header = ('Name', 'Shares', 'Price', 'Change')
print("%10s %10s %10s %10s" % header)
print(('-' * 10 + ' ') * len(header))
for r in report:
    print("%10s %10d %10s %10.2f" % r)
    

