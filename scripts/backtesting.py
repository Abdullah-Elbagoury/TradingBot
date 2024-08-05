# scripts/backtesting.py

def simulate_real_time(data, strategy_func):
    trade_log = []
    for _, row in data.iterrows():
        signal = strategy_func(row)
        if signal == 'buy':
            trade_log.append((row['Date'], row['Ticker'], 'Buy', row['Close']))
            print(f"Buying {row['Ticker']} at {row['Date']}, price: {row['Close']}")
        elif signal == 'sell':
            trade_log.append((row['Date'], row['Ticker'], 'Sell', row['Close']))
            print(f"Selling {row['Ticker']} at {row['Date']}, price: {row['Close']}")  # Corrected line
    return trade_log
