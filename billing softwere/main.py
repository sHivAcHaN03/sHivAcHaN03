from scrollFrame import *
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import simpledialog
from mysql import *
from tkinter import messagebox as msg
import datetime as dt
import sys

global CREATE
global con3
global  win5
global slv
global Pqty
global amt
amt=0
Pqty=[]
slv=[]
con=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
#============create p1================
a=Tk()
a.geometry("1366x768+0+0")
a.title("Sign Up page")
a.config(bg="#4EC2F6")
a.iconbitmap("icon.ICO")
####all images 
img=PhotoImage(file="bill.png")
img1=PhotoImage(file="name.png")
img2=PhotoImage(file="mail.png")
img3=PhotoImage(file="pass.png")
img4=PhotoImage(file="cpass.png")
img5=PhotoImage(file="show.png")
img6=PhotoImage(file="hide.png")
img7=PhotoImage(file="in.png")
img8=PhotoImage(file="id.png")
img9=PhotoImage(file="out.png")
img10=PhotoImage(file="5.png")
img11=PhotoImage(file="admin.png")
img12=PhotoImage(file="eye.png")
img13=PhotoImage(file="ceye.png")
img14=PhotoImage(file="us.png")
img15=PhotoImage(file="password.png")
img16=PhotoImage(file="stock.png")
img17=PhotoImage(file="emp.png")
img18=PhotoImage(file="create1.png")
img19=PhotoImage(file="update.png")
img20=PhotoImage(file="add.png")
img21=PhotoImage(file="srch.png")
img22=PhotoImage(file="up.png")
img23=PhotoImage(file="del.png")
#img24=PhotoImage(file="add2.png")
img25=PhotoImage(file="bilm1.png")
img26=PhotoImage(file="ot.png")
img27=PhotoImage(file="Bill1.png")
############sign up page sql functions##############

def signup():
    a=f2e0.get()
    b=f2e1.get()
    c=f2e2.get()
    d=f2e3.get()
    tup=(a,b,c)
    if c==d:
        msg.showinfo("check","Password match")
        print(tup)
        res=con.cursor()
        sql="insert into sign_in(Full_name,Email,password) values (%s,%s,%s);"
        res.execute(sql,tup)
        con.commit()
        if res:
            msg.showinfo("success","Login Success")
            sign()
        else:
            msg.showerror("error","Login Failed")
    else:
        f2e3.delete(0,END)
        msg.showerror("check","Password mismatch")

#########designing##################
label0=Label(a,image=img,width=1000,height=700)
label0.place(x=0,y=63)
label1=Label(a,text="d",bg="#65D7FE",fg="#65D7FE",width=24,height=1)
label1.place(x=0,y=70)
label2=Label(a,text="vevrftrvgddrrf",bg="#2CCCFD",fg="#2CCCFD",width=28,height=1)
label2.place(x=163,y=70)
label3=Label(a,text="vevrftrvgddrrf",bg="#EC84F4",fg="#EC84F4",width=46,height=1)
label3.place(x=364,y=70) 
label4=Label(a,text="",bg="#4EC2F6",fg="#EC84F4",width=46,height=1)
label4.place(x=690,y=70)

#=================================page 1 frame 1 =================================
f1=Frame(a,width=1366,height=70)
f1.place(x=0,y=0)
f1.config(bg="#0a457f")

f1l0=Label(f1,text="Online Billing System",font=("Courier",20,"bold"),bg="#0a457f",fg="white",bd=2)
f1l0.place(x=500,y=20)

#=============page1 frame 2========
f2=Frame(a,width=1366,height=700)
f2.place(x=1002,y=70)
f2.config(bg="#bc88f9")

f2l0=Label(f2,text="Sign Up",font=("times",20,"bold"),bg="#bc88f9",fg="white")
f2l0.place(x=120,y=5)
def on_enter(e):
    f2e0.delete(0,END)
def on_leave(e):
    name=f2e0.get()
    if name =='':
        f2e0.insert(0, "Enter your Name ...")
        
f2l1=Label(f2,text="Full Name",font=("times",13,"bold"),bg="#bc88f9",fg="white")
f2l1.place(x=55,y=90)
f2e0=Entry(f2,font=("times",13,"bold"),bg="#bc88f9",fg="white",bd=0,width=30)
f2e0.insert(0, "Enter your Name ...")
f2e0.bind("<FocusIn>",on_enter)
f2e0.bind("<FocusOut>",on_leave)
f2e0.place(x=15,y=135)
f2l1=Label(f2,image=img1)
f2l1.place(x=9,y=90)
F1=Frame(f2,width=295,height=2,bg="white").place(x=15,y=155)

def on_enter1(e):
    f2e1.delete(0,END)
def on_leave1(e):
    name=f2e1.get()
    if name =='':
        f2e1.insert(0, " Email id ...")
f2l2=Label(f2,text="Email",font=("times",13,"bold"),bg="#bc88f9",fg="white")
f2l2.place(x=55,y=200)
f2e1=Entry(f2,font=("times",13,"bold"),bg="#bc88f9",fg="white",bd=0,width=30)
f2e1.insert(0," Email id ...")
f2e1.bind("<FocusIn>",on_enter1)
f2e1.bind("<FocusOut>",on_leave1)
f2e1.place(x=15,y=250)
f2l3=Label(f2,image=img2,width=26,height=26)
f2l3.place(x=9,y=200)
F2=Frame(f2,width=295,height=2,bg="white").place(x=15,y=270)

