import customtkinter as ctk

# Create a root window

theme_path = 'D:\\Backup (E)\\Python - Cafe MGT Project\\Anthracite.json'
ctk.set_default_color_theme(theme_path)
root = ctk.CTk()
root._set_appearance_mode("System")
root.title("Login Page")

# Set the default theme to the provided JSON file path

# Create and configure widgets for the login page
username_label = ctk.CTkLabel(root, text="Username:")
username_label.pack()

username_entry = ctk.CTkEntry(root)
username_entry.pack()

password_label = ctk.CTkLabel(root, text="Password:")
password_label.pack()

password_entry = ctk.CTkEntry(root, show="*")  # Passwords are usually hidden
password_entry.pack()

login_button = ctk.CTkButton(root, text="Login", command=lambda: login(username_entry.get(), password_entry.get()), fg_color="green",text_color="white")
login_button.pack()

# Define a login function
def login(username, password):
    # Replace this with your authentication logic
    if username == "admin" and password == "password":
        ctk.messagebox.showinfo("Login", "Login successful!")
    else:
        ctk.messagebox.showerror("Login", "Invalid credentials")

# Start the GUI main loop
root.mainloop()
