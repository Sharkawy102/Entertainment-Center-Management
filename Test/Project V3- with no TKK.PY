import tkinter as tk
from datetime import datetime

def start_rent(unit):
    current_time = datetime.now().strftime("%H:%M:%S")
    start_time_labels[unit].config(text="Start Time: " + current_time)

def stop_rent(unit):
    current_time = datetime.now().strftime("%H:%M:%S")
    stop_time_labels[unit].config(text="Stop Time: " + current_time)

def add_item(unit):
    # Add logic to add an item from inventory to the customer's cart for the selected unit.
    pass

def checkout(unit):
    # Add logic to calculate the total cost and handle the payment process for the selected unit.
    pass

root = tk.Tk()
root.title("Entertainment Center Management")

# Set background color
root.configure(bg="#F4F4F4")  # You can change the color code as desired

unit_rectangles = []
start_time_labels = []
stop_time_labels = []

for i in range(6):
    frame = tk.Frame(root, borderwidth=2, relief="solid", width=200, height=100, bg="white")
    row = i // 3
    col = i % 3
    frame.grid(row=row, column=col, padx=10, pady=10)

    unit_label = tk.Label(frame, text="Unit {}".format(i + 1))
    unit_label.pack()

    start_time_label = tk.Label(frame, text="Start Time: N/A")
    start_time_label.pack()
    start_time_labels.append(start_time_label)

    stop_time_label = tk.Label(frame, text="Stop Time: N/A")
    stop_time_label.pack()
    stop_time_labels.append(stop_time_label)

    # Styling for buttons
    button_style = {"bg": "#007ACC", "fg": "white", "borderwidth": 2, "relief": "raised", "width": 12}

    start_button = tk.Button(frame, text="Start Rent", command=lambda i=i: start_rent(i), **button_style)
    start_button.pack(side="left", padx=5)

    stop_button = tk.Button(frame, text="Stop Rent", command=lambda i=i: stop_rent(i), **button_style)
    stop_button.pack(side="left", padx=5)

    add_item_button = tk.Button(frame, text="Add Item", command=lambda i=i: add_item(i), **button_style)
    add_item_button.pack(side="left", padx=5)

    checkout_button = tk.Button(frame, text="Checkout", command=lambda i=i: checkout(i), **button_style)
    checkout_button.pack(side="left", padx=5)

    unit_rectangles.append(frame)

root.mainloop()
