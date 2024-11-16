import streamlit as st
from coffee_machine import CoffeeMachine
from coffee import espresso, latte, cappuccino
from money_manager import MoneyManager

coffee_machine = CoffeeMachine()
money_manager = MoneyManager()

if 'quarters' not in st.session_state:
    st.session_state.quarters = 0
if 'dimes' not in st.session_state:
    st.session_state.dimes = 0
if 'nickels' not in st.session_state:
    st.session_state.nickels = 0
if 'pennies' not in st.session_state:
    st.session_state.pennies = 0
if 'selected_coffee' not in st.session_state:
    st.session_state.selected_coffee = None

st.title("Coffee Machine")

coffee_choice = st.selectbox("Select coffee type:", ["espresso", "latte", "cappuccino", "show report"])

if coffee_choice != "show report" and coffee_choice != st.session_state.selected_coffee:
    st.session_state.quarters = 0
    st.session_state.dimes = 0
    st.session_state.nickels = 0
    st.session_state.pennies = 0

st.session_state.selected_coffee = coffee_choice

if coffee_choice == "show report":
    coffee_machine.report()
else:
    coffee_types = {"espresso": espresso, "latte": latte, "cappuccino": cappuccino}
    selected_coffee = coffee_types.get(coffee_choice)

    if coffee_machine.check_resources(selected_coffee):
        st.write(f"Money required for {selected_coffee.name}: ${selected_coffee.cost}")

        st.session_state.quarters = st.number_input("Number of quarters:", min_value=0, step=1, value=st.session_state.quarters)
        st.session_state.dimes = st.number_input("Number of dimes:", min_value=0, step=1, value=st.session_state.dimes)
        st.session_state.nickels = st.number_input("Number of nickels:", min_value=0, step=1, value=st.session_state.nickels)
        st.session_state.pennies = st.number_input("Number of pennies:", min_value=0, step=1, value=st.session_state.pennies)

        if st.button("Process money"):
            inserted_money = money_manager.process_coins(st.session_state.quarters, st.session_state.dimes, st.session_state.nickels, st.session_state.pennies)
            st.write(f"Total money added: ${inserted_money}")

            if money_manager.transaction_successful(inserted_money, selected_coffee.cost):
                coffee_machine.make_coffee(selected_coffee)

                change = inserted_money - selected_coffee.cost

