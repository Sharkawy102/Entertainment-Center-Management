from customtkinter import *
owner_title = ('E.C.O.M')


class EmployeeWindow:
    def __init__(self):
        print("EmployeeWindow constructor")
        set_appearance_mode("Dark")
        # set_default_color_theme('theme.JSON')
        set_widget_scaling(1.0)
        set_window_scaling(1.0)

        # Initiate window
        self.EmployeeWindow = CTk()

        # Get the screen width and height
        screen_width = self.EmployeeWindow.winfo_screenwidth()
        screen_height = self.EmployeeWindow.winfo_screenheight()

        # Set the window's dimensions
        window_width = 600
        window_height = 480

        # Calculate the x and y coordinates for the window to be centered
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window's position  responsively to be centered on screen according to size
        self.EmployeeWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set the window title & resize
        self.EmployeeWindow.title(f'{owner_title} -Employee Page')
        self.EmployeeWindow.resizable(False, False)

    def run(self):
        self.EmployeeWindow.mainloop()



if __name__ == "__main__":
    login_page = EmployeeWindow()
    login_page.run()