class Category:
    
    def __init__(self, name):
        self.name = name
        self.funds = 0
        self.ledger: list = []

    def __str__(self):
        title = self.name.capitalize().center(30, "*") + "\n"
        items = ""
        total = 0
        
        for i in self.ledger:
            items += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + "\n"
            total += i["amount"]
        return title + items + "Total: " + str(total)

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds = self.funds + amount

    def withdraw(self, amount: float, description: str = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        self.funds = self.funds - amount
        return True

    def get_balance(self):
        return self.funds

    def transfer(self, amount: float, budget_category: object):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if self.funds >= amount:
            return True
        return False

    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)

    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10

    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key = len)

    for x in range(len(maxi)):
        nameStr = "     "
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "

        if(x != len(maxi) - 1):
            nameStr += "\n"

        x_axis += nameStr
    
    res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
    return res

b1 = Category("food")
b1.deposit(1000, "initial deposit")

print("ledger = ", b1.ledger)
print("balance = ", b1.get_balance(), "\n")

b1.deposit(2000, "more funds123456789012345")
print("ledger = ", b1.ledger)
print("balance = ", b1.get_balance(), "\n")

b1.withdraw(2000, "fuel")
print("ledger = ", b1.ledger)
print("balance = ", b1.get_balance(), "\n")

b1.withdraw(500, "fuel")
print("ledger = ", b1.ledger)
print("balance = ", b1.get_balance(), "\n")

b2 = Category("wear")
b2.deposit(3500)

print("ledger2 = ", b2.ledger)
print("balance2 = ", b2.get_balance(), "\n")

b2.transfer(500, b1)
print("ledger2 = ", b2.ledger)
print("balance2 = ", b2.get_balance(), "\n")
print("ledger = ", b1.ledger)
print("balance = ", b1.get_balance(), "\n")

#b1.print_instance()
print(b1)