#=======password============
def on_enter2(e):
    f2e2.delete(0,END)
def on_leave2(e):
    name=f2e2.get()
    if name =='':
        f2e2.insert(0, " Password ...")
def show():
    f2b1=Button(f2,image=img5,command=hide,relief=FLAT,activebackground="#bc88f9",bg="#bc88f9",fg="black",height=-10,bd=0)
    f2b1.place(x=300,y=360)
    f2e2.config(show="")
    
def hide():
    f2b2=Button(f2,image=img6,command=show,relief=FLAT,activebackground="#bc88f9",bg="#bc88f9",fg="black",height=-10,bd=0)
    f2b2.place(x=300,y=360)
    f2e2.config(show="*")
f2l4=Label(f2,text="Password",font=("times",13,"bold"),bg="#bc88f9",fg="white")
f2l4.place(x=55,y=310)

f2e2=Entry(f2,font=("times",13,"bold"),bg="#bc88f9",fg="white",bd=0,width=30)
f2e2.insert(0," Password ...")
f2e2.bind("<FocusIn>",on_enter2)
f2e2.bind("<FocusOut>",on_leave2)
f2e2.place(x=15,y=360)
f2l3=Label(f2,image=img3,width=26,height=26)
f2l3.place(x=9,y=310)
F2=Frame(f2,width=295,height=2,bg="white").place(x=15,y=380)

f2b1=Button(f2,image=img6,command=hide,relief=FLAT,activebackground="#bc88f9",bg="#bc88f9",fg="black",height=-10,bd=0)
f2b1.place(x=300,y=360)

#=====comfirm password


def on_enter3(e):
    f2e3.delete(0,END)
def on_leave3(e):
    name=f2e3.get()
    if name =='':
        f2e3.insert(0, "Confirm Password ...")
def showc():
    f2b3=Button(f2,image=img5,command=hidec,relief=FLAT,activebackground="#bc88f9",bg="#bc88f9",fg="black",bd=0)
    f2b3.place(x=300,y=470)
    f2e3.config(show="")
    
def hidec():
    f2b4=Button(f2,image=img6,command=showc,relief=FLAT,activebackground="#bc88f9",bg="#bc88f9",fg="black",bd=0)
    f2b4.place(x=300,y=470)
    f2e3.config(show="*")
l4=Label(f2,text="Confirm Password",font=("times",13,"bold"),bg="#bc88f9",fg="white")
l4.place(x=55,y=420)
f2e3=Entry(f2,font=("times",13,"bold"),bg="#bc88f9",fg="white",bd=0,width=30)
f2e3.insert(0,"Confirm Password ...")
f2e3.bind("<FocusIn>",on_enter3)
#f2e3.bind("<FocusOut>",on_leave3)
f2e3.place(x=15,y=470)
f2l4=Label(f2,image=img4,width=26,height=26)
f2l4.place(x=9,y=420)
F2=Frame(f2,width=295,height=2,bg="white").place(x=15,y=490)

f2b3=Button(f2,image=img6,command=hidec,relief=FLAT,activebackground="#bc88f9",bg="#bc88f9",fg="black",bd=0)
f2b3.place(x=300,y=470)


#======>>>>>>>>>>>>> nxt page log in ###############
f2l5=Label(f2,text="Already You have an Account ?",font=("times",9),bg="#bc88f9",fg="black",bd=0)
f2l5.place(x=130,y=585)
c1=StringVar()
f2l5=Checkbutton(f2,text="i agree to the terms and conditions and privacy policy",activebackground="#bc88f9",variable=c1,onvalue=1,offvalue=0,height=0,width=50,bg="#bc88f9")
f2l5.place(x=0,y=530)

