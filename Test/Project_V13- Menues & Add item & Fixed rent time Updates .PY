import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, ttk, Menu
from datetime import datetime, timedelta
import time
import tkinter.messagebox as messagebox

# Global variables to track the start time and rental status for each unit
unit_start_times = [None] * 6
unit_busy_statuses = [False] * 6

def start_rent(unit):
    if not unit_busy_statuses[unit]:
        result = messagebox.askquestion("Rental time", "Is the rental start time specified?")
        if result == 'yes':
            hoursWindow= tk.Tk()
            hoursWindow.geometry('200x185')
            label = Label(hoursWindow, text='Hours:').place(x= 40, y=20)
            entry = Entry(hoursWindow,)
            entry.place(x= 40, y=40)
            def ok():
                input_hours = entry.get()
                try:
                    input_hours = int(input_hours)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    start_time_labels[unit].config(text="Start Time: " + current_time)
                    hoursWindow.destroy()
                    end_time = (datetime.now() + timedelta(hours=input_hours)).strftime("%H:%M:%S")
                    unit_start_times[unit] = time.time()  # Record the start time
                    unit_busy_statuses[unit] = True  # Set the unit status to BUSY
                    status_labels[unit].config(text="Status: BUSY", fg="red", font=("Helvetica", 10, "bold"))
                    update_status_count()
                    stop_time_labels[unit].config(text="Stop Time: " + end_time)
                    print("End Time:", end_time)
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter a valid number of hours")
            buttonOK = Button(hoursWindow, text='Ok', command=ok, width=8)
            buttonOK.place(x=37, y=80)
        else:
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
           

            # Show a confirmation message box with the unit number
            confirm_stop = messagebox.askyesno("Confirmation", "Stop renting for Unit {}?".format(unit + 1))
            if confirm_stop:
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)  # Calculate elapsed time
                stop_time_labels[unit].config(text="Stop Time: " + current_time)
                unit_busy_statuses[unit] = False  # Set the unit status to READY
                status_labels[unit].config(text="Status: READY", fg="green", font=("Helvetica", 10, "bold"))
                update_status_count()
                counter_labels[unit].config(text="Elapsed Time: {} seconds".format(elapsed_time))
                unit_start_times[unit] = None  # Reset the start time
                # Add logic to handle the rental stop and payment here
                print("Rental stopped for Unit {}.".format(unit + 1))
            else:
                # If "No" is pressed, do not stop the rental process
                unit_busy_statuses[unit] = True
                status_labels[unit].config(text="Status: BUSY", fg="red", font=("Helvetica", 10, "bold"))
                # start_time_labels[unit].config(text="Start Time: " + current_time)
                stop_time_labels[unit].config(text="Stop Time: N/A")
        else:
            messagebox.showerror("Error", "Please start renting first.")
    else:
        messagebox.showinfo("Info", "Unit {} is already READY.".format(unit + 1))

def clear(unit):
    start_time_labels[unit].config(text="Start Time: N/A")
    stop_time_labels[unit].config(text="Stop Time: N/A")
    counter_labels[unit].config(text="")



def update_status_count():
    busy_count = sum(unit_busy_statuses)
    ready_count = 6 - busy_count  # Total units minus busy units
    busy_label.config(text="Busy: {}".format(busy_count))
    ready_label.config(text="Ready: {}".format(ready_count))

def open_main_window():
    login_window.destroy()  # Close the login window
    main_window.deiconify()  # Show the main window

def login():
    # Add logic to check the login credentials here
    # For simplicity, let's assume successful login for now
    open_main_window()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.configure(bg='lightblue')

# Create labels and entry fields for username and password
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=10)
username_entry = ttk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = ttk.Entry(login_window, show="*")  # Mask the password
password_entry.pack()

# Create a login button
login_button = ttk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

# Create the main window (hidden initially)
main_window = tk.Tk()
main_window.title("Entertainment Center Management")
main_window.configure(bg='lightblue')
main_window.withdraw()  # Hide the main window initially


