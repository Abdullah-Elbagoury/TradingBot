import pandas as pd
import os

# List of stock tickers corresponding to the CSV files
stock_tickers = ['TSLA', 'TBIO', 'SNDL', 'SAVA', 'ROKU', 'PDD', 'GNLN', 'DOCU', 'CMLS', 'AVGR']

def load_and_combine_data():
    all_data = []
    data_dir = 'data/'
    for ticker in stock_tickers:
        # Construct the file path for CSV files
        file_path = os.path.join(data_dir, f'{ticker}.csv')
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            df['Ticker'] = ticker
            all_data.append(df)
        else:
            print(f"File not found: {file_path}")
    # Concatenate all DataFrames into one
    full_data = pd.concat(all_data)
    full_data.to_csv('data/full_historical_data.csv', index=False)
    return full_data
