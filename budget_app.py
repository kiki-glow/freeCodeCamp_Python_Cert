class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, other_category):
        if self.withdraw(amount, f"Transfer to {other_category.name}"):
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ''
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total spent per category
    spent_amounts = [sum(-entry['amount'] for entry in cat.ledger if entry['amount'] < 0) for cat in categories]
    total_spent = sum(spent_amounts)
    
    # Percentage spent rounded down to nearest 10
    percentages = [int((amount / total_spent) * 100) // 10 * 10 for amount in spent_amounts]
    
    chart = "Percentage spent by category\n"
    
    # Build chart rows from 100 to 0
    for i in range(100, -1, -10):
        row = str(i).rjust(3) + "|"
        for p in percentages:
            row += " o " if p >= i else "   "
        chart += row + " \n"
    
    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Vertical category labels
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     "  # 5 spaces to align with chart
        for cat in categories:
            if i < len(cat.name):
                row += cat.name[i] + "  "  # character + 2 spaces
            else:
                row += "   "  # 3 spaces if no character
        if i < max_len - 1:
            chart += row + "\n"
        else:
            chart += row.rstrip() + "  "
    
    return chart
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(150.25, "groceries")
food.withdraw(50.75, "restaurant")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(200, "maintenance")

print(create_spend_chart([food, clothing, auto]))
