amount_due = 50

while amount_due > 0:

    coin = input("Insert Coin: ")

    if not coin.isdigit():
        print("Please insert a valid integer coin")
        continue

    coin = int(coin)

    if coin != 5 and coin != 10 and coin != 25:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {amount_due}")
        continue

    amount_due = amount_due - coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")
