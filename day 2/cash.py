import math

def main():
    dollar = money()
    cents = dollar * 100
    cents = int(cents)
    quarter = math.floor(cents / 25)
    cents = cents - (quarter * 25)
    dime = math.floor(cents / 10)
    cents = cents - (dime * 10)
    nickel = math.floor(cents / 5)
    cents = cents - (nickel * 5)
    pennie = cents
    coin = quarter + dime + nickel + pennie
    print(coin)





def money():
    while True:
        n = float(input("money in dollars: "))
        if n >= 0:
            return n

main()