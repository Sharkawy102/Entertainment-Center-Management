# This is the Login_Page class created for E.C.O.M
# Importing libraries..
import AdminPanel as AP
from customtkinter import *
from PIL import Image
import db_Users as Users
import Employee_Window as EW
owner_title = ('E.C.O.M')


class LoginPage:
    def __init__(self):
        # Set window properties and information
        set_appearance_mode("Dark")
        # set_default_color_theme('theme.JSON')
        set_widget_scaling(1.0)
        set_window_scaling(1.0)

        # Initiate window
        self.login_page = CTk()

        # Get the screen width and height
        screen_width = self.login_page.winfo_screenwidth()
        screen_height = self.login_page.winfo_screenheight()

        # Set the window's dimensions
        window_width = 600
        window_height = 480

        # Calculate the x and y coordinates for the window to be centered
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window's position  responsively to be centered on screen according to size
        self.login_page.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set the window title & resize
        self.login_page.title(f'{owner_title} -Login Page')
        self.login_page.resizable(False, False)

        # Load images
        side_img_data = Image.open(
            "Login_Page_Class_Template\\side-img.png")
        user_icon_data = Image.open(
            "Login_Page_Class_Template\\user-icon.png")
        password_icon_data = Image.open(
            "Login_Page_Class_Template\password-icon.png")
        login_icon_data = Image.open(
            "Login_Page_Class_Template\login-icon.png")

        # Store images
        side_img = CTkImage(dark_image=side_img_data,
                            light_image=side_img_data, size=(300, 480))
        user_icon = CTkImage(dark_image=user_icon_data,
                             light_image=user_icon_data, size=(20, 20))
        password_icon = CTkImage(
            dark_image=password_icon_data, light_image=password_icon_data, size=(20, 20))
        login_icon = CTkImage(dark_image=login_icon_data,
                              light_image=login_icon_data, size=(20, 20))

        # Create UI elements
        CTkLabel(master=self.login_page, text="",
                 image=side_img).pack(expand=True, side="left")

        frame = CTkFrame(master=self.login_page, width=300,
                         height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        CTkLabel(master=frame, text="Welcome to E.C.O.M!", text_color="#071952", anchor="w", justify="left",
                 font=("Segoe UI Black", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Log-in to your user account", text_color="#071952", anchor="w", justify="left",
                 font=("Segoe UI Semibold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  USER ID:", text_color="#071952", anchor="w", justify="left",
                 font=("Dungeon", 14), image=user_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        userEntry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#071952", border_width=1,
                             text_color="#000000")
        userEntry.pack(anchor="w", padx=(25, 0))
        CTkLabel(master=frame, text="  PASSWORD:", text_color="#071952", anchor="w", justify="left",
                 font=("Dungeon", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0),
                                                                                  padx=(25, 0))

        passEntry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#071952", border_width=1,
                             text_color="#000000", show="*")
        passEntry.pack(anchor="w", padx=(25, 0))

        def checkRole():
            userName = userEntry.get()
            password = passEntry.get()
            role = Users.login(userName, password, "Admin")
            role = Users.login(userName, password, "Employee")
            if role == "Admin":
                self.login_page.destroy()
                Admin_window1 = AP.AdminPanel()
                print("Admin")
                Admin_window1.run()
            elif role == "Employee":
                self.login_page.destroy()
                employee_window1 = EW.EmployeeWindow()
                print("Employee2")
                employee_window1.run()

        CTkButton(master=frame, text="Login", image=login_icon, fg_color="#419197", hover_color="#12486B",
                  font=("Dungeon", 22), text_color="#ffffff", height=40, width=225,
                  command=lambda: checkRole()).pack(anchor="w", pady=(40, 0), padx=(25, 0))

    def run(self):
        self.login_page.mainloop()


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.run()
