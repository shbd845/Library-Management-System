from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry('1920x1080+0+0')
        labeltitle=Label(self.root,text="Library Management System",bg="#5CDBE0",fg="black",bd=20,relief=RAISED,font=("Arial Bold",50),cursor="pirate")
        labeltitle.pack(side=TOP,fill=X)
        frame=Frame(self.root,bg="#5CDBE0",bd=0,relief=RIDGE,width=1920,height=550,cursor="arrow")
        frame.pack()


        # ====================================Variables==================================
        self.type=StringVar()
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.regnumber=StringVar()
        self.add=StringVar()
        self.branch=StringVar()
        self.year=StringVar()
        self.bookid=StringVar()
        self.bookname=StringVar()
        self.bdate=StringVar()
        self.ddate=StringVar()
        self.fee=StringVar()
        self.price=StringVar()
        self.rdate=StringVar()


        # ===================================DataFrameLeft===============================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",font=("Ubuntu",20),bg="#5CDBE0",fg="#1D644D",bd=10,relief=RIDGE,labelanchor='n')
        DataFrameLeft.place(width=1000,height=540,bordermode=INSIDE,y=10)

        lblMember=Label(DataFrameLeft,text="Member Type:",bg="#5CDBE0",font=("Arial Bold",15))
        lblMember.grid(column=0,row=0,padx=0,pady=20,sticky=W)

        membertype=ttk.Combobox(DataFrameLeft,state="readonly",width=20,textvariable=self.type)
        membertype["values"]=("Student","Lecturer","Admin Staff")
        membertype.grid(column=1,row=0)

        lblfirstname=Label(DataFrameLeft,text="First Name:",bg="#5CDBE0",font=("Arial Bold",15))
        lblfirstname.grid(column=0,row=1,sticky=W)

        textfirstname=Entry(DataFrameLeft,width=20,textvariable=self.firstname)
        textfirstname.grid(column=1,row=1,padx=10,pady=20)

        lbllastname=Label(DataFrameLeft,text="Last Name:",bg="#5CDBE0",font=("Arial Bold",15))
        lbllastname.grid(column=0,row=2,sticky=W)

        textlastname=Entry(DataFrameLeft,width=20,textvariable=self.lastname)
        textlastname.grid(column=1,row=2,padx=10,pady=20)

        lblRegistno=Label(DataFrameLeft,text="Registration Number:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200,justify=LEFT)
        lblRegistno.grid(column=0,row=3,sticky=W)

        regno=Entry(DataFrameLeft,width=20,textvariable=self.regnumber)
        regno.grid(column=1,row=3,padx=10,pady=20)


        lblAddress=Label(DataFrameLeft,text="Address:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200)
        lblAddress.grid(column=0,row=4,sticky=W)

        textadd=Entry(DataFrameLeft,width=20,textvariable=self.add)
        textadd.grid(column=1,row=4,padx=10,pady=20)   
             
        lblBranch=Label(DataFrameLeft,text="Branch:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200)
        lblBranch.grid(column=0,row=5,sticky=W)

        txtBranch=Entry(DataFrameLeft,width=20,textvariable=self.branch)
        txtBranch.grid(column=1,row=5,padx=10,pady=20)

        lblYear=Label(DataFrameLeft,text="Admission Year:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200)
        lblYear.grid(column=0,row=6,sticky=W)

        txtYear=Entry(DataFrameLeft,width=20,textvariable=self.year)
        txtYear.grid(column=1,row=6,padx=10,pady=20)

        lblBookId=Label(DataFrameLeft,text="Book ID:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200)
        lblBookId.grid(column=2,row=0,padx=50,sticky=W)

        txtBookId=Entry(DataFrameLeft,width=20,textvariable=self.bookid)
        txtBookId.grid(column=3,row=0,padx=0,pady=20)   

        lblBookTitle=Label(DataFrameLeft,text="Book Title:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200)
        lblBookTitle.grid(column=2,row=1,padx=50,sticky=W)

        txtBookName=Entry(DataFrameLeft,width=20,textvariable=self.bookname)
        txtBookName.grid(column=3,row=1,padx=0,pady=20)

        lblDateB=Label(DataFrameLeft,text="Borrowing Date:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200,justify=LEFT)
        lblDateB.grid(column=2,row=2,padx=50,sticky=W)

        txtBorrowDate=Entry(DataFrameLeft,width=20,textvariable=self.bdate)
        txtBorrowDate.grid(column=3,row=2,padx=0,pady=20)  

        lblDuedate=Label(DataFrameLeft,text="Due Date:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200,justify=LEFT)
        lblDuedate.grid(column=2,row=3,padx=50,sticky=W)

        txtdueDate=Entry(DataFrameLeft,width=20,textvariable=self.ddate)
        txtdueDate.grid(column=3,row=3,padx=0,pady=20)  

        lblFee=Label(DataFrameLeft,text="Late Return Fee:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200,justify=LEFT)
        lblFee.grid(column=2,row=4,padx=50,sticky=W)

        txtFee=Entry(DataFrameLeft,width=20,textvariable=self.fee)
        txtFee.grid(column=3,row=4,padx=0,pady=20)     

        lblPrice=Label(DataFrameLeft,text="Book MRP:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200,justify=LEFT)
        lblPrice.grid(column=2,row=5,padx=50,sticky=W)

        txtPrice=Entry(DataFrameLeft,width=20,textvariable=self.price)
        txtPrice.grid(column=3,row=5,padx=0,pady=20) 

        lblRDate=Label(DataFrameLeft,text="Return Date:",bg="#5CDBE0",font=("Arial Bold",15),wraplength=200,justify=LEFT)
        lblRDate.grid(column=2,row=6,padx=50,sticky=W)

        txtRDate=Entry(DataFrameLeft,width=20,textvariable=self.rdate)
        txtRDate.grid(column=3,row=6,padx=0,pady=20) 


        # ===================================DataFrameRight===============================
        DataFrameRight=LabelFrame(frame,text="Book Details",font=("Ubuntu",20),bg="#5CDBE0",fg="#1D644D",bd=10,relief=RIDGE,labelanchor='n')
        DataFrameRight.place(width=960,height=540,bordermode=INSIDE,x=960,y=10)

        listScrollBarY=Scrollbar(DataFrameRight,width=20,elementborderwidth=2,activebackground="yellow",bg="light green",bd=10,relief=RIDGE)
        listScrollBarY.grid(column=1,row=0,sticky='ns',pady=10,padx=5)   


        def SelectBook(event):
            value=str(listbox.get(listbox.curselection()))
            x=value

            if(x=="Design of Elevated Water Tanks"):
                self.bookid.set("BK74851")
                self.bookname.set("Design of Elevated Water Tanks")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1050")
            
            elif(x=="Asphalt Materials Science and Technology"):
                self.bookid.set("LB52851")
                self.bookname.set("Asphalt Materials Science and Technology")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.3450")
            
            elif(x=="Construction Daily Report Free Excel Template"):
                self.bookid.set("BF54791")
                self.bookname.set("Construction Daily Report Free Excel Template")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.3250")
            
            elif(x=="Excel Construction Management Request for Information Log Template"):
                self.bookid.set("BQ16221")
                self.bookname.set("Excel Construction Management Request for Information Log Template")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.2540")
            
            elif(x=="Construction Estimator Free Excel Template"):
                self.bookid.set("BY48851")
                self.bookname.set("Construction Estimator Free Excel Template")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1650")
            
            elif(x=="A Textbook of Fluid Mechanics and Hydraulic Machines"):
                self.bookid.set("BK54861")
                self.bookname.set("A Textbook of Fluid Mechanics and Hydraulic Machines")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.7850")
            
            elif(x=="A Textbook of Machine Design"):
                self.bookid.set("BK78412")
                self.bookname.set("A Textbook of Machine Design")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1860")
            
            elif(x=="Theory of Machines"):
                self.bookid.set("BK98524")
                self.bookname.set("Theory of Machines")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.700")
            
            elif(x=="An Introduction to Mechanics"):
                self.bookid.set("BK02145")
                self.bookname.set("An Introduction to Mechanics")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.4500")
            
            elif(x=="Mechanical Vibrations"):
                self.bookid.set("BK84521")
                self.bookname.set("Mechanical Vibrations")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1210")
            
            elif(x=="Basic & Applied Thermodynamics"):
                self.bookid.set("BI548621")
                self.bookname.set("Basic & Applied Thermodynamics")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.2145")

            elif(x=="Engineering Mechanics"):
                self.bookid.set("BK74851")
                self.bookname.set("Engineering Mechanics")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1050")

            elif(x=="Design of Machine Elements"):
                self.bookid.set("BK74851")
                self.bookname.set("Design of Machine Elements")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1050")

            elif(x=="Fluid Mechanics"):
                self.bookid.set("BK74851")
                self.bookname.set("Fluid Mechanics")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1050")

            elif(x=="Fundamentals of Thermodynamics"):
                self.bookid.set("BK74851")
                self.bookname.set("Fundamentals of Thermodynamics")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1050")

            elif(x=="Steel Stair Design Based on AISC"):
                self.bookid.set("BK74851")
                self.bookname.set("Steel Stair Design Based on AISC")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fee.set("Rs.50")
                self.price.set("Rs.1050")

        listbox=Listbox(DataFrameRight,width=30,height=15,justify=LEFT,font=("New Times Roman",15),selectmode=SINGLE,yscrollcommand=listScrollBarY.set,relief=RAISED,bd=10,bg="#F8D6F3")
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(column=0,row=0,padx=5,pady=5)
        BookNames=["Design of Elevated Water Tanks","Asphalt Materials Science and Technology","Construction Daily Report Free Excel Template","Excel Construction Management Request for Information Log Template","Construction Estimator Free Excel Template","Steel Stair Design Based on AISC","A Textbook of Fluid Mechanics and Hydraulic Machines","A Textbook of Machine Design","Theory of Machines","An Introduction to Mechanics","Theory of Machines","Mechanical Vibrations","Basic & Applied Thermodynamics","Engineering Mechanics","Design of Machine Elements","Fluid Mechanics","Fundamentals of Thermodynamics"]
        for i in BookNames:
            listbox.insert(END,i)
        listScrollBarY.config(command=listbox.yview)

        self.txtbox=Text(DataFrameRight,padx=10,pady=10,width=33,height=22,relief=RAISED,bd=10)
        self.txtbox.grid(column=2,row=0)
      
           



        # ===================================Buttons Frame===============================
        Buttonframe=Frame(self.root,bg="#5CDBE0",bd=10,relief=RIDGE,width=1920,cursor="arrow")
        Buttonframe.place(y=680,height=90)

        bttAdd=Button(Buttonframe,command=self.AddData,bg="#A1CB6E",activebackground="#3976D7",activeforeground="#FFF300",text="ADD DATA",font=("Ubuntu",10,"bold"),height=2,width=32,bd=10,relief=RAISED,padx=2,pady=2)
        bttAdd.grid(column=0,row=0)

        bttDelete=Button(Buttonframe,command=self.Delete,bg="#A1CB6E",activebackground="#3976D7",activeforeground="#FFF300",text="DELETE",font=("Ubuntu",10,"bold"),height=2,width=32,bd=10,relief=RAISED,padx=2,pady=2)
        bttDelete.grid(column=1,row=0)


        bttShow=Button(Buttonframe,command=self.show_data,bg="#A1CB6E",activebackground="#3976D7",activeforeground="#FFF300",text="SHOW DATA",font=("Ubuntu",10,"bold"),height=2,width=32,bd=10,relief=RAISED,padx=2,pady=2)
        bttShow.grid(column=2,row=0)

        bttReset=Button(Buttonframe,command=self.reset,bg="#A1CB6E",activebackground="#3976D7",activeforeground="#FFF300",text="RESET",font=("Ubuntu",10,"bold"),height=2,width=32,bd=10,relief=RAISED,padx=2,pady=2)
        bttReset.grid(column=3,row=0)

        bttUpdate=Button(Buttonframe,command=self.update,bg="#A1CB6E",activebackground="#3976D7",activeforeground="#FFF300",text="UPDATE",font=("Ubuntu",10,"bold"),height=2,width=32,bd=10,relief=RAISED,padx=2,pady=2)
        bttUpdate.grid(column=4,row=0)

        bttExit=Button(Buttonframe,command=self.exit,bg="#A1CB6E",activebackground="#3976D7",activeforeground="#FFF300",text="EXIT",font=("Ubuntu",10,"bold"),height=2,width=32,bd=10,relief=RAISED,padx=2,pady=2)
        bttExit.grid(column=5,row=0)


        # ===================================DataBase Frame===============================
        databaseframe=Frame(self.root,bg="#5CDBE0",bd=10,relief=RIDGE,width=1920,cursor="arrow")
        databaseframe.place(y=770,height=245)
        
        TableFrame=Frame(databaseframe)
        TableFrame.place(width=1900)
        xscroll=Scrollbar(TableFrame,orient=HORIZONTAL,activebackground="yellow",bg="green",width=10)
        yscroll=Scrollbar(TableFrame,orient=VERTICAL,activebackground="yellow",bg="green",width=10)
        self.libraryTable=ttk.Treeview(TableFrame,columns=("Member","First","Last","reg",'add',"branch","year","id","title","bdate","ddate","fee","mrp","rdate"),show='tree headings',xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(fill=X,side=BOTTOM)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.configure(command=self.libraryTable.xview)
        yscroll.configure(command=self.libraryTable.yview)
        self.libraryTable.heading("Member",text="Member Type")
        self.libraryTable.heading("First",text="First Name")
        self.libraryTable.heading("Last",text="Last Name")
        self.libraryTable.heading("reg",text="Reg. Number")
        self.libraryTable.heading("add",text="Address")
        self.libraryTable.heading("branch",text="Branch")
        self.libraryTable.heading("year",text="Year")
        self.libraryTable.heading("id",text="Book ID")
        self.libraryTable.heading("title",text="Book Title")
        self.libraryTable.heading("bdate",text="Borrow Date")
        self.libraryTable.heading("ddate",text="Due Date")
        self.libraryTable.heading("fee",text="Late Return Fee")
        self.libraryTable.heading("mrp",text="Book MRP")
        self.libraryTable.heading("rdate",text="Return Date")
        self.libraryTable.pack(fill=BOTH)
        self.libraryTable.column("#0",width=60)
        self.fetch_data()
        self.libraryTable.bind("<ButtonRelease-1>",self.get_cursor)
    #=======================================Buttons Commands========================================
    def AddData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="test1234",database="practice")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into newtable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.type.get(),self.firstname.get(),self.lastname.get(),self.regnumber.get(),self.add.get(),self.branch.get(),self.year.get(),self.bookid.get(),self.bookname.get(),self.bdate.get(),self.ddate.get(),self.fee.get(),self.price.get(),self.rdate.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")

    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="test1234",database="practice")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from newtable")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.libraryTable.delete(*self.libraryTable.get_children())
            for i in rows:
                self.libraryTable.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.libraryTable.focus()
        content=self.libraryTable.item(cursor_row)
        row=content["values"]

        self.type.set(row[0])
        self.firstname.set(row[1])
        self.lastname.set(row[2])
        self.regnumber.set(row[3])
        self.add.set(row[4])
        self.branch.set(row[5])
        self.year.set(row[6])
        self.bookid.set(row[7])
        self.bookname.set(row[8])
        self.bdate.set(row[9])
        self.ddate.set(row[10])
        self.fee.set(row[11])
        self.price.set(row[12])
        self.rdate.set(row[13])


    def show_data(self):
        self.txtbox.insert(END,"Member type:\t"+self.type.get()+"\n")
        self.txtbox.insert(END,"Fisrt Name:\t"+self.firstname.get()+"\n")
        self.txtbox.insert(END,"Last Name:\t"+self.lastname.get()+"\n")
        self.txtbox.insert(END,"Registration Number:\t"+self.regnumber.get()+"\n")
        self.txtbox.insert(END,"Address:\t"+self.add.get()+"\n")
        self.txtbox.insert(END,"Branch:\t"+self.branch.get()+"\n")
        self.txtbox.insert(END,"Year:\t"+self.year.get()+"\n")
        self.txtbox.insert(END,"Book ID:\t"+self.bookid.get()+"\n")
        self.txtbox.insert(END,"Book Name:\t"+self.bookname.get()+"\n")
        self.txtbox.insert(END,"Borrow Date:\t"+self.bdate.get()+"\n")
        self.txtbox.insert(END,"Due Date:\t"+self.ddate.get()+"\n")
        self.txtbox.insert(END,"Fine:\t"+self.fee.get()+"\n")
        self.txtbox.insert(END,"MRP:\t"+self.price.get()+"\n")
        self.txtbox.insert(END,"Return Date:\t"+self.rdate.get()+"\n")

    def reset(self):
        self.type.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.regnumber.set("")
        self.add.set("")
        self.branch.set("")
        self.year.set("")
        self.bookid.set("")
        self.bookname.set("")
        self.bdate.set("")
        self.ddate.set("")
        self.fee.set("")
        self.price.set("")
        self.rdate.set("")
        self.txtbox.delete("1.0",END)

    def exit(self):
        iexit=messagebox.askyesno("Library Management System","Do you want to exit")
        if iexit>0:
            window.destroy()
        else:
            return

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="test1234",database="practice")
        my_cursor=conn.cursor()
        my_cursor.execute(" update newtable set member_type=%s,First_name=%s,Last_name=%s,Registration_number=%s,address=%s,branch=%s,year=%s,bookid=%s,bookname=%s,bdate=%s,ddate=%s,fine=%s,mrp=%s,rdate=%s where Registration_number=%s",(self.type.get(),self.firstname.get(),self.lastname.get(),self.regnumber.get(),self.add.get(),self.branch.get(),self.year.get(),self.bookid.get(),self.bookname.get(),self.bdate.get(),self.ddate.get(),self.fee.get(),self.price.get(),self.rdate.get(),self.regnumber.get()))
        # query="update newtable set member_type=%s,First name=%s,Last name=%s,Registration number=%s,address=%s,branch=%s,year=%s,bookid=%s,bookname=%s,bdate=%s,ddate=%s,fine=%s,mrp=%s,rdate=%s where Registration number=%s"
        # value=(self.type.get(),self.firstname.get(),self.lastname.get(),self.regnumber.get(),self.add.get(),self.branch.get(),self.year.get(),self.bookid.get(),self.bookname.get(),self.bdate.get(),self.ddate.get(),self.fee.get(),self.price.get(),self.rdate.get(),self.regnumber.get())
        # my_cursor.execute(query,value)
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("success","Member has been updated successfuly")

    def Delete(self):
        if self.regnumber.get()=="" or self.bookid.get()=="":
            messagebox.showerror("Error","First select the member and the Book")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="test1234",database="practice")
            my_cursor=conn.cursor()
            my_cursor.execute("delete from newtable where Registration_number= %s",(self.regnumber.get(),))
            # query="delete from newtable where Registration_number=%s"
            # value=(self.regnumber.get(),)
            # my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member has been deleetd successfully")


window=Tk()
obj=LibraryManagementSystem(window)
window.mainloop()