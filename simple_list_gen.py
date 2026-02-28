stocks = [
    ('MSFT', 3, 450), # Company name, quantity, price
    ('AAPL', 2, 190),
    ('TXN', 6, 150)
]

values = []
for i in range(len(stocks)):
    curr_holding = stocks[i]
    values.append(curr_holding[1] * curr_holding[2])
total = sum(values)
print(f'total is {total}')

holdings = sum([s[1] * s[2] for s in stocks]) #using generators
print(f'holdings is {holdings}')

