import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
import tkinter.messagebox as messagebox

# Global variables to track the status and start time for each unit
unit_statuses = [False] * 6
unit_start_times = [None] * 6
counter_labels = []
rental_statuses = [tk.StringVar() for _ in range(6)]

def start_rent(unit):
    if not unit_statuses[unit]:
        current_time = datetime.now().strftime("%H:%M:%S")
        start_time_labels[unit].config(text="Start Time: " + current_time)
        unit_start_times[unit] = time.time()  # Record the start time
        unit_statuses[unit] = True
        rental_statuses[unit].set("BUSY")
        status_labels[unit].config(foreground="red", font=("Helvetica", 10, "bold"))
        update_counter(unit)

def stop_rent(unit):
    if unit_statuses[unit]:
        end_time = time.time()
        elapsed_time = round(end_time - unit_start_times[unit], 2)  # Calculate elapsed time
        stop_time_labels[unit].config(text="Stop Time: " + datetime.now().strftime("%H:%M:%S"))
        unit_statuses[unit] = False
        status_labels[unit].config(foreground="green", font=("Helvetica", 10, "bold"))
        rental_statuses[unit].set("READY")
        counter_labels[unit].after_cancel(counter_jobs[unit])  # Stop the counter
        # Show a confirmation message box with the unit number
        confirm_stop = messagebox.askyesno("Confirmation", "Stop renting for Unit {}?".format(unit + 1))
        if confirm_stop:
            # Add logic to handle the rental stop and payment here
            print("Rental stopped for Unit {}.".format(unit + 1))
    else:
        messagebox.showerror("Error", "Unit {} is not currently rented.".format(unit + 1))

def update_counter(unit):
    if unit_statuses[unit]:
        elapsed_time = round(time.time() - unit_start_times[unit], 2)  # Calculate elapsed time
        counter_labels[unit].config(text="Elapsed Time: {} seconds".format(elapsed_time))
        counter_jobs[unit] = counter_labels[unit].after(1000, lambda: update_counter(unit))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Entertainment Center Management")
    root.configure(bg='lightblue')

    unit_rectangles = []
    start_time_labels = []
    stop_time_labels = []
    status_labels = []
    counter_jobs = [None] * 6

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

        status_label = tk.Label(frame, textvariable=rental_statuses[i], fg="green", font=("Helvetica", 10, "bold"))
        status_label.pack()
        status_labels.append(status_label)

        counter_label = tk.Label(frame, text="Elapsed Time: 0.0 seconds")
        counter_label.pack()
        counter_labels.append(counter_label)

        style = ttk.Style()
        style.configure("TButton",
                        foreground="black",
                        background="lightgray",
                        font=("Helvetica", 12))

        start_button = ttk.Button(frame, text="Start Rent", command=lambda i=i: start_rent(i))
        start_button.pack(side="left")

        stop_button = ttk.Button(frame, text="Stop Rent", command=lambda i=i: stop_rent(i))
        stop_button.pack(side="left")

        # Add item and checkout buttons
        add_item_button = ttk.Button(frame, text="Add Item", command=lambda i=i: add_item(i))
        add_item_button.pack(side="left")

        checkout_button = ttk.Button(frame, text="Checkout", command=lambda i=i: checkout(i))
        checkout_button.pack(side="left")

        unit_rectangles.append(frame)

    root.mainloop()
