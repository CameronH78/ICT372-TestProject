import tkinter as tk
from tkinter import ttk
from datetime import datetime
import yfinance as yf
from matplotlib import pyplot as plot
import seaborn as sns


def make_graph():
    symbol = symbol_set.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Collect the data from yfinance module using a symbol
    data = yf.download(symbol, start=start_date, end=end_date)

    # Visualize data
    plot.figure(figsize=(10, 6))
    sns.lineplot(x=data.index, y=data['Close'])
    if symbol == "GOOGL":
        plot.title(f'Stock Prices for GOOGLE')
        plot.xlabel('Date')
        plot.ylabel('Price')
        plot.show()
    elif symbol == "MSFT":
        plot.title(f'Stock Prices for Microsoft')
        plot.xlabel('Date')
        plot.ylabel('Price')
        plot.show()
    elif symbol == "AMZN":
        plot.title(f'Stock Prices for Amazon')
        plot.xlabel('Date')
        plot.ylabel('Price')
        plot.show()


def reset_boxes():
    start_date_entry.delete(0, 'end')
    end_date_entry.delete(0, 'end')
    #make_graph[symbol_set] = ttk.Entry(graph, width=20)


# Create main window
graph = tk.Tk()
graph.title("Test ICT-372 Graph")

# Create and place labels and talk boxes
start_date = ttk.Label(graph, text="Start date - (YYYY-MM-DD):")
start_date.grid(row=0, column=0, padx=10, pady=5)
start_date_entry = ttk.Entry(graph, width=20)
start_date_entry.grid(row=0, column=1, padx=10, pady=5)
start_date_entry.insert(0, '')

end_date = ttk.Label(graph, text="End date - (YYYY-MM-DD):")
end_date.grid(row=1, column=0, padx=10, pady=5)
end_date_entry = ttk.Entry(graph, width=20)
end_date_entry.grid(row=1, column=1, padx=10, pady=5)
end_date_entry.insert(0, '')

# Labels - Google - GOOGL, Microsoft - MSFT, Amazon - AMZN
symbol_label = ttk.Label(graph, text="Choose a stock - GOOGL, MSFT, AMZN:")
symbol_label.grid(row=2, column=0, padx=10, pady=5)
symbol_set = ttk.Entry(graph, width=20)
symbol_set.grid(row=2, column=1, padx=10, pady=5)

start_button = ttk.Button(graph, text="TEST BUTTON", command=make_graph)

start_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

start_button2 = ttk.Button(graph, text="RESET", command=reset_boxes)

start_button2.grid(row=3, column=1, columnspan=2, padx=5, pady=20)

# Start the Tkinter event loop
graph.mainloop()
