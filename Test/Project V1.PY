import tkinter as tk
from datetime import datetime

def start_rent(unit):
    current_time = datetime.now().strftime("%H:%M:%S")
    start_time_labels[unit].config(text="Start Time: " + current_time)

def stop_rent(unit):
    current_time = datetime.now().strftime("%H:%M:%S")
    stop_time_labels[unit].config(text="Stop Time: " + current_time)

def add_item(unit):
    # Add logic to add an item from inventory to the customer's cart for the specified unit.
    pass

def checkout(unit):
    # Add logic to calculate the total cost and handle the payment process for the specified unit.
    pass

root = tk.Tk()
root.title("Entertainment Center Management")

unit_rectangles = []
start_time_labels = []
stop_time_labels = []

for i in range(6):
    frame = tk.Frame(root, borderwidth=2, relief="solid")
    row = i // 3
    col = i % 3
    frame.grid(row=row, column=col)

    unit_label = tk.Label(frame, text="Unit {}".format(i + 1))
    unit_label.pack()

    start_time_label = tk.Label(frame, text="Start Time: N/A")
    start_time_label.pack()
    start_time_labels.append(start_time_label)

    stop_time_label = tk.Label(frame, text="Stop Time: N/A")
    stop_time_label.pack()
    stop_time_labels.append(stop_time_label)

    unit_rectangles.append(frame)

    add_item_button = tk.Button(frame, text="Add Item", command=lambda i=i: add_item(i))
    add_item_button.pack()

    checkout_button = tk.Button(frame, text="Checkout & Pay", command=lambda i=i: checkout(i))
    checkout_button.pack()

root.mainloop()