##########pag2
def sign():
    a.withdraw()
    win2=Toplevel()
    win2.title("Log in ")
    win2.geometry("1366x768")
    win2.config(bg="#5DC692")
    win2.iconbitmap("icon.ICO")
    #############functions##############

    def login():
        con2=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
        res2=con2.cursor()
        em1=w2e4.get()
        pwd1=w2e5.get()
        #print(em,pwd)
        tup2=(em1,pwd1)
        sql2="select * from sign_in where Email=%s and password=%s"
        res2.execute(sql2,tup2)
        rows=res2.fetchall()
        con2.close()
        if len(rows)==0:
            msg.showerror("note","Log in Failed")
        else:
            msg.showinfo("note","Log in success")
            update()
        print(len(rows))

    w2l1=Label(win2,image=img10,bd=0)
    w2l1.place(x=350,y=0)
    w2l2=Label(win2,text="Log in Here ...!",font=("times",35,"bold"),bg="#5DC692",fg="#141F35")
    w2l2.place(x=250,y=0)
    w2cb=ttk.Combobox(win2,width=20,height=50)
    w2cb["values"]=("employee"," ")
    w2cb.current(0)
    w2cb.place(x=300,y=160)
    w2l3=Label(win2,image=img11)
    w2l3.place(x=320,y=200)
    def on_enter(e):
            w2e4.delete(0,END)
    def on_leave(e):
        a=w2e4.get()
        if a=='':
            w2e4.insert(0,"Name or Mail id")
    w2e4=Entry(win2,font=("times",20,"bold"),bg="#5DC692",fg="#141F35")
    w2e4.insert(0,"Name or Mail id")
    w2e4.bind("<FocusIn>",on_enter)
    w2e4.bind("<FocusOut>",on_leave)
    w2e4.place(x=250,y=350)
    w2l6=Label(win2,image=img14,bg="#5DC692")
    w2l6.place(x=200,y=350)
    def on_enter1(e):
        w2e5.delete(0,END)
    def on_leave1(e):
        a=w2e5.get()
        if a=='':
            w2e5.insert(0,"Password")
            
    w2e5=Entry(win2,font=("times",20,"bold"),bg="#5DC692",fg="#141F35")
    w2e5.insert(0,"Password")
    w2e5.bind("<FocusIn>",on_enter1)
    w2e5.bind("<FocusOut>",on_leave1)
    w2e5.place(x=250,y=430)
    w2c0=Checkbutton(win2,text="Remember Me ...!",font=("times",12,"bold"),activebackground="#5DC692",bg="#5DC692")
    w2c0.place(x=250,y=480)
    #w2b0=Button(win2,text="Log In",font=("times",17,"bold"),activebackground="#5DC692",bg="#703DC1",fg="#141F35",command=update)
    #w2b0.place(x=330,y=530)
    def show():
        w2b0=Button(win2,image=img12,command=hide,activebackground="#5DC692",bg="#5DC692")
        w2b0.place(x=540,y=435)
        w2e5.config(show="")
    def hide():    
        w2b1=Button(win2,image=img13,command=show,activebackground="#5DC692",bg="#5DC692")
        w2b1.place(x=540,y=435)
        w2e5.config(show="*")
    w2l7=Label(win2,image=img15,bg="#5DC692")
    w2l7.place(x=200,y=435)
##=============page 3
    def update():
        win2.withdraw()
        
        win3=Toplevel()
        win3.title("Update page ")
        win3.geometry("700x600+300+80")
        win3.config(bg="skyblue")
        win3.iconbitmap("icon.ICO")
        #w3btn=Button(win3,image=img16)
        #w3btn.place(x=150,y=250)
        w3lbl=Label(win3,text="Stock Update",font=("times",13,"bold"),bg="skyblue")
        w3lbl.place(x=150,y=352)
        #w3btn1=Button(win3,image=img17,font=("times",12,"bold"),command=main)
        #w3btn1.place(x=400,y=250)
        w3lbl=Label(win3,text="Employee Billing",font=("times",13,"bold"),bg="skyblue")
        w3lbl.place(x=400,y=352)

###############Stock page 
        def Stock():
            win3.withdraw()
            win5=Toplevel()
            win5.title("Stock In")
            win5.geometry("1366x768")
            win5.config(bg="#F2BE22")
            win5.iconbitmap("icon.ICO")
            
            lbl=Label(win5,text="Stock In Page ",font=("Times",22,"bold"),width=1366,height=2,bg="#F2BE22",fg="black",relief=GROOVE)
            lbl.pack()
            def close1():
                win5.withdraw()
                main()
            btn=Button(win5,image=img25,command=close1,bg="#F2BE22",bd=0)
            btn.place(x=10,y=25)
            l1=Label(win5,text="Bill Page",font=("times",12,"bold"),bg="#F2BE22",fg="black")
            l1.place(x=7,y=0)
            
            ### Stock page tree view
            def tree():
                con3=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                res3=con3.cursor()
                sql3="select *from prodcuts;"
                res3.execute(sql3,)
                mytree=ttk.Treeview(win5,height=15)
                mytree["columns"]=('S.No','Product Name','Quantity','Rate','Dis Amt','Dis%','stockIn date','Expiry date ','GST')
                mytree.column('#0',width=10,stretch=NO)
                style=ttk.Style(win5)
                style.theme_use("classic")
                style.configure("Treeview")
                style.configure("Treeview.Heading",background="#A0BFE0",foreground="black")
#stretch=NO means it will remove the 0th column
                mytree.column("#1",width=60,anchor=CENTER)
                mytree.column("#2",width=180,anchor=CENTER)
                mytree.column("#3",width=180,anchor=CENTER)
                mytree.column("#4",width=130,anchor=CENTER)
                mytree.column("#5",width=150,anchor=CENTER)
                mytree.column("#6",width=150,anchor=CENTER)
                mytree.column("#7",width=180,anchor=CENTER)
                mytree.column("#8",width=180,anchor=CENTER)
                mytree.column("#9",width=130,anchor=CENTER)
                
                mytree.heading("#0",text="")
                mytree.heading("#1",text="Sno")
                mytree.heading("#2",text="Product Name")
                mytree.heading("#3",text="Quantity")
                mytree.heading("#4",text="Rate")
                mytree.heading("#5",text="Dis Amt")
                mytree.heading("#6",text="Dis%")
                mytree.heading("#7",text="stockIn date")
                mytree.heading("#8",text="Expiry date")
                mytree.heading("#9",text="GST")
                #res3=Stock()
                for i in res3:
                    if i[0]%2==0:
                        mytree.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]),tags=("even",))
                    else:
                        mytree.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]),tags=("odd",))
                mytree.tag_configure("even",background="#97FEED",foreground="black")
                mytree.tag_configure("odd",background="#35A29F",foreground="black")
                mytree.place(x=0,y=80)
            ##stock frame 1
                global fw5e
