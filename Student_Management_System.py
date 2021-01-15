import tkinter
from tkinter import *
from tkinter import ttk#For combobox
import pymysql#For connect with database
root=Tk()
class Student:
    def __init__ (self,root):
        self.root=root
        self.root.title("Student Management System")#window title
        self.root.geometry("1350x700+0+0")#window size & position
        self.root.configure(background='red')#window background color
        title=Label(self.root,text="Student Management System",fg='black',bg='yellow',bd=10,relief=GROOVE,font=("Times new roman",18,"bold"))#title on the window
        title.pack(side=TOP,fill=X)#side=TOP(Center allignment) & fill=X(X axis Fill up by color)

        #*****Al Variable*****
        self.roll_v=StringVar()
        self.name_v=StringVar()
        self.email_v=StringVar()
        self.gender_v=StringVar()
        self.contact_v=StringVar()
        self.dob_v=StringVar()
        self.searchby_v=StringVar()
        self.search_v=StringVar()


        #************MANAGEMENT FRAME*************
        Manage_Frame=Label(self.root,bd=4,relief=RIDGE,bg='green')#Management box which situated in left side of window
        Manage_Frame.place(x=20,y=70,width=450,height=600)
        M_title=Label(Manage_Frame,text='Student Management',fg='black',bg='green',font=('times new roman',16,'bold'))
        M_title.pack(side=TOP)

            #****Roll Box*****
        roll=Label(Manage_Frame,text='Roll No:',fg='black',bg='green',font=('times new roman',14,'bold'))#roll
        roll.place(x=40,y=80)
        In_roll=Entry(Manage_Frame,textvariable=self.roll_v,bd=1,width=25,font=14)#roll input
        In_roll.place(x=135,y=84)

            #*****Name Box*****
        name=Label(Manage_Frame,text='Name:',fg='black',bg='green',font=('times new roman',14,'bold'))#name
        name.place(x=42,y=120)
        In_name=Entry(Manage_Frame,textvariable=self.name_v,bd=1,width=25,font=14)#name input
        In_name.place(x=135,y=124)

            #*****E-mail Box****
        email=Label(Manage_Frame,text='E-mail:',fg='black',bg='green',font=('',14,'bold'))#E-mail
        email.place(x=40,y=160)
        In_email=Entry(Manage_Frame,textvariable=self.email_v,bd=1,width=25,font=14)#E-mail input
        In_email.place(x=135,y=164)

            #*****Gender Box******
        gender=Label(Manage_Frame,text='Gender:',fg='black',bg='green',font=('',14,'bold'))#Gender
        gender.place(x=40,y=204)
        In_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_v,font=14,width=23,state='readonly')#Gender Option
        In_gender['values']=('Male','Female','Others')
        In_gender.place(x=135,y=204)

            #*****Contact*****
        contact=Label(Manage_Frame,text='Contact:',fg='black',bg='green',font=('',14,'bold'))#contact
        contact.place(x=40,y=244)
        In_contact=Entry(Manage_Frame,textvariable=self.contact_v,bd=1,width=25,font=14)#contact input
        In_contact.place(x=135,y=244)

            #*****Date Of Birth********
        date_of_birth=Label(Manage_Frame,text='D.O.B:',fg='black',bg='green',font=('',14,'bold'))#Date Of Birth
        date_of_birth.place(x=40,y=284)
        In_date_of_birth=Entry(Manage_Frame,textvariable=self.dob_v,bd=1,width=25,font=14)#Date of Birth input
        In_date_of_birth.place(x=135,y=284)

            #*****Address****
        address=Label(Manage_Frame,text='Address:',fg='black',bg='green',font=('',14,'bold'))#Address
        address.place(x=40,y=340)
        self.In_address=Text(Manage_Frame,width=25,height=4,font=14)#Address input
        self.In_address.place(x=135,y=324)

        #******Button******
        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,width=200,bg='green')#button box in management box
        btn_frame.place(x=10,y=500,width=420,height=35)

        add_btn=Button(btn_frame,text='Add',width=8,fg='white',bg='black',font=('',10,'bold'),command=self.add_stu)#Add button
        add_btn.place(x=3,y=0)

        update_btn=Button(btn_frame,text='Update',width=8,fg='white',bg='black',font=('',10,'bold'),command=self.update_data)#Update button
        update_btn.place(x=112,y=0)

        delete_btn=Button(btn_frame,text='Delete',width=8,fg='white',bg='black',font=('',10,'bold'),command=self.delete_data)#Delete button
        delete_btn.place(x=218,y=0)

        clear_btn=Button(btn_frame,text='Clear',width=8,fg='white',bg='black',font=('',10,'bold'),command=self.clear)#clear button
        clear_btn.place(x=333,y=0)

        #************DETAIL FRAME****************
        Detail_Frame=Label(self.root,bd=4,relief=RIDGE,bg='green')#Detail box which situated in right side of window
        Detail_Frame.place(x=500,y=70,width=800,height=600)
        D_title=Label(Detail_Frame,text='Student Details',fg='black',bg='green',font=('times new roman',16,'bold'))
        D_title.pack(side=TOP)

        #*****Search ******
        search=Label(Detail_Frame,text='Search By:',fg='black',bg='green',font=('',14,'bold'))#Search
        search.place(x=0,y=40)
        op_search=ttk.Combobox(Detail_Frame,font=14,state='readonly',textvariable=self.searchby_v)#Search option
        op_search['values']=('Roll No','Name','Contact')
        op_search.place(x=110,y=40,width=100)

        In_search=Entry(Detail_Frame,bd=2,relief=RIDGE,width=35,font=14,textvariable=self.search_v)#Search box
        In_search.place(x=240,y=40)

        search_btn=Button(Detail_Frame,text='Search',fg='white',bg='black',font=('',10,'bold'),width=8,command=self.search_data)#Search button
        search_btn.place(x=600,y=38)

        showall_btn=Button(Detail_Frame,text='Search All',fg='white',bg='black',font=('',10,'bold'),width=10,command=self.fetch_data)#Show all button
        showall_btn.place(x=690 ,y=38)

        #Table Frame******
        table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='green')#Table Frame
        table_frame.place(x=10,y=80,width=770,height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)#Scroll bar left to right
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)#Scroll bar up to down
        self.Student_table=ttk.Treeview(table_frame,columns=('roll','name','e-mail','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill=X)#Scroll right & left
        scroll_y.pack(side=RIGHT,fill=Y)#Scroll Up & down
        scroll_x.config(command=self.Student_table.xview)#view scroll
        scroll_y.config(command=self.Student_table.yview)#view scroll
        self.Student_table.heading('roll',text='Roll')#Heading on table
        self.Student_table.heading('name',text='Name')#
        self.Student_table.heading('e-mail',text='E-mail')#
        self.Student_table.heading('gender',text='Gender')#
        self.Student_table.heading('contact',text='Contact')#
        self.Student_table.heading('dob',text='D.O.B')#
        self.Student_table.heading('address',text='Address')#Heading on table

        self.Student_table['show']='headings'#show just heading

        self.Student_table.column('roll',width=100)#space in table
        self.Student_table.column('name',width=180)
        self.Student_table.column('e-mail',width=200)
        self.Student_table.column('gender',width=100)
        self.Student_table.column('contact',width=150)
        self.Student_table.column('dob',width=150)
        self.Student_table.column('address',width=350)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    #***Add values in database *****
    def add_stu(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='shamol')
        cur=con.cursor()
        cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)',(self.roll_v.get(),
                                                                         self.name_v.get(),
                                                                         self.email_v.get(),
                                                                         self.gender_v.get(),
                                                                         self.contact_v.get(),
                                                                         self.dob_v.get(),
                                                                         self.In_address.get('1.0',END)
                                                                         ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    #******Show data on the table********
    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='shamol')
        cur = con.cursor()
        cur.execute('select * from students')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    #******clear data from the table*****
    def clear(self):
        self.roll_v.set('')
        self.name_v.set('')
        self.email_v.set('')
        self.gender_v.set('')
        self.contact_v.set('')
        self.dob_v.set('')
        self.In_address.delete('1.0',END)

    #click on the output get in input table
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.roll_v.set(row[0])
        self.name_v.set(row[1])
        self.email_v.set(row[2])
        self.gender_v.set(row[3])
        self.contact_v.set(row[4])
        self.dob_v.set(row[5])
        self.In_address.delete('1.0',END)
        self.In_address.insert(END,row[6])

    #Update data from the table
    def update_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='shamol')
        cur = con.cursor()
        cur.execute('update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll=%s', (
                                                                          self.name_v.get(),
                                                                          self.email_v.get(),
                                                                          self.gender_v.get(),
                                                                          self.contact_v.get(),
                                                                          self.dob_v.get(),
                                                                          self.In_address.get('1.0', END),
                                                                          self.roll_v.get()
                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    #Delete data from the table
    def delete_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='shamol')
        cur = con.cursor()
        cur.execute('delete from students where roll=%s',self.roll_v.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='shamol')
        cur = con.cursor()

        cur.execute("select * from students where"+str(self.searchby_v.get())+"LIKE '% "+str(self.search_v.get())+" %'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

ob=Student(root)
root.mainloop()