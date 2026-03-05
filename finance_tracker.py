import pandas as pd

file = "finance.csv"

try:
    data = pd.read_csv(file)
except:
    data = pd.DataFrame(columns=["type","category","amount"])

while True:

    print("\n1 Add Income")
    print("2 Add Expense")
    print("3 Show Summary")
    print("4 Exit")

    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Income amount: "))
        row = {"type":"income","category":"salary","amount":amount}
        data.loc[len(data)] = row

    if choice == "2":
        category = input("Category: ")
        amount = float(input("Expense amount: "))
        row = {"type":"expense","category":category,"amount":amount}
        data.loc[len(data)] = row

    if choice == "3":
        income = data[data["type"]=="income"]["amount"].sum()
        expense = data[data["type"]=="expense"]["amount"].sum()

        print("Income:", income)
        print("Expenses:", expense)
        print("Balance:", income-expense)

    if choice == "4":
        data.to_csv(file,index=False)
        break