###############Stock page             
                f3=Frame(win5,width=1366,height=50,relief=GROOVE,bd=5)
                f3.config(bg="#74DBEF")
                f3.place(x=100,y=410)
                fw5l=Label(f3,text="Product Name",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l.grid(row=0,column=0,sticky=W,pady=2)
                fw5l1=Label(f3,text="Quantity",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l1.grid(row=1,column=0,sticky=W,pady=2)
                fw5l2=Label(f3,text="Rate",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l2.grid(row=2,column=0,sticky=W,pady=2)
                fw5l3=Label(f3,text="Dis Amt",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l3.grid(row=3,column=0,sticky=W,pady=2)
                fw5l4=Label(f3,text="Dis%",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l4.grid(row=4,column=0,sticky=W,pady=2)
                fw5l5=Label(f3,text="StockIn date",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l5.grid(row=5,column=0,sticky=W,pady=2)
                fw5l6=Label(f3,text="Expiry date",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l6.grid(row=6,column=0,sticky=W,pady=2)
                fw5l7=Label(f3,text="GST",font=("times",15,"bold"),bg="#74DBEF",fg="black")
                fw5l7.grid(row=7,column=0,sticky=W,pady=2)
                fw5e=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e.grid(row=0,column=1,pady=2)
                fw5e1=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e1.grid(row=1,column=1,pady=2)
                fw5e2=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e2.grid(row=2,column=1,pady=2)
                fw5e3=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e3.grid(row=3,column=1,pady=2)
                fw5e4=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e4.grid(row=4,column=1,pady=2)
                fw5e5=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e5.grid(row=5,column=1,pady=2)
                fw5e6=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e6.grid(row=6,column=1,pady=2)
                fw5e7=Entry(f3,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                fw5e7.grid(row=7,column=1,pady=2)
                mytree.tag_configure("even",background="#97FEED",foreground="black")
                mytree.tag_configure("odd",background="#35A29F",foreground="black")
                def Insert():
                    pn=fw5e.get()
                    qty=fw5e1.get()
                    rt=fw5e2.get()
                    da=fw5e3.get()
                    d=fw5e4.get()
                    st=fw5e5.get()
                    ex=fw5e6.get()
                    Gst=fw5e7.get()
                    con=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                    res=con.cursor()
                    sql=("insert into  prodcuts(Product_Name,Quantity,Rate,Dis_Amt,Dis,stockIn_date,Expiry_date,GST)values(%s,%s,%s,%s,%s,%s,%s,%s);")
                    user=(pn,qty,rt,da,d,st,ex,Gst)
                    res.execute(sql,user)
                        #print(con.lastrowSno)
                    con.commit()
                    mytree.insert('','end',text="",values=(pn,qty,rt,da,d,st,ex,Gst))
                    msg.showinfo("Note","Product added successfully")
                    fw5e.delete(0,END)
                    fw5e1.delete(0,END)
                    fw5e2.delete(0,END)
                    fw5e3.delete(0,END)
                    fw5e4.delete(0,END)
                    fw5e5.delete(0,END)
                    fw5e6.delete(0,END)
                    fw5e7.delete(0,END)
                    tree()
                    ###serch treeview
                def Search():
                    try:
                        con1=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                        res1=con1.cursor()
                        f4=Frame(win5,width=1366,height=50,relief=GROOVE,bd=5)
                        f4.config(bg="#74DBEF")
                        f4.place(x=0,y=350)
                        f4w5l=Label(f4,text="Product Name",font=("times",12,"bold"),bg="#74DBEF",fg="black")
                        f4w5l.grid(row=0,column=0,sticky=W,pady=2)
                        f4w5l1=Label(f4,text="Quantity",font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5l1.grid(row=0,column=1,sticky=W,pady=2)
                        f4w5l2=Label(f4,text="Rate",font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5l2.grid(row=0,column=2,sticky=W,pady=2)
                        f4w5l3=Label(f4,text="Dis Amt",font=("times",12,"bold"),bg="#74DBEF",fg="black")
                        f4w5l3.grid(row=0,column=3,sticky=W,pady=2)
                        f4w5l4=Label(f4,text="Dis%",font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5l4.grid(row=0,column=4,sticky=W,pady=2)
                        f4w5l5=Label(f4,text="StockIn date",font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5l5.grid(row=0,column=5,sticky=W,pady=2)
                        f4w5l6=Label(f4,text="Expiry date",font=("times",12,"bold"),bg="#74DBEF",fg="black")
                        f4w5l6.grid(row=0,column=6,sticky=W,pady=2)
                        f4w5l7=Label(f4,text="GST",font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5l7.grid(row=0,column=7,sticky=W,pady=2)
                        
                        f4w5e=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e.grid(row=1,column=0,pady=2)
                        f4w5e1=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e1.grid(row=1,column=1,pady=2)
                        f4w5e2=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e2.grid(row=1,column=2,pady=2)
                        f4w5e3=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e3.grid(row=1,column=3,pady=2)
                        f4w5e4=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e4.grid(row=1,column=4,pady=2)
                        f4w5e5=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e5.grid(row=1,column=5,pady=2)
                        f4w5e6=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e6.grid(row=1,column=6,pady=2)
                        f4w5e7=Entry(f4,font=("times",11,"bold"),bg="#74DBEF",fg="black")
                        f4w5e7.grid(row=1,column=7,pady=2)
                        
                        f4w5e.delete(0,END)
                        f4w5e1.delete(0,END)
                        f4w5e2.delete(0,END)
                        f4w5e3.delete(0,END)
                        f4w5e4.delete(0,END)
                        f4w5e5.delete(0,END)
                        f4w5e6.delete(0,END)
                        f4w5e7.delete(0,END)                        
                        r2=simpledialog.askstring("Search","Plese Enter the id you need to search ")
                        sql1="select*from prodcuts where sno ="+r2
                        print("1")
                        res1.execute(sql1,)
                        row=res1.fetchall()
                        print(row)
                        def fun(a):
                            fun2(*a)
                        def fun2(a,b,c,d,e,f,g,h,i):
                            print(a,b,c,d,e,f,g,h,i)
                            f4w5e.insert(0,b)
                            f4w5e1.insert(0,c)
                            f4w5e2.insert(0,d)
                            f4w5e3.insert(0,e)
                            f4w5e4.insert(0,f)
                            f4w5e5.insert(0,g)
                            f4w5e6.insert(0,h)
                            f4w5e7.insert(0,i)
                        fun(*row)
                        print("succssfully")                        
                    except  Exception as e:
                        print("e")
                def Update():
                    r5=simpledialog.askstring("Note","Plece enter the Sno to Update ")
                    con5=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                    res5=con5.cursor()
                    pn=fw5e.get()
                    qty=fw5e1.get()
                    rt=fw5e2.get()
                    da=fw5e3.get()
                    d=fw5e4.get()
                    st=fw5e5.get()
                    ex=fw5e6.get()
                    Gst=fw5e7.get()
                    user5=(pn,qty,rt,da,d,st,ex,Gst,r5)
                    sql5=("update prodcuts set Product_Name=%s ,Quantity=%s ,Rate=%s ,Dis_Amt=%s ,Dis=%s ,stockIn_date=%s ,Expiry_date=%s ,GST=%s  where sno=%s ")
                    res5.execute(sql5,user5)
                    fw5e.delete(0,END)
                    fw5e1.delete(0,END)
                    fw5e2.delete(0,END)
                    fw5e3.delete(0,END)
                    fw5e4.delete(0,END)
                    fw5e5.delete(0,END)
                    fw5e6.delete(0,END)
                    fw5e7.delete(0,END)                  
                    con5.commit()
                    tree()
                def Delete():
                    con4=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                    res4=con4.cursor()
                    r4=simpledialog.askstring("delete","Plese Enter the id width you want delete" )
                    sql4=("delete from prodcuts where  sno=%s;")
                    user4=(r4,)
                    res4.execute(sql4,user4)
                    con4.commit()
                    fw5e.delete(0,END)
                    fw5e1.delete(0,END)
                    fw5e2.delete(0,END)
                    fw5e3.delete(0,END)
                    fw5e4.delete(0,END)
                    fw5e5.delete(0,END)
                    fw5e6.delete(0,END)
                    fw5e7.delete(0,END)
                    tree()
                fwlbl1=Label(win5,text="Insert",font=("times",15,"bold"),activebackground="#F2BE22",bg="green",fg="black")
                fwlbl1.place(x=20,y=470)
                fwlbl2=Label(win5,text="Search",font=("times",15,"bold"),bg="#8CC0DE",fg="black")
                fwlbl2.place(x=430,y=470)
                fwlbl3=Label(win5,text="Update",font=("times",15,"bold"),bg="#88598b",fg="black")
                fwlbl3.place(x=660,y=470)
                fwlbl4=Label(win5,text="Delete",font=("times",15,"bold"),bg="red",fg="black")
                fwlbl4.place(x=860,y=470)            
                ###page  5 buttons
                fwbtn1=Button(win5,image=img20,command=Insert,bg="#F2BE22",bd=0)
                fwbtn1.place(x=20,y=420)
                fwbtn2=Button(win5,image=img21,command=Search,bg="#F2BE22",bd=0)
                fwbtn2.place(x=430,y=420)
                fwbtn3=Button(win5,image=img22,command=Update,bg="#F2BE22",bd=0)
                fwbtn3.place(x=660,y=420)
                fwbtn4=Button(win5,image=img23,command=Delete,bg="#F2BE22",bd=0)
                fwbtn4.place(x=860,y=420)
            tree()

#=====================#### page 4 componants=====================================###################################################################
        def main():
##########Create  in bill page ###############################################

            def CREATE():
                cname=w4e0.get()
                cph=w4e1.get()
                cadd=ENTRY1.get()
                disp=ENTRY2.get()
                srep=ENTRY3.get()
                billty=w4cb.get()
                tm=TOT_E.get()
                print(billty)
                con1=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                res1=con1.cursor()
                sql1="insert into customer(cust_name,cust_ph,cust_add,dis_price,s_rep,bill_type,totamt) values(%s,%s,%s,%s,%s,%s,%s);"
                user1=(cname,cph,cadd,disp,srep,billty,tm)
                res1.execute(sql1,user1)
                con1.commit()
                w4e0.delete(0,END)
                w4e1.delete(0,END)
                ENTRY1.delete(0,END)
                ENTRY2.delete(0,END)
                ENTRY3.delete(0,END)
                w4cb.delete(0,END)
                TOT_E.delete(0,END)
                print("hi")
                msg.showinfo("CREATE","Detailes stored Successfull")
#############search in bill page ###############################################
            def Search():
                global w4E2
                billno=w4E2.get()
                #billno="4"
                print(billno)
                tup=(billno,)
                print(tup)
                con2=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
                res2=con2.cursor()
                try:
                    sql2="SELECT *FROM customer where bill_number="+billno
                    #print("success")
                    #print(sql2)
                    res2.execute(sql2,)
                    #print(res2)
                    rows=res2.fetchall()
                    #print(rows)
                    #print("success")
                    def fun(a):
                        fun2(*a)
                    def fun2(a,b,c,d,e,f,g,h):
                        w4e0.insert(0,b)
                        w4e1.insert(0,c)
                        ENTRY1.insert(0,d)
                        ENTRY2.insert(0,e)
                        ENTRY3.insert(0,f)
                        w4cb.insert(0,g)
                        TOT_E.insert(0,h)
                        
                    fun(*rows)
                    print("hgh")
                except Exception as e:
                    print("e")
            win3.withdraw()
            win4=Toplevel()
            win4.title("Log in")
            win4.geometry("1366x768")
            win4.config(bg="#4F4557")

            #### page 4 componants==================================================================================================
            #############variables
            bill_no=StringVar()
            c_name=StringVar()
            phone=StringVar()
            
            win4.iconbitmap("icon.ICO")
            title=Label(win4,text="Billing Software",font=("times",22,"bold"),bg="#4F4557",fg="white",height=2,bd=5,relief=GROOVE)
            title.pack(fill=X)
            w4lbl0=Label(win4,width=1366,height=4,bg="#4F4557",bd=5,relief=GROOVE)
            w4lbl0.place(x=0,y=65)
            w4l1=Label(win4,text="Customer Detailes",font=("times",12,"bold"),bg="#4F4557",fg="yellow")
            w4l1.place(x=2,y=65)
            w4l2=Label(win4,text="Customer Name",font=("times",15,"bold"),bg="#4F4557",fg="white")
            w4l2.place(x=15,y=95)
            w4e0=Entry(win4,font=("times",12),bg="white",fg="black",width=25,textvariable=c_name)
            w4e0.place(x=175,y=100)
            w4l2=Label(win4,text="Phone No.",font=("times",15,"bold"),bg="#4F4557",fg="white")
            w4l2.place(x=400,y=95)
            w4e1=Entry(win4,font=("times",12),bg="white",fg="black",width=25)
            w4e1.place(x=500,y=100)
            w4l3=Label(win4,text="Bill  No.",font=("times",15,"bold"),bg="#4F4557",fg="white")
            w4l3.place(x=720,y=95)
            global w4E2
            w4E2=Entry(win4,font=("times",12),bg="white",fg="black",textvariable=bill_no)
            w4E2.place(x=800,y=100)
            #w4b2=Button(win4,text="Search",command=Search,font=("times",12,"bold"),bg="skyblue",fg="white",width=8,activeforeground="white",activebackground="#4F4557")
            #w4b2.place(x=1030,y=95)
            w4l4=Label(win4,text="Log Out ",font=("times",9,"bold"),bg="#4F4557",fg="yellow")
            w4l4.place(x=10,y=3)
            w4l7=Label(win4,text="Stock Entry",font=("times",9,"bold"),bg="#4F4557",fg="yellow")
            w4l7.place(x=1270,y=3)
            #w4b0=Button(win4,image=img9,command=sign,height=0,width=0)
            #w4b0.place(x=20,y=30)
            date=dt.datetime.now()
            time=Label(win4,text=f"{date: %d/%m/%y}",font=("times",15,"bold"),bg="#4F4557",fg="white")
            time.place(x=1230,y=95)
            lab=Label(win4,text="date : ",font=("times",15,"bold"),fg="white",bg="#4F4557")
            lab.place(x=1150,y=95)
                        ###tree view
            w4con=mysql.connector.connect(host="localhost",user="root",password="kitty03",database="siva")
            w4res=w4con.cursor()
            w4sql="select *from prodcuts;"
            w4res.execute(w4sql,)
            def displaySelectedItem(a):
                r=simpledialog.askstring("Note","Enter the quantity: ")
                Pqty.append(int(r))          
                
                selectedItem=mytree.selection()[0]
                print(mytree.item(selectedItem)["values"][0:])
                slv.append(mytree.item(selectedItem)["values"][0:])
                print(len(slv))
                print(Pqty)
            mytree=ttk.Treeview(win4,height=21)
            mytree["columns"]=('S.No','Product Name','Quantity','Rate','Dis Amt','Dis%','stockIn date','Expiry date ','GST')
            mytree.column('#0',width=30,stretch=NO)
            style=ttk.Style(win4)
            style.theme_use("classic")
            style.configure("Treeview")
            style.configure("Treeview.Heading",background="white",foreground="black")
        
#stretch=NO means it will remove the 0th column
            mytree.column("#0",width=0,anchor=CENTER)
            mytree.column("#1",width=120,anchor=CENTER)
            mytree.column("#2",width=210,anchor=CENTER)
            mytree.column("#3",width=120,anchor=CENTER)
            mytree.column("#4",width=120,anchor=CENTER)
            mytree.column("#5",width=120,anchor=CENTER)
            mytree.column("#6",width=120,anchor=CENTER)
            mytree.column("#7",width=210,anchor=CENTER)
            mytree.column("#8",width=210,anchor=CENTER)
            mytree.column("#9",width=120,anchor=CENTER)           
            mytree.heading("#0",text="")
            mytree.heading("#1",text="Sno")
            mytree.heading("#2",text="Product Name")
            mytree.heading("#3",text="Quantity")
            mytree.heading("#4",text="Rate")
            mytree.heading("#5",text="Dis Amt")
            mytree.heading("#6",text="Dis%")
            mytree.heading("#7",text="stockIn date")
            mytree.heading("#8",text="Expiry date")
            mytree.heading("#9",text="GST")
            #mytree.place(x=5,y=150)
            for i in w4res:
                if i[0]%2==0:
                    mytree.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]),tags=("even",))
                else:
                    mytree.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]),tags=("odd",))
            mytree.tag_configure("even",background="#A9A9A9",foreground="black")
            mytree.tag_configure("odd",background="#D3D3D3",foreground="black")
            mytree.place(x=5,y=148)
            mytree.bind("<<TreeviewSelect>>", displaySelectedItem)
            lbl1=LabelFrame(win4,font=("times",16,"bold"),bg="#4f4557",fg="white",relief=GROOVE,bd=5)
            lbl1.place(x=5,y=600,width=1350,height=130)
            w4l5=Label(win4,text="Product Details",font=("times",12,"bold"),bg="#4F4557",fg="yellow")
            w4l5.place(x=5,y=120)
            w4l6=Label(win4,text="Bill Details",font=("times",12,"bold"),bg="#4F4557",fg="yellow")
            w4l6.place(x=5,y=590)
            ##BILL AREA ===============================================================================================
##########Delete in bill page ###############################################

            def BILL():
                win6=Toplevel(win4)
                win6.title("BILL page ")
                win6.geometry("750x500+580+180")
                win6.config(bg="#73777B")
                win6.iconbitmap("icon.ICO")
                win6.resizable(False,False)

                wf=ScrollableFrame(win6)
                f1=Frame(wf.frame,bg="white",width=740,height=3000)
                f1.grid(row=1,column=0)
                F1l=Frame(f1,width=750,height=2,bg="black").place(x=0,y=140)

                f1l3=Label(f1,text="Sno",font=("times",12,"bold"))
                f1l3.place(x=10,y=150)
                f1l4=Label(f1,text="Product Name",font=("times",12,"bold"))
                f1l4.place(x=160,y=150)
                f1l5=Label(f1,text="Quantity",font=("times",12,"bold"))
                f1l5.place(x=310,y=150)
                f1l6=Label(f1,text="Rate",font=("times",12,"bold"))
                f1l6.place(x=460,y=150)
                f1l7=Label(f1,text="Total",font=("times",12,"bold"))
                f1l7.place(x=610,y=150)
                F2ll=Frame(f1,width=750,height=2,bg="black").place(x=0,y=180)
                x1=10
                y1=165
                k=0
                for i in slv:
                    ii=0
                    x1=10
                    y1=y1+40
                    for j in i:
                        ii+=1
                        if ii==5:
                            break
                        else:
                            if x1==310:
                                f1ln2=Label(f1,text=Pqty[k],font=("times",12,"bold"))
                                f1ln2.place(x=x1,y=y1)
                                x1=x1+150
                                k+=1
                            else:
                                f1ln3=Label(f1,text=j,font=("times",12,"bold"))
                                f1ln3.place(x=x1,y=y1)
                                x1=x1+150
                kk=0
                rates=[]
                ppid=[]
                for i in slv:
                    iii=0
                    for j in i:
                        if iii==0:
                            ppid.append(j)
                        if iii==3:
                            #print(j*Pqty[kk])
                            rates.append(j*Pqty[kk])
                            kk+=1
                        else:
                            pass
                        iii+=1
                print(rates)
                print("this is ppid",ppid)
                x1=610
                y1=165
                kkk=0
                for i in rates:
                    y1=y1+40
                    f1ln1=Label(f1,text=i,font=("times",12,"bold"))
                    f1ln1.place(x=x1,y=y1)
                    kkk=kkk+i
                print(kkk)
                amt=kkk
                def crl():
                    global slv
                    print("before slv ",slv)
                    slv=[]
                    print("after slv ",slv)
                    win6.withdraw()
                def insertrate():
                    f1e1.insert(0,amt)
                    totamt(amt)
                f1b1=Button(f1,text="Clear BILL",command=crl,font=("times",12,"bold"),bg="blue",fg="white")
                f1b1.place(x=10,y=y1+50)
                f1b2=Button(f1,text="TOTAL",command=insertrate,font=("times",12,"bold"),bg="blue",fg="white")
                f1b2.place(x=450,y=y1+50)
                f1e1=Entry(f1,font=("times",12,"bold"),width=12,bg="blue",fg="white")
                f1e1.place(x=600,y=y1+55)
                #f1e1.insert(0,kkk)
                F2lll=Frame(f1,width=750,height=2,bg="black").place(x=0,y=y1+40)
                F2llll=Frame(f1,width=750,height=2,bg="black").place(x=0,y=y1+85)
                wf.pack(side=BOTTOM,fill=BOTH,expand=YES)      
            LBL2=Label(win4,text="Customer_address",font=("15",12,"bold"),bg="#4f4557",fg="white")
            LBL2.place(x=20,y=620)
            ENTRY1=Entry(win4,font=("times",15,"bold"),bg="white",bd=0)
            ENTRY1.place(x=180,y=620)
            LBL3=Label(win4,text="Discount price",font=("15",12,"bold"),bg="#4f4557",fg="white")
            LBL3.place(x=20,y=680)
            ENTRY2=Entry(win4,font=("times",15,"bold"),bg="white",bd=0)
            ENTRY2.place(x=180,y=680)

            LBL4=Label(win4,text="Sales_rep*",font=("15",12,"bold"),bg="#4f4557",fg="white")
            LBL4.place(x=400,y=680)
            ENTRY3=Entry(win4,font=("times",15,"bold"),bg="white",bd=0)
            ENTRY3.place(x=500,y=680)
            LBL3=Label(win4,text="BillType",font=("15",12,"bold"),bg="#4f4557",fg="white")
            LBL3.place(x=400,y=620)

            w4cb=ttk.Combobox(win4)
            w4cb["values"]=(" ","C-CASH BILL","K-CARD BILL","U-UPI")
            w4cb.current(0)
            w4cb.place(x=500,y=620)
            
            LBL7=Label(win4,text="CREATE",font=("times",12,"bold"),bg="#4f4557",fg="white")
            LBL7.place(x=780,y=690)
            BTN1=Button(win4,image=img18,bd=0,command=CREATE,bg="#4f4557",fg="white",activebackground="#4f4557")
            BTN1.place(x=850,y=670)
            LBL8=Label(win4,text="BILL",font=("times",12,"bold"),bg="#4f4557",fg="white")
            LBL8.place(x=950,y=690)
            BTN2=Button(win4,image=img27,command=BILL,font=("times",15,"bold"),bd=0,bg="#4f4557",activebackground="#4f4557",fg="black",activeforeground="white")
            BTN2.place(x=1000,y=670)
            
            TOT_Bamt=Label(win4,text="Total Bill amt..:",font=("times",16,"bold"),bg="#4f4557",fg="white")
            TOT_Bamt.place(x=700,y=615)
            def totamt(amtr):
                TOT_E.insert(0,amtr)
            TOT_E=Entry(win4,font=("times",16,"bold"),bg="white",fg="black")
            TOT_E.place(x=850,y=615)

            
            

            
            #######bill area
            ##page 4 button
            w4b2=Button(win4,text="Search",command=Search,font=("times",12,"bold"),bg="skyblue",fg="white",width=8,activeforeground="white",activebackground="#4F4557")
            w4b2.place(x=1030,y=95)
            def close3():
                sign()
                win4.withdraw()    
            w4b0=Button(win4,image=img9,command=close3,height=0,width=0)
            w4b0.place(x=20,y=30)
            def close2():
                win4.withdraw()
                Stock()
            w4b1=Button(win4,image=img26,command=close2,bg="#4f4557",bd=0)
            w4b1.place(x=1300,y=25)
        ##page 3 buttons
        w3btn1=Button(win3,image=img17,font=("times",12,"bold"),command=main)
        w3btn1.place(x=400,y=250)
        w5btn=Button(win3,image=img16,command=Stock)
        w5btn.place(x=150,y=250)        
        ##page 2 button
    w2b0=Button(win2,text="Log In",font=("times",17,"bold"),activebackground="#5DC692",bg="#703DC1",fg="#141F35",command=login)
    w2b0.place(x=330,y=530)
###page 1 button
f2b0=Button(f2,text="Sign Up",font=("times",12,"bold"),activebackground="skyblue",bg="#0a457f",fg="yellow",width=7,height=1,command=signup)
f2b0.place(x=20,y=580)

f2b01=Button(f2,image=img7,bg="#bc88f9",activebackground="#bc88f9",fg="black",bd=0,width=0,height=0,command=sign)
f2b01.place(x=290,y=580)


mainloop()

