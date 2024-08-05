
def calculate_moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

def calculate_rsi(data, periods=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


# scripts/strategy.py
def scalping_strategy(row):
    short_ma = row['Short_MA']
    long_ma = row['Long_MA']
    rsi_value = row['RSI']

    if short_ma > long_ma and rsi_value < 70:
        return 'buy'
    elif short_ma < long_ma and rsi_value > 30:
        return 'sell'
    return 'hold'

