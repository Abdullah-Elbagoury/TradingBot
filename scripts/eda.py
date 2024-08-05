import matplotlib.pyplot as plt

def plot_data(data, column):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data[column])
    plt.title(f"{column} over Time")
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.show()
