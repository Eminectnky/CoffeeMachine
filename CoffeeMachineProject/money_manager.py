import streamlit as st

class MoneyManager:
    def __init__(self):
        self.total_money = 0

    def process_coins(self, quarters, dimes, nickels, pennies):
        self.total_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
        return round(self.total_money, 2)

    def transaction_successful(self, amount, cost):
        if amount < cost:
            st.write("Sorry, that's not enough money. Money refunded.")
            return False
        elif amount > cost:
            change = round(amount - cost, 2)
            st.write(f"Here is ${change} in change.")
        return True

    def reset(self):
        self.total_money = 0
