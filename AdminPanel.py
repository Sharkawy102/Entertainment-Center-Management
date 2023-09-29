from customtkinter import *
from PIL import Image

owner_title = ("E.C.O.M")
logged_user = ("Admin")

# def toggle_button():
#     if CTkButton.winfo_width() == 0:
#         CTkButton.config(width=10)  # Set the normal width (adjust as needed)
#     else:
#         CTkButton.config(width=0)   # Set the width to 0


class AdminPanel:
    def __init__(self):
        # Set window properties and information
        set_appearance_mode("Dark")

        # set_default_color_theme('theme.JSON')
        set_widget_scaling(1.0)
        set_window_scaling(1.0)

        # Initiate window
        self.main_page = CTk()

        # Get the screen width and height
        screen_width = self.main_page.winfo_screenwidth()
        screen_height = self.main_page.winfo_screenheight()

        # Set the window's dimensions
        window_width = 1240
        window_height = 680

        # Calculate the x and y coordinates for the window to be centered
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window's position  responsively to be centered on screen according to size
        self.main_page.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set the window title & resize
        self.main_page.title(f'{owner_title} -Main Page')
        self.main_page.resizable(True, True)

        # Sidebar frame properties
        logo_img_data = Image.open("Main_Page_Class_Template\logo.png")
        self.sidebar_frame = CTkFrame(
            master=self.main_page, fg_color="#040D12", width=200, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        logo_img = CTkImage(dark_image=logo_img_data,
                            light_image=logo_img_data, size=(150.68, 170.42))
        CTkLabel(master=self.sidebar_frame, text="", image=logo_img).pack(
            pady=(38, 0), anchor="center")

        # Main frame properties
        self.main_frame = CTkFrame(master=self.main_page, fg_color="#040D12", width=1200, height=650,
                                   corner_radius=1)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", side="left")

        # Create a container frame for the buttons
        button_container = CTkFrame(
            master=self.main_frame, fg_color="#040D12", width=150, height=75)
        button_container.pack(anchor="ne", fill="both", padx=10, pady=(20, 5))

        # Logout Button
        logout_img_data = Image.open("Main_Page_Class_Template\logout.png")
        logout_img = CTkImage(dark_image=logout_img_data,
                              light_image=logout_img_data, size=(18, 18))
        CTkButton(master=button_container, image=logout_img, text="Log out", fg_color="#040D12",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="center").pack(side="right", padx=3)

        # Send Reports Button
        send_report_img_data = Image.open(
            "Main_Page_Class_Template\SendReports.png")
        send_report_img = CTkImage(
            dark_image=send_report_img_data, light_image=send_report_img_data, size=(18, 18))
        CTkButton(master=button_container, image=send_report_img, text="Send Reports", fg_color="#040D12",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="center").pack(side="right", padx=3)

        # Set a welcome message at top
        welcome_message = CTkLabel(master=self.main_frame, fg_color="#252B48", width=600, height=20, font=("Segoe UI Semilight", 12),
                                   corner_radius=4,
                                   text=f'Hi {logged_user}, what you wanna do today?')
        welcome_message.pack(anchor="center", fill="both",
                             padx=10, pady=(3, 0))

        # Metrics frame properties
        metrics_frame = CTkFrame(
            master=self.main_frame, fg_color="#040D15", width=150, height=75)
        metrics_frame.pack(anchor="nw", fill="x",  padx=10, pady=(20, 20))

        hours_metric = CTkFrame(master=metrics_frame,
                                fg_color="#35A29F", width=250, height=75)
        hours_metric.grid_propagate(0)
        hours_metric.pack(side="left")

        hours_img_data = Image.open("Main_Page_Class_Template\Hours.png")
        hours_img = CTkImage(light_image=hours_img_data,
                             dark_image=hours_img_data, size=(43, 43))

        CTkLabel(master=hours_metric, image=hours_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
        CTkLabel(master=hours_metric, text="Hours Played", text_color="#fff", font=(
            "Dungeon", 15)).grid(row=0, column=1, sticky="sw")
        CTkLabel(master=hours_metric, text="124 Hour", text_color="#fff", font=(
            "Dungeon", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

        revenues_metric = CTkFrame(
            master=metrics_frame, fg_color="#35A29F", width=250, height=75)
        revenues_metric.grid_propagate(0)
        revenues_metric.pack(side="left", expand=True, anchor="center")

        revenues_img_data = Image.open("Main_Page_Class_Template\Revenues.png")
        revenues_img = CTkImage(
            light_image=revenues_img_data, dark_image=revenues_img_data, size=(43, 43))

        CTkLabel(master=revenues_metric, image=revenues_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
        CTkLabel(master=revenues_metric, text="Revenues", text_color="#fff", font=(
            "Dungeon", 15)).grid(row=0, column=2, sticky="nw")
        CTkLabel(master=revenues_metric, text="37,000.00", text_color="#fff", font=(
            "Dungeon", 15), justify="left").grid(row=1, column=2, sticky="s", pady=(0, 10))

        expense_metric = CTkFrame(
            master=metrics_frame, fg_color="#35A29F", width=250, height=75)
        expense_metric.grid_propagate(0)
        expense_metric.pack(side="right")

        expense_img_data = Image.open("Main_Page_Class_Template\Expenses.png")
        expense_img = CTkImage(light_image=expense_img_data,
                               dark_image=expense_img_data, size=(43, 43))

        CTkLabel(master=expense_metric, image=expense_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

        CTkLabel(master=expense_metric, text="Expenses", text_color="#fff", font=(
            "Dungeon", 15)).grid(row=0, column=4, sticky="nw")
        CTkLabel(master=expense_metric, text="23,000.00", text_color="#fff", font=(
            "Dungeon", 15), justify="left").grid(row=1, column=4, sticky="s", pady=(0, 10))

        # Metrics frame2 properties
        metrics_frame = CTkFrame(
            master=self.main_frame, fg_color="#040D15", width=150, height=75)
        metrics_frame.pack(anchor="nw", fill="x",  padx=10, pady=(20, 20))

        hours_metric = CTkFrame(master=metrics_frame,
                                fg_color="#35A29F", width=250, height=75)
        hours_metric.grid_propagate(0)
        hours_metric.pack(side="left")

        hours_img_data = Image.open("Main_Page_Class_Template\Hours.png")
        hours_img = CTkImage(light_image=hours_img_data,
                             dark_image=hours_img_data, size=(43, 43))

        CTkLabel(master=hours_metric, image=hours_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
        CTkLabel(master=hours_metric, text="Hours Played", text_color="#fff", font=(
            "Dungeon", 15)).grid(row=0, column=1, sticky="sw")
        CTkLabel(master=hours_metric, text="124 Hour", text_color="#fff", font=(
            "Dungeon", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

        revenues_metric = CTkFrame(
            master=metrics_frame, fg_color="#35A29F", width=250, height=75)
        revenues_metric.grid_propagate(0)
        revenues_metric.pack(side="left", expand=True, anchor="center")

        revenues_img_data = Image.open("Main_Page_Class_Template\Revenues.png")
        revenues_img = CTkImage(
            light_image=revenues_img_data, dark_image=revenues_img_data, size=(43, 43))

        CTkLabel(master=revenues_metric, image=revenues_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
        CTkLabel(master=revenues_metric, text="Revenues", text_color="#fff", font=(
            "Dungeon", 15)).grid(row=0, column=2, sticky="nw")
        CTkLabel(master=revenues_metric, text="37,000.00", text_color="#fff", font=(
            "Dungeon", 15), justify="left").grid(row=1, column=2, sticky="s", pady=(0, 10))

        expense_metric = CTkFrame(
            master=metrics_frame, fg_color="#35A29F", width=250, height=75)
        expense_metric.grid_propagate(0)
        expense_metric.pack(side="right")

        expense_img_data = Image.open("Main_Page_Class_Template\Expenses.png")
        expense_img = CTkImage(light_image=expense_img_data,
                               dark_image=expense_img_data, size=(43, 43))

        CTkLabel(master=expense_metric, image=expense_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

        CTkLabel(master=expense_metric, text="Expenses", text_color="#fff", font=(
            "Dungeon", 15)).grid(row=0, column=4, sticky="nw")
        CTkLabel(master=expense_metric, text="23,000.00", text_color="#fff", font=(
            "Dungeon", 15), justify="left").grid(row=1, column=4, sticky="s", pady=(0, 10))

        # ... Add metrics and widgets here ...
        # Set scorllable frame on side panel
        self.scrollable_frame = CTkScrollableFrame(self.sidebar_frame, fg_color="#040D12", width=190, height=380,
                                                   corner_radius=10, scrollbar_button_color="#EE9322", scrollbar_button_hover_color="#219C90",
                                                   border_color="#fff")
        self.scrollable_frame.pack(fill="x", pady=15, anchor="center")
        self.scrollable_frame.pack_propagate(True)

        # Add buttons and widgets to the sidebar
        settings_img_data = Image.open("Main_Page_Class_Template\settings.png")
        settings_img = CTkImage(
            dark_image=settings_img_data, light_image=settings_img_data)
        CTkButton(master=self.scrollable_frame, image=settings_img, text="System Settings",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="e",
                  command=lambda: switch_frame(self.scrollable_frame)).pack(anchor="w", ipady=5, pady=(16, 0))

        inputs_img_data = Image.open("Main_Page_Class_Template\inputs.png")
        inputs_img = CTkImage(dark_image=inputs_img_data,
                              light_image=inputs_img_data)
        CTkButton(master=self.scrollable_frame, image=inputs_img, text="System Inputs",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: switch_frame(self.scrollable_frame2)).pack(anchor="w", ipady=5, pady=(16, 0))

        units_img_data = Image.open("Main_Page_Class_Template\\units.png")
        units_img = CTkImage(dark_image=units_img_data,
                             light_image=units_img_data)
        CTkButton(master=self.scrollable_frame, image=units_img, text="Units Data",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        employees_img_data = Image.open(
            "Main_Page_Class_Template\employees.png")
        employees_img = CTkImage(
            dark_image=employees_img_data, light_image=employees_img_data)
        CTkButton(master=self.scrollable_frame, image=employees_img, text="Employees Data",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322",
                  anchor="w", command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        users_img_data = Image.open("Main_Page_Class_Template\\users.png")
        users_img = CTkImage(dark_image=users_img_data,
                             light_image=users_img_data)
        CTkButton(master=self.scrollable_frame, image=users_img, text="Users Data",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        inventory_img_data = Image.open(
            "Main_Page_Class_Template\inventory.png")
        inventory_img = CTkImage(
            dark_image=inventory_img_data, light_image=inventory_img_data)
        CTkButton(master=self.scrollable_frame, image=inventory_img, text="Inventory Data",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        transactions_img_data = Image.open(
            "Main_Page_Class_Template\\transactions.png")
        transactions_img = CTkImage(
            dark_image=transactions_img_data, light_image=transactions_img_data)
        CTkButton(master=self.scrollable_frame, image=transactions_img, text="Transactions",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        timesheet_img_data = Image.open(
            "Main_Page_Class_Template\\timesheet.png")
        timesheet_img = CTkImage(
            dark_image=timesheet_img_data, light_image=timesheet_img_data)
        CTkButton(master=self.scrollable_frame, image=timesheet_img, text="Time Sheet",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        expenses_img_data = Image.open("Main_Page_Class_Template\expenses.png")
        expenses_img = CTkImage(
            dark_image=expenses_img_data, light_image=expenses_img_data)
        CTkButton(master=self.scrollable_frame, image=expenses_img, text="Expenses",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        revenues_img_data = Image.open(
            "Main_Page_Class_Template\\revenues.png")
        revenues_img = CTkImage(
            dark_image=revenues_img_data, light_image=revenues_img_data)
        CTkButton(master=self.scrollable_frame, image=revenues_img, text="Revenues",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        cash_img_data = Image.open("Main_Page_Class_Template\\cash.png")
        cash_img = CTkImage(dark_image=cash_img_data,
                            light_image=cash_img_data)
        CTkButton(master=self.scrollable_frame, image=cash_img, text="Cash Data",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        reports_img_data = Image.open("Main_Page_Class_Template\\reports.png")
        reports_img = CTkImage(dark_image=reports_img_data,
                               light_image=reports_img_data)
        CTkButton(master=self.scrollable_frame, image=reports_img,
                  text="System Reports",
                  fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w",
                  command=lambda: print('button pressed')).pack(anchor="w", ipady=5, pady=(16, 0))

        account_img_data = Image.open("Main_Page_Class_Template\\account.png")
        account_img = CTkImage(dark_image=account_img_data,
                               light_image=account_img_data)
        CTkButton(master=self.sidebar_frame, image=account_img, text="Switch Account", fg_color="transparent",
                  font=("Arial Bold", 14), hover_color="#EE9322", anchor="w").pack(anchor="w", ipady=5, pady=(20, 0))
        # Add other buttons and widgets in the sidebar

        # Set scorllable frame on main frame
        self.scrollable_frame = CTkScrollableFrame(self.main_frame, fg_color="#040D12", width=400, height=390,
                                                   scrollbar_button_color="#EE9322", scrollbar_button_hover_color="#219C90",
                                                   border_color="#EE9250", border_width=0.6, corner_radius=5)
        self.scrollable_frame.pack(fill="both", pady=15, anchor="center")
        self.scrollable_frame.pack_propagate(True)

        configuration_img_data = Image.open(
            "Main_Page_Class_Template\\configuration.png")
        configuration_img = CTkImage(
            dark_image=configuration_img_data, light_image=configuration_img_data, size=(50, 50))
        configuration_button = CTkButton(master=self.scrollable_frame, image=configuration_img,
                                         text="Configurations Screen",
                                         fg_color="transparent",
                                         font=("Arial Bold", 14), hover_color="#EE9322", anchor="center", border_color="#fff",
                                         border_spacing=4, border_width=1,
                                         command=lambda: print('Configurations button pressed'))

        changepassword_img_data = Image.open(
            "Main_Page_Class_Template\\changepassword.png")
        changepassword_img = CTkImage(
            dark_image=changepassword_img_data, light_image=changepassword_img_data, size=(50, 50))
        changepassword_button = CTkButton(master=self.scrollable_frame, image=changepassword_img,
                                          text="Change Password Screen",
                                          fg_color="transparent",
                                          font=("Arial Bold", 14), hover_color="#EE9322", anchor="center", border_color="#fff",
                                          border_spacing=4, border_width=1,
                                          command=lambda: print('Change Password button pressed'))

        # Set scorllable frame on main frame
        self.scrollable_frame2 = CTkScrollableFrame(self.main_frame, fg_color="#040D12", width=400, height=390,
                                                    scrollbar_button_color="#EE9322", scrollbar_button_hover_color="#219C90",
                                                    border_color="#EE9250", border_width=0.6, corner_radius=5,)
        self.scrollable_frame2.pack(fill="both", pady=15, anchor="center")
        self.scrollable_frame2.pack_propagate(True)

        configuration_img_data2 = Image.open(
            "Main_Page_Class_Template\\configuration.png")
        configuration_img2 = CTkImage(
            dark_image=configuration_img_data2, light_image=configuration_img_data2, size=(50, 50))
        configuration_button2 = CTkButton(master=self.scrollable_frame, image=configuration_img2,
                                          text="Configurations2 Screen",
                                          fg_color="transparent",
                                          font=("Arial Bold", 14), hover_color="#EE9322", anchor="center", border_color="#fff",
                                          border_spacing=4, border_width=1,
                                          command=lambda: print('Configurations button pressed'))

        changepassword_img_data2 = Image.open(
            "Main_Page_Class_Template\\changepassword.png")
        changepassword_img2 = CTkImage(
            dark_image=changepassword_img_data2, light_image=changepassword_img_data2, size=(50, 50))
        changepassword_button2 = CTkButton(master=self.scrollable_frame, image=changepassword_img2,
                                           text="Change Password2 Screen",
                                           fg_color="transparent",
                                           font=("Arial Bold", 14), hover_color="#EE9322", anchor="center", border_color="#fff",
                                           border_spacing=4, border_width=1,
                                           command=lambda: print('Change Password button pressed'))

        # Use the grid geometry manager to position the buttons
        configuration_button.grid(
            row=0, column=1, padx=10, pady=10, sticky="e")
        changepassword_button.grid(
            row=0, column=2, padx=10, pady=10, sticky="w")
        configuration_button2.grid(
            row=0, column=1, padx=10, pady=10, sticky="e")
        changepassword_button2.grid(
            row=0, column=2, padx=10, pady=10, sticky="w")
        # Function to switch between frames

        def switch_frame(frame_to_show):
            # Hide all frames
            self.scrollable_frame.pack_forget()
            self.scrollable_frame2.pack_forget()

        # Show the selected frame
            frame_to_show.pack(fill="both")

    def run(self):
        self.main_page.mainloop()
