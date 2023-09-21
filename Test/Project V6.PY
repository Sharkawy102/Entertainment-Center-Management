import tkinter as tk
from tkinter import ttk, Menu
from datetime import datetime
import time
import tkinter.messagebox as messagebox

# Global variables to track the start time and rental status for each unit
unit_start_times = [None] * 6
unit_busy_statuses = [False] * 6

def start_rent(unit):
    if not unit_busy_statuses[unit]:
        current_time = datetime.now().strftime("%H:%M:%S")
        start_time_labels[unit].config(text="Start Time: " + current_time)
        unit_start_times[unit] = time.time()  # Record the start time
        unit_busy_statuses[unit] = True  # Set the unit status to BUSY
        status_labels[unit].config(text="Status: BUSY", fg="red", font=("Helvetica", 10, "bold"))
        update_status_count()
        # Clear the elapsed time label
        counter_labels[unit].config(text="")
    else:
        messagebox.showinfo("Info", "Unit {} is already BUSY.".format(unit + 1))

def stop_rent(unit):
    if unit_busy_statuses[unit]:
        current_time = datetime.now().strftime("%H:%M:%S")
        start_time = unit_start_times[unit]
        if start_time is not None:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)  # Calculate elapsed time
            stop_time_labels[unit].config(text="Stop Time: " + current_time)
            unit_busy_statuses[unit] = False  # Set the unit status to READY
            status_labels[unit].config(text="Status: READY", fg="green", font=("Helvetica", 10, "bold"))
            update_status_count()
            counter_labels[unit].config(text="Elapsed Time: {} seconds".format(elapsed_time))
            unit_start_times[unit] = None  # Reset the start time

            # Show a confirmation message box with the unit number
            confirm_stop = messagebox.askyesno("Confirmation", "Stop renting for Unit {}?".format(unit + 1))
            if confirm_stop:
                # Add logic to handle the rental stop and payment here
                print("Rental stopped for Unit {}.".format(unit + 1))
        else:
            messagebox.showerror("Error", "Please start renting first.")
    else:
        messagebox.showinfo("Info", "Unit {} is already READY.".format(unit + 1))

def update_status_count():
    busy_count = sum(unit_busy_statuses)
    ready_count = 6 - busy_count  # Total units minus busy units
    busy_label.config(text="Busy: {}".format(busy_count))
    ready_label.config(text="Ready: {}".format(ready_count))

root = tk.Tk()
root.title("Entertainment Center Management")
root.configure(bg='lightblue')

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add menu options (File, Inventory, Log, Settings, Help)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

inventory_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Inventory", menu=inventory_menu)
inventory_menu.add_command(label="Add Item")
inventory_menu.add_command(label="Remove Item")

log_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Log", menu=log_menu)
log_menu.add_command(label="View Log")

settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Preferences")

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

unit_rectangles = []
start_time_labels = []
stop_time_labels = []
counter_labels = []
status_labels = []

for i in range(6):
    frame = tk.Frame(root, borderwidth=2, relief="solid", width=200, height=150)
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

    counter_label = tk.Label(frame, text="", font=("Helvetica", 10))
    counter_label.pack()
    counter_labels.append(counter_label)

    status_label = tk.Label(frame, text="Status: READY", fg="green", font=("Helvetica", 10, "bold"))
    status_label.pack()
    status_labels.append(status_label)

    style = ttk.Style()
    style.configure("TButton",
                    foreground="black",
                    background="lightgray",
                    font=("Helvetica", 12))

    start_button = ttk.Button(frame, text="Start Rent", command=lambda i=i: start_rent(i))
    start_button.pack(side="left")

    stop_button = ttk.Button(frame, text="Stop Rent", command=lambda i=i: stop_rent(i))
    stop_button.pack(side="left")

    add_item_button = ttk.Button(frame, text="Add Item", command=lambda i=i: add_item(i))
    add_item_button.pack(side="left")

    checkout_button = ttk.Button(frame, text="Checkout", command=lambda i=i: checkout(i))
    checkout_button.pack(side="left")

    unit_rectangles.append(frame)

# Add total count labels at the bottom
total_count_frame = tk.Frame(root, bg='lightblue')
total_count_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=10)

busy_label = tk.Label(total_count_frame, text="Busy: 0", fg="red", font=("Helvetica", 12, "bold"))
busy_label.grid(row=0, column=0, padx=20)

ready_label = tk.Label(total_count_frame, text="Ready: 6", fg="green", font=("Helvetica", 12, "bold"))
ready_label.grid(row=0, column=1, padx=20)

root.mainloop()