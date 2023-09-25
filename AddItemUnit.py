import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, ttk, Menu
from datetime import datetime, timedelta
import time
import tkinter.messagebox as messagebox


# create add item window
def add_item(unit):
    root = tk.Tk()
    root.title("Add Item Window")
    root.geometry('500x500')
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl1 = ttk.Notebook(tab1)

    tabControl.add(tab1, text='Drinks')
    tabControl.add(tab2, text='Foods')
    tabControl.pack(expand=1, fill="both")

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

            # Calculate the total cost (item price x quantity)
            item_price = 25  # Fixed price for each item (e.g., 25 EGP)
            total_cost = item_price * quantity

            # Memorize the total cost for adding it to the bill later
            global item_total
            item_total = total_cost
            # Display the total cost in a big bold format
            # result_label.config(text=f"Total: {total_cost} EGP", font=("Helvetica", 24, "bold"), fg="red", border=True, borderwidth=1)
            result_label = tk.Label(tab1, text=f"Total: {total_cost} EGP", font=(
                "Helvetica", 24, "bold"), fg="#39FF14", border=True, borderwidth=1)
            result_label.place(x=150, y=420)
        except ValueError:
            # Handle the case where quantity is not a valid integer
            # result_label.config(text="Invalid quantity")
            result_label = tk.Label(tab1, text=f"Invalid Quantity", font=(
                "Helvetica", 24, "bold"), fg="#FF073A", border=True, borderwidth=1)
            result_label.place(x=150, y=420)

    listbox = Listbox(tab1, width=35, height=15, selectmode=tk.SINGLE)
    listbox.insert(1, "Pepsi")
    listbox.insert(2, "Coca")
    listbox.insert(3, "Sprit")
    listbox.insert(4, "7up")
    listbox.insert(5, "Tea")
    listbox.insert(6, "Coffe")

    listbox.pack()
    listbox.place(x=40, y=40)
    label = Label(tab1, text='Quantity:', fg="black").place(x=18, y=300)
    entry = Entry(tab1, )
    entry.place(x=75, y=300)

    multiply_button = tk.Button(
        tab1, text='Add to Check', command=multiply_item)
    multiply_button.place(x=160, y=350)

    ttk.Label(tab2,
              text="Lets dive into the\
            world of computers").grid(column=0,
                                      row=0,
                                      padx=100,
                                      pady=30)
    root.mainloop()
