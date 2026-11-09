rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return rates[self.currency] * self.amount

    def __add__(self, other):
        if self.currency != other.currency:
            return Money(self.convert_to_kgs() + other.convert_to_kgs(), "KGS")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            return Money(self.convert_to_kgs() - other.convert_to_kgs(), "KGS")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)

    def __truediv__(self, other):
        return Money(self.amount / other, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
result = money1 + money2
print(result)
