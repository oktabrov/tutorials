import requests
import json
url = 'https://open.er-api.com/v6/latest/USD'
print("Fetching exchange rates...")
data = requests.get(url = url).json()
print("Processing expenses.csv...")
with open('expenses.csv', 'r') as f:
    my_d = {}
    amounts, currencys = [], []
    for i in f:
        amount, currency = i.strip().split(',')
        if (amount.count('.') == 1 and amount.replace('.', '').isdigit()) or amount.isdigit():
            amounts.append(float(amount))
            currencys.append(currency)
grand_total = 0
print("Report written to expense_report.txt")
in_usd = []
for i in range(len(amounts)):
    price = data['rates'][currencys[i]]
    amount_in_usd = amounts[i]/price
    in_usd.append(amount_in_usd)
    grand_total += amount_in_usd
with open('expense_report.txt', 'w') as f:
    s = ''
    for i in range(len(amounts)):
        s += f"Item: Original: {amounts[i]:.2f} {currencys[i]} | USD: ${in_usd[i]:.2f}\n"
    s += '--------------------------------------------------\n'
    s += f"GRAND TOTAL: ${grand_total:.2f}"
    f.write(s)
print(f"Total Expenses: ${grand_total:.2f}")