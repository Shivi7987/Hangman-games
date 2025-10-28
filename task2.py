# Stock Portfolio Tracker

# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}  # To store user input (stock name and quantity)
total_investment = 0.0

print("Welcome to the Stock Portfolio Tracker!\n")
print("Available Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when finished.\n")

# Get user input
while True:
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
print("\n📊 Portfolio Summary:")
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save result to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock]*quantity}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")
else:
    print("Summary not saved.")

