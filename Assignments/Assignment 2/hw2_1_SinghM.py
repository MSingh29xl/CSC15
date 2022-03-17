# ***************
# File: hw2_1_SinghM.py
# Program Description: Calculates net profit of a bitcoin miner based on iputted revenue, electricity cost, and flat depreciation fee
# Input: Amount of blocks mined in a month, amount of electricity used in kWh, recieved from user through keyboard
# Output: The net monthly profit is presented to the user
# Manmeet Singh
# Date: 9/22/21
# ***************

def main():
    # Defines constants for block price, electricity cost, and depreciation value
    BLOCK_PRICE = 52900.0
    COST_UNIT_ELECTRIC = 0.12
    HWR_DEPRECIATION = 100.0

    print("Program that calculates profit of a bitcoin miner.")

    # Prompts user to input blocks mined and electricity used within the month
    blocks_mined = float(input("Please enter the amount of blocks mined this month: "))
    electricity_used = float(input("Please enter the hours of electricity usage: "))

    # Calculates profit based on blocks mined and electricity used by the user
    revenue = blocks_mined * BLOCK_PRICE
    electric_cost = electricity_used * COST_UNIT_ELECTRIC
    net_profit = (revenue - electric_cost) - HWR_DEPRECIATION

    # Prints net profit to the user
    print(f"\nBitcoin miner monthly profit: ${net_profit}")
    return


main()
