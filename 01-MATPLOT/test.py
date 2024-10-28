import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set the ticker symbol for Tata Steel
ticker_symbol = "TATASTEEL.NS"  # .NS for National Stock Exchange of India

# Calculate the date range (10 years ago from today)
end_date = datetime.now()
start_date = end_date - timedelta(days=365 * 10)

# Fetch the data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Closing Price')

# Customize the plot
plt.title(f"Tata Steel Share Price (Past 10 Years)")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)

# Rotate and align the tick labels so they look better
plt.gcf().autofmt_xdate()

# Show the plot
plt.tight_layout()
plt.show()

