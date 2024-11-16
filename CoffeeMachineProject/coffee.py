class Coffee:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

# Types of Coffee
espresso = Coffee("espresso", water=50, milk=0, coffee=18, cost=1.5)
latte = Coffee("latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = Coffee("cappuccino", water=250, milk=100, coffee=24, cost=3.0)
