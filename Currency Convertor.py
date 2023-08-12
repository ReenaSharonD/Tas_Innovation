import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

root = tk.Tk()
root.title("Currency Converter")

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()

        c = CurrencyRates()
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate

        result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

label_amount = tk.Label(root, text="Amount:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

label_from_currency = tk.Label(root, text="From Currency:")
label_from_currency.pack()

combo_from_currency = ttk.Combobox(root, values=["USD", "EUR", "JPY", "GBP", "AUD", "CAD"])
combo_from_currency.pack()

label_to_currency = tk.Label(root, text="To Currency:")
label_to_currency.pack()

combo_to_currency = ttk.Combobox(root, values=["USD", "EUR", "JPY", "GBP", "AUD", "CAD"])
combo_to_currency.pack()

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
