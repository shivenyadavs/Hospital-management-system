from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")




        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.medicine = StringVar()
        self.PatientId = StringVar()
        self.nhsno = StringVar()
        self.PatientName = StringVar()
        self.dob = StringVar()
        self.PatientAddress = StringVar()


        lbltitle = Label(
            self.root,
            bd=0,
            relief=RIDGE,
            text="Hospital Management System",
            fg="white",
            bg="#007acc",  # Blue background for the title
            font=("Helvetica", 48, "bold")  # Changed to Helvetica for modern feel
        )
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe styling
        dataframe = Frame(self.root, bd=15, relief=RIDGE, bg="#f4f4f9")  # Light grey background
        dataframe.place(x=0, y=100, width=1360, height=410)

        dataframeLeft = LabelFrame(
            dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("Helvetica", 16, "bold"),
            bg="#e8f0fe",  # Light blue background for left frame
            fg="#333333",  # Dark text for contrast
            text="Patient Information"
        )
        dataframeLeft.place(x=0, y=4, width=880, height=340)

        dataframeRight = LabelFrame(
            dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("Helvetica", 16, "bold"),
            bg="#e8f0fe",  # Light blue background for right frame
            fg="#333333",  # Dark text for contrast
            text="Prescription"
        )
        dataframeRight.place(x=990, y=4, width=320, height=340)

        # Button frame styling
        bframe = Frame(self.root, bd=15, relief=RIDGE, bg="#f4f4f9")  # Light grey background
        bframe.place(x=0, y=440, width=1360, height=50)

        # Details frame styling
        detailsframe = Frame(self.root, bd=15, relief=RIDGE, bg="#ffffff")  # White background for details
        detailsframe.place(x=0, y=495, width=1360, height=160)



        # ========================dataframeLeft=====================================
        lblNameTablet = Label(dataframeLeft, text="Names Of Tablet", font=("times new roman",12,"bold"),padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0,sticky=W)



        comNametablet = ttk.Combobox(dataframeLeft, state="readonly", font=("times new roman", 12, "bold"),
                             width=33, textvariable=self.Nameoftablets)
        comNametablet["values"] = ("Nice", "corona vaccine", "Acetaminophen", "Addrell", "amlodipine", "ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(dataframeLeft, font=("arial", 12, "bold"), text="Reference no:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.ref)
        txtref.grid(row=1, column=1)

        lblDose = Label(dataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(dataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.NumberofTablets)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(dataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.Lot)
        txtLot.grid(row=4, column=1)

        lblissuedate = Label(dataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissuedate.grid(row=5, column=0, sticky=W)
        txtissuedate = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.Issuedate)
        txtissuedate.grid(row=5, column=1)

        lblexpdate = Label(dataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblexpdate.grid(row=6, column=0, sticky=W)
        txtexpdate = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.ExpDate)
        txtexpdate.grid(row=6, column=1)

        lbldailydose = Label(dataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lbldailydose.grid(row=7, column=0, sticky=W)
        txtdailydose = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.DailyDose)
        txtdailydose.grid(row=7, column=1)

        lblsideEffect = Label(dataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblsideEffect.grid(row=8, column=0, sticky=W)
        txtsideEffect = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.sideEffect)
        txtsideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(dataframeLeft, font=("arial", 12, "bold"), text="Further Info:", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.FurtherInformation)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodpress = Label(dataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodpress.grid(row=1, column=2, sticky=W)
        txtBloodpress = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.StorageAdvice)
        txtBloodpress.grid(row=1, column=3)

        lblstorage = Label(dataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblstorage.grid(row=2, column=2, sticky=W)
        txtstorage = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.StorageAdvice)
        txtstorage.grid(row=2, column=3)

        lblmedicine = Label(dataframeLeft, font=("arial", 12, "bold"), text="Medicine:", padx=2, pady=6)
        lblmedicine.grid(row=3, column=2, sticky=W)
        txtmedicine = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.medicine)
        txtmedicine.grid(row=3, column=3)

        lblpatientid = Label(dataframeLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=6)
        lblpatientid.grid(row=4, column=2, sticky=W)
        txtpatientid = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.PatientId)
        txtpatientid.grid(row=4, column=3)

        lblnhsno = Label(dataframeLeft, font=("arial", 12, "bold"), text="NHS No:", padx=2, pady=6)
        lblnhsno.grid(row=5, column=2, sticky=W)
        txtnhsno = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.nhsno)
        txtnhsno.grid(row=5, column=3)

        lblpatientname = Label(dataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblpatientname.grid(row=6, column=2, sticky=W)
        txtpatientname = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.PatientName)
        txtpatientname.grid(row=6, column=3)

        lbldob = Label(dataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lbldob.grid(row=7, column=2, sticky=W)
        txtdob = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.dob)
        txtdob.grid(row=7, column=3)

        lblpatientadd = Label(dataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblpatientadd.grid(row=8, column=2, sticky=W)
        txtpatientadd = Entry(dataframeLeft, font=("arial", 13, "bold"), width=30, textvariable=self.PatientAddress)
        txtpatientadd.grid(row=8, column=3)


        self.txtprescription=Text(dataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)
# =============================buttons=======================
        btnprescription=Button(bframe,text="prescription",bg="green",fg="white",font=("arial",12,"bold"),width=19,padx=2,pady=6,command=self.fetch_data) 
        btnprescription.grid(row=0,column=0)


        btnprescriptiondata = Button(bframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=19, padx=2, pady=6, command=self.iPrescriptionData)
        btnprescriptiondata.grid(row=0, column=1)


        btnupdate = Button(bframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=19, padx=2, pady=6, command=self.update)
        btnupdate.grid(row=0, column=2)


        btndelete=Button(bframe,text="delete",bg="green",fg="white",font=("arial",12,"bold"),width=19,padx=2,pady=6, command=self.delete) 
        btndelete.grid(row=0,column=3)

        btnclear=Button(bframe,text="clear",bg="green",fg="white",font=("arial",12,"bold"),width=19,padx=2,pady=6,command=self.clear)
        btnclear.grid(row=0,column=4)

        btnexit=Button(bframe,text="exit",bg="green",fg="white",font=("arial",12,"bold"),width=19,padx=2,pady=6,command=self.exit_app) 
        btnexit.grid(row=0,column=5)
        
        # =========================table===============================
        
        # =========================scrollbar===========================

        # =========================table===============================
        
        # Scrollbars
        scroll_x = ttk.Scrollbar(detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe, orient=VERTICAL)

        # Treeview
        self.hospital = ttk.Treeview(
            detailsframe,
            columns=("nameoftable", "ref", "dose", "nooftables", "lot", "issuedate", "expdate",
                    "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        # Configure scrollbar commands AFTER the Treeview is defined
        scroll_x.config(command=self.hospital.xview)
        scroll_y.config(command=self.hospital.yview)

        # Pack scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure Treeview headings
        self.hospital.heading("nameoftable", text="Name Of Tablets")
        self.hospital.heading("ref", text="Reference No.")
        self.hospital.heading("dose", text="Dose")
        self.hospital.heading("nooftables", text="No Of Tablets")
        self.hospital.heading("lot", text="Lot")
        self.hospital.heading("issuedate", text="Issue Date")
        self.hospital.heading("expdate", text="Exp Date")
        self.hospital.heading("dailydose", text="Daily Dose")
        self.hospital.heading("storage", text="Storage")
        self.hospital.heading("nhsnumber", text="NHS Number")
        self.hospital.heading("pname", text="Patient Name")
        self.hospital.heading("dob", text="DOB")
        self.hospital.heading("address", text="Address")

        # Show only headings
        self.hospital["show"] = "headings"

        # Pack the Treeview
        self.hospital.pack(fill=BOTH, expand=1)

        # Set column widths
        columns = ("nameoftable", "ref", "dose", "nooftables", "lot", "issuedate", "expdate",
                "dailydose", "storage", "nhsnumber", "pname", "dob", "address")

        for col in columns:
            self.hospital.column(col, width=90)  # You can adjust the width as per your preference


        self.hospital.bind("<ButtonRelease-1>", self.get_cursor)

    # = Functinality Declration=:
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="shiven", password="root", database="mydata"
                )
                my_cursor = conn.cursor()

                # Insert data into the hospital table
                query = """INSERT INTO hospital (nameoftablets, ref, dose, nooftablets, lot, issuedate,
                                                expdate, dailydose, storage, nhsnumber, pname, dob, address)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsno.get(),
                    self.PatientName.get(),
                    self.dob.get(),
                    self.PatientAddress.get(),
                )
                my_cursor.execute(query, values)
                conn.commit()

                # Now fetch data from the database to populate the Treeview
                my_cursor.execute("SELECT * FROM hospital")
                rows = my_cursor.fetchall()

                # Clear the Treeview before inserting new data
                self.hospital.delete(*self.hospital.get_children())

                # Insert the fetched data into the Treeview
                for row in rows:
                    self.hospital.insert("", "end", values=row)

                conn.close()
                messagebox.showinfo("Success", "Data Inserted and Treeview Updated")

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")


    def update(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="shiven",
                    password="root",
                    database="mydata"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE hospital SET Nameoftablets=%s, Dose=%s, NumberofTablets=%s, Lot=%s, Issuedate=%s, ExpDate=%s, DailyDose=%s, StorageAdvice=%s, nhsno=%s, PatientName=%s, dob=%s, PatientAddress=%s WHERE ref=%s",
                    (
                        self.Nameoftablets.get(),
                        self.Dose.get(),
                        self.NumberofTablets.get(),
                        self.Lot.get(),
                        self.Issuedate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.StorageAdvice.get(),
                        self.nhsno.get(),
                        self.PatientName.get(),
                        self.dob.get(),
                        self.PatientAddress.get(),
                        self.ref.get(),  # Unique Reference No
                    )
                )
                conn.commit()
                self.fetch_data()  # Refresh Treeview
                conn.close()
                messagebox.showinfo("Success", "Record has been updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {e}")




    def fetch_data(self):
        # Clear the Treeview before inserting new data
        for row in self.hospital.get_children():
            self.hospital.delete(row)
        
        # Connect to the database
        conn = mysql.connector.connect(host="localhost", username="shiven", password="root", database="mydata")
        my_cursor = conn.cursor()
        
        # Execute query to fetch all records
        my_cursor.execute("SELECT * FROM hospital")
        
        # Fetch all rows
        rows = my_cursor.fetchall()
        
        # Insert data into the Treeview
        for row in rows:
            self.hospital.insert("", "end", values=row)
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Data Fetch", "Data fetched successfully")

    # Fetch data from the database and insert into the Treeview
    def get_cursor(self, event=""):
        cursor_row = self.hospital.focus()  # Get the currently selected row in the Treeview
        contents = self.hospital.item(cursor_row)  # Retrieve data from the selected row
        row = contents['values']  # Extract row values as a list

        if row:  # Ensure the row is not empty
            self.Nameoftablets.set(row[0])  # Name of Tablets
            self.ref.set(row[1])  # Reference No
            self.Dose.set(row[2])  # Dose
            self.NumberofTablets.set(row[3])  # Number of Tablets
            self.Lot.set(row[4])  # Lot
            self.Issuedate.set(row[5])  # Issue Date
            self.ExpDate.set(row[6])  # Expiry Date
            self.DailyDose.set(row[7])  # Daily Dose
            self.StorageAdvice.set(row[8])  # Storage Advice
            self.nhsno.set(row[9])  # NHS Number
            self.PatientName.set(row[10])  # Patient Name
            self.dob.set(row[11])  # DOB
            self.PatientAddress.set(row[12])  # Address


    def delete(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="shiven",
                    password="root",
                    database="mydata"
                )
                my_cursor = conn.cursor()
                sql_query = "DELETE FROM hospital WHERE ref=%s"
                value = (self.ref.get(),)
                my_cursor.execute(sql_query, value)
                conn.commit()
                conn.close()

                self.fetch_data()  # Refresh the Treeview
                self.clear()  # Clear the form fields
                messagebox.showinfo("Success", "Record has been deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {e}")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsno.set("")
        self.PatientName.set("")
        self.dob.set("")
        self.PatientAddress.set("")


    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.root.destroy()  # Closes the application window


root=Tk()
ob=hospital(root)
root.mainloop()