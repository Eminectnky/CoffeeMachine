import streamlit as st

class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.money = 0

    def check_resources(self, coffee):
        if self.resources["water"] < coffee.water:
            st.write("Sorry, there is not enough water.")
            return False
        if self.resources["milk"] < coffee.milk:
            st.write("Sorry, there is not enough milk.")
            return False
        if self.resources["coffee"] < coffee.coffee:
            st.write("Sorry, there is not enough coffee.")
            return False
        return True

    def make_coffee(self, coffee):
        self.resources["water"] -= coffee.water
        self.resources["milk"] -= coffee.milk
        self.resources["coffee"] -= coffee.coffee
        self.money += coffee.cost

        self.report()

    def report(self):
        st.write(f"Water: {self.resources['water']}ml")
        st.write(f"Milk: {self.resources['milk']}ml")
        st.write(f"Coffee: {self.resources['coffee']}g")
        st.write(f"Money: ${self.money:.2f}")