# create add item window
def add_item(unit):
    root = tk.Tk()
    root.title("Add Item Window")
    root.geometry('500x500')
    tabControl = ttk.Notebook(root)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl1 = ttk.Notebook(tab1)
    
    tabControl.add(tab1, text ='Drinks')
    tabControl.add(tab2, text ='Foods')
    tabControl.pack(expand = 1, fill ="both")
    
    def multiply_item():
        # Get the selected item from the Listbox
        selected_index = listbox.curselection()
        if not selected_index:
            return  # No item selected, exit the function
        selected_item = listbox.get(selected_index)

        # Get the quantity from the Entry
        quantity = entry.get()

        try:
            # Convert quantity to an integer
            quantity = int(quantity)

            # Multiply the item by the quantity
            result = f"{selected_item} x {quantity} = {selected_item * quantity}"

            # Display the result
            result_label.config(text=result)
        except ValueError:
            # Handle the case where quantity is not a valid integer
            result_label.config(text="Invalid quantity")

      
    
    listbox = Listbox(tab1 , width=35 , height=15, selectmode=tk.SINGLE)
    listbox.insert(1, "Pepsi")
    listbox.insert(2, "Coca")
    listbox.insert(3, "Sprit")
    listbox.insert(4, "7up")
    listbox.insert(5, "Tea")
    listbox.insert(6, "Coffe")

    listbox.pack()
    listbox.place(x= 40, y=40)
    label = Label(tab1, text='Quantity:',fg="black").place(x= 18, y=300)
    entry =Entry(tab1, )
    entry.place(x=75, y=300)

    multiply_button = tk.Button(tab1, text='Multiply', command=multiply_item)
    multiply_button.place(x=160, y=350)

    result_label = tk.Label(tab1, text='', fg="black")
    result_label.place(x=18, y=240)
    ttk.Label(tab2,
            text ="Lets dive into the\
            world of computers").grid(column = 0,
                                        row = 0, 
                                        padx = 100,
                                        pady = 30)

# Create a menu bar for the main window
menu_bar = Menu(main_window)
main_window.config(menu=menu_bar)

# Add menu options (File, Inventory, Log, Settings, Help)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=main_window.quit)

inventory_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Inventory", menu=inventory_menu)
inventory_menu.add_command(label="Add Item")
inventory_menu.add_command(label="Remove Item")

employees_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Employees", menu=employees_menu)
employees_menu.add_command(label="Manage employees")

branches_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="branches", menu=branches_menu)
branches_menu.add_command(label="Manage branches")

revenues_expenses_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Revenues / Expenses", menu=revenues_expenses_menu)
revenues_expenses_menu.add_command(label="Add Revenue")
revenues_expenses_menu.add_separator()
revenues_expenses_menu.add_command(label="Add Expense")

log_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Log", menu=log_menu)
log_menu.add_command(label="View Log")

settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Preferences")

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

# Rest of the code for the main window (similar to the previous version)

unit_rectangles = []
start_time_labels = []
stop_time_labels = []
counter_labels = []
status_labels = []

for i in range(6):
    frame = tk.Frame(main_window, borderwidth=2, relief="solid", width=200, height=150)
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

    # checkout_button = ttk.Button(frame, text="Clear", command=lambda i=i: clear(i))
    # checkout_button.pack(side="left")

    unit_rectangles.append(frame)

# Add total count labels at the bottom using grid
total_count_frame = tk.Frame(main_window, bg='lightblue')
total_count_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=10)

busy_label = tk.Label(total_count_frame, text="Busy: 0", fg="red", font=("Helvetica", 12, "bold"))
busy_label.grid(row=0, column=0, padx=20)

ready_label = tk.Label(total_count_frame, text="Ready: 6", fg="green", font=("Helvetica", 12, "bold"))
ready_label.grid(row=0, column=1, padx=20)

main_window.mainloop()
