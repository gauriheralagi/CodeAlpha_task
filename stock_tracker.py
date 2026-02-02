price_chart = {
    "INFY": 1500,
    "TCS": 3600,
    "WIPRO": 450
}

final_amount = 0
print("My Stock Calculator")

while True:
    stock = input("Stock name (or stop): ").upper()

    if stock == "STOP":
        break

    if stock in price_chart:
        units = int(input("Number of shares: "))
        total = price_chart[stock] * units
        final_amount += total
        print("Total price:", total)
    else:
        print("Invalid stock name!")

with open("my_stocks.txt", "w") as f:
    f.write("Overall Investment: " + str(final_amount))

print("Saved in my_stocks.txt")
