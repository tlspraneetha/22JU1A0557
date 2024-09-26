import os
import pandas as pd
import matplotlib.pyplot as plt

# Hypothetical market cap values (in billions of USD) for the pie chart
market_caps = {
    'AAPL': 2300,
    'MSFT': 2100,
    'GOOGL': 1600,
    'AMZN': 1700,
    'TSLA': 900,
    'BRK-B': 600,
    'NVDA': 500,
    'META': 700,
    'JNJ': 400,
    'V': 500
}

# List of top 10 companies by market cap with their full names
top_10_companies = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc.',
    'AMZN': 'Amazon.com, Inc.',
    'TSLA': 'Tesla, Inc.',
    'BRK-B': 'Berkshire Hathaway Inc.',
    'NVDA': 'NVIDIA Corporation',
    'META': 'Meta Platforms, Inc.',
    'JNJ': 'Johnson & Johnson',
    'V': 'Visa Inc.'
}

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
csv_file_path = os.path.join(current_directory, 'top_10_stocks_sample_2013_2023.csv')

# Load the sample CSV file
df = pd.read_csv(csv_file_path)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract the year from the 'Date' column
df['Year'] = df['Date'].dt.year

# List of stock columns
stock_columns = ['AAPL_Close', 'MSFT_Close', 'GOOGL_Close', 'AMZN_Close', 'TSLA_Close',
                 'BRK-B_Close', 'NVDA_Close', 'META_Close', 'JNJ_Close', 'V_Close']

# Calculate the average closing price for each year
average_prices = df.groupby('Year')[stock_columns].mean().reset_index()

# Plot bar graphs for the average closing prices
plt.figure(figsize=(20, 10))
bar_width = 0.1
years = average_prices['Year']

# Define positions for the bars
positions = [years + i * bar_width for i in range(len(stock_columns))]

# Plot each stock's average price as a bar
for i, column in enumerate(stock_columns):
    plt.bar(positions[i], average_prices[column], width=bar_width, label=column.split('_')[0])

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Average Closing Price')
plt.title('Average Closing Price of Top 10 Stocks (2013-2023)')
plt.xticks(years + bar_width * 4.5, years)
plt.legend()
plt.tight_layout()
plt.show()

# Plot the pie chart
def plot_pie_chart():
    labels = [top_10_companies[ticker] for ticker in top_10_companies]
    sizes = [market_caps[ticker] for ticker in top_10_companies]
    
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Market Cap Distribution of Top 10 Companies')
    plt.show()

# Call the function to plot the pie chart
plot_pie_chart()