# main.py
import pandas as pd
from scripts.data_handler import load_and_combine_data
from scripts.backtesting import simulate_real_time
from scripts.strategy import scalping_strategy, calculate_moving_average, calculate_rsi

# Load full historical data
full_data = load_and_combine_data()

# Ensure 'Date' column is datetime
full_data['Date'] = pd.to_datetime(full_data['Date'])

# Sorting data by date
full_data = full_data.sort_values(by='Date')

# Calculate indicators
full_data['Short_MA'] = calculate_moving_average(full_data, 5)  # Example short-term moving average window
full_data['Long_MA'] = calculate_moving_average(full_data, 20)  # Example long-term moving average window
full_data['RSI'] = calculate_rsi(full_data)

# Data Segmentation
train_size = 0.6
backtest_size = 0.2
n_total = len(full_data)
n_train = int(n_total * train_size)
n_backtest = int(n_total * backtest_size)

# Data Segments
train_data = full_data.iloc[:n_train]
backtest_data = full_data.iloc[n_train:n_train + n_backtest]
simulated_real_time_data = full_data.iloc[n_train + n_backtest:]

# Apply the strategy and simulate trading
backtest_log = simulate_real_time(backtest_data, scalping_strategy)
real_time_log = simulate_real_time(simulated_real_time_data, scalping_strategy)

# Save logs
pd.DataFrame(backtest_log, columns=['Date', 'Ticker', 'Action', 'Price']).to_csv('data/backtest_log.csv', index=False)
pd.DataFrame(real_time_log, columns=['Date', 'Ticker', 'Action', 'Price']).to_csv('data/real_time_log.csv', index=False)
