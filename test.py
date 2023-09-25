# import db_Units_for_Rent as items
# items.units()
# # items.addUnits("Number 1", 10, True)
# # items.addUnits("Number 2", 10, True)
# # items.addUnits("Number 3", 10, True)
# # items.addUnits("Number 4", 10, True)
# # items.addUnits("Number 5", 10, True)
# # items.addUnits("Number 6", 10, True)
# units = items.viewUnits()
# for unit in units:
#     print(unit)
import tkinter as tk
from tkinter import ttk
import sqlite3
import db_Units_for_Rent as iii
# Define your SQLite database functions here
# Example: units(), start_rent(i), stop_rent(i), add_item(i), checkout(i)

# Function to create UI elements for a unit


def create_unit_ui(unit_info):
    frame = tk.Frame(main_window, borderwidth=2,
                     relief="solid", width=200, height=150)
    frame.grid(padx=10, pady=10)

    unit_label = tk.Label(frame, text="Unit: {}".format(unit_info["UnitName"]))
    unit_label.pack()

    start_time_label = tk.Label(frame, text="Start Time: N/A")
    start_time_label.pack()
    start_time_labels.append(start_time_label)

    stop_time_label = tk.Label(frame, text="Stop Time: N/A")
    stop_time_label.pack()
    stop_time_labels.append(stop_time_label)

    counter_label = tk.Label(frame, text="", font=("Helvetica", 10))
    counter_label.pack()
    counter_labels.append(counter_label)

    status_label_text = "Status: {}".format(
        "READY" if unit_info["AvailabilityStatus"] else "NOT READY")
    status_label = tk.Label(frame, text=status_label_text,
                            fg="green" if unit_info["AvailabilityStatus"] else "red", font=("Helvetica", 10, "bold"))
    status_label.pack()
    status_labels.append(status_label)

    rent_cost_label = tk.Label(frame, text="Total Cost Rent + Cafeteria: N/A")
    rent_cost_label.pack()
    rent_cost_labels.append(rent_cost_label)

    style = ttk.Style()
    style.configure("TButton", foreground="black",
                    background="lightgray", font=("Helvetica", 12))

    start_button = ttk.Button(frame, text="Start Rent",
                              command=lambda: start_rent(unit_info["UnitId"]))
    start_button.pack(side="left")

    stop_button = ttk.Button(frame, text="Stop Rent",
                             command=lambda: stop_rent(unit_info["UnitId"]))
    stop_button.pack(side="left")

    add_item_button = ttk.Button(
        frame, text="Add Item", command=lambda: add_item(unit_info["UnitId"]))
    add_item_button.pack(side="left")

    checkout_button = ttk.Button(
        frame, text="Checkout", command=lambda: checkout(unit_info["UnitId"]))
    checkout_button.pack(side="left")


unit_infos = iii.viewUnits()

main_window = tk.Tk()
main_window.title("Unit Management")

# Lists to store labels and other elements
start_time_labels = []
stop_time_labels = []
counter_labels = []
status_labels = []
rent_cost_labels = []

# Create UI elements for each unit
for unit_info in unit_infos:
    create_unit_ui({
        "UnitId": unit_info[0],
        "UnitName": unit_info[1],
        "AvailabilityStatus": bool(unit_info[2])
    })

main_window.mainloop()
