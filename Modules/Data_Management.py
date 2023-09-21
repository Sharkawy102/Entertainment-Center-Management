
from tkinter import *
import tkinter.messagebox
import stdDatabase_backend


class student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student DataBase Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        stdID = StringVar()
        firstName = StringVar()
        surName = StringVar()
        BoD = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # ===================================function===========================
        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Student DataBase Management System", "Confirm if you need to Exit?")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtSurna.delete(0, END)
            self.txtBOD.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddres.delete(0, END)
            self.txtmob.delete(0, END)

        def addData():
            stdDatabase_backend.studentDta()
            if len(stdID.get()) != 0:
                stdDatabase_backend.addStdRec(stdID.get(), firstName.get(), surName.get(),
                                              BoD.get(), Age.get(),  Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, stdID.get(), firstName.get(), surName.get(),
                                   BoD.get(), Age.get(),  Gender.get(), Address.get(), Mobile.get())

        def displayData():
            studentList.delete(0, END)
            for row in stdDatabase_backend.viewData():
                studentList.insert(END, row, str(" "))

        def studentRec(event):
            global sd
            searchStd = studentList.curselection()[0]
            sd = studentList.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[2])
            self.txtSurna.delete(0, END)
            self.txtSurna.insert(END, sd[3])
            self.txtBOD.delete(0, END)
            self.txtBOD.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAddres.delete(0, END)
            self.txtAddres.insert(END, sd[7])
            self.txtmob.delete(0, END)
            self.txtmob.insert(END, sd[8])

        def deleteData():
            if len(stdID.get()) != 0:
                stdDatabase_backend.deleteRec(sd[0])
                clearData()
                displayData()

        def searchData():
            studentList.delete(0, END)
            for row in stdDatabase_backend.serchData(stdID.get(), firstName.get(), surName.get(),
                                                     BoD.get(), Age.get(),  Gender.get(), Address.get(), Mobile.get()):
                studentList.insert(END, row, str(" "))

        def updateData():
            if len(stdID.get()) != 0:
                stdDatabase_backend.deleteRec(sd[0])
            if len(stdID.get()) != 0:
                stdDatabase_backend.addStdRec(stdID.get(), firstName.get(), surName.get(),
                                              BoD.get(), Age.get(),  Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, stdID.get(), firstName.get(), surName.get(),
                                   BoD.get(), Age.get(),  Gender.get(), Address.get(), Mobile.get())
        # ===================================Frame===========================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        titFrame = Frame(MainFrame, bd=2, padx=54, pady=8,
                         bg="Ghost White", relief=RIDGE)
        titFrame.pack(side=TOP)

        self.lblTit = Label(titFrame, font=('arial', 36, 'bold'),
                            text="Student DataBase Management System", bg="Ghost White")
        self.lblTit.grid()

        buttonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10,
                            bg="Ghost White", relief=RIDGE)
        buttonFrame.pack(side=BOTTOM)

        dataFrame = Frame(MainFrame, bd=1, width=1300, height=350, padx=20, pady=20,
                          bg="cadet blue", relief=RIDGE)
        dataFrame.pack(side=BOTTOM)

        dataFrameLeft = LabelFrame(dataFrame, bd=1, width=1000, height=600, padx=20,
                                   bg="Ghost White", relief=RIDGE, font=('arial', 20, 'bold'), text="student info\n")
        dataFrameLeft.pack(side=LEFT)

        dataFrameRight = LabelFrame(dataFrame, bd=1, width=450, height=300, padx=40, pady=3,
                                    bg="Ghost White", relief=RIDGE, font=('arial', 20, 'bold'), text="student details\n")
        dataFrameRight.pack(side=RIGHT)
        # ===================================LBL & Entry===========================
        self.lblStdID = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                              text="Student ID", padx=2, pady=8, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                              textvariable=stdID, width=39)
        self.txtStdID.grid(row=0, column=1)
        self.lblFna = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                            text="First Name", padx=2, pady=8, bg="Ghost White")
        self.lblFna.grid(row=1, column=0, sticky=W)
        self.txtFna = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                            textvariable=firstName, width=39)
        self.txtFna.grid(row=1, column=1)
        self.lblSurna = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                              text="Sur Name", padx=2, pady=8, bg="Ghost White")
        self.lblSurna.grid(row=2, column=0, sticky=W)
        self.txtSurna = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                              textvariable=surName, width=39)
        self.txtSurna.grid(row=2, column=1)
        self.lblBOD = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                            text="Birth of Date", padx=2, pady=8, bg="Ghost White")
        self.lblBOD.grid(row=3, column=0, sticky=W)
        self.txtBOD = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                            textvariable=BoD, width=39)
        self.txtBOD.grid(row=3, column=1)

        self.lblAge = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                            text="Age", padx=2, pady=8, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                            textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                               text="Gender", padx=2, pady=8, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                               textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)
        self.lblAddres = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                               text="Address", padx=2, pady=8, bg="Ghost White")
        self.lblAddres.grid(row=6, column=0, sticky=W)
        self.txtAddres = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                               textvariable=Address, width=39)
        self.txtAddres.grid(row=6, column=1)
        self.lblmob = Label(dataFrameLeft, font=('arial', 20, 'bold'),
                            text="Student Mobile", padx=2, pady=8, bg="Ghost White")
        self.lblmob.grid(row=7, column=0, sticky=W)
        self.txtmob = Entry(dataFrameLeft, font=('arial', 20, 'bold'),
                            textvariable=Mobile, width=39)
        self.txtmob.grid(row=7, column=1)
        # ===================================Scroll bar===========================
        scrollBarr = Scrollbar(dataFrameRight)
        scrollBarr.grid(row=0, column=1, sticky='ns')

        studentList = Listbox(dataFrameRight, width=41,
                              height=14, font=('arial', 12, 'bold'), yscrollcommand=scrollBarr.set)
        studentList.bind('<<ListboxSelect>>', studentRec)
        studentList.grid(row=0, column=0, padx=8)
        scrollBarr.config(command=studentList.yview)
        # ===================================Button Widget===========================
        self.btnAddDate = Button(buttonFrame, text="Add New", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddDate.grid(row=0, column=0)
        self.btnDisplayDate = Button(buttonFrame, text="Display", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=displayData)
        self.btnDisplayDate.grid(row=0, column=1)
        self.btnClearDate = Button(buttonFrame, text="Clear", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnClearDate.grid(row=0, column=2)
        self.btnDeleteDate = Button(buttonFrame, text="Delete", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=deleteData)
        self.btnDeleteDate.grid(row=0, column=3)
        self.btnSearchDate = Button(buttonFrame, text="Search", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=searchData)
        self.btnSearchDate.grid(row=0, column=4)
        self.btnUpdateDate = Button(buttonFrame, text="Update", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=updateData)
        self.btnUpdateDate.grid(row=0, column=5)
        self.btnExit = Button(buttonFrame, text="Exit", font=(
            'arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)


# This code block will only run if this script is executed as the main program
if __name__ == '__main__':
    root = Tk()
    application = student(root)
    root.mainloop()
    # Code to be executed when the script is run directly
