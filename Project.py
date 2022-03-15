import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from csv import writer

win=tk.Tk()
win.geometry("1920x1800")

label1=tk.Label(win,text=("STUDY WELL PUBLIC SCHOOL"),height='3',width='75',font=('verdana',24,'bold'))
label1.place(x=0,y=0)
label1.configure(background="yellow",foreground="black")

label8=tk.Label(win,text="DELHI 123456", height=1, width=75, font=("verdana",17,"bold"))
label8.place(x=210,y=80)
label8.configure(background="yellow",foreground="black")

c=tk.Canvas(win,bg='yellow',height=358,width=358)
file=tk.PhotoImage(file='image.png')
id=c.create_image(1,1,anchor=tk.NW,image=file)
c.place(x=0,y=0)
################################################################################
def action2():
    exit()
def Student(username1):
    l1=[]
    l2=[]
    win2=tk.Tk()
    win2.geometry("1000x600+0+0")
    def back2():
        win2.destroy()
    back_button=tk.Button(win2,text='<--EXIT-->', height= 1, width="10",font=("verdana",15,"bold"),command=back2)
    back_button.configure(bg="red",fg="yellow")
    back_button.place(x=830,y=500)
    with open("StuData.csv","r") as c:
        a=csv.reader(c)
        for line in a:
            l1.append(line)
        if l1!=[[]]:
            for i in range(1,len(l1)):
                if l1[i][0]==username1:
                    l2.append(l1[i])
                else:
                    continue
        label1=tk.Label(win2,text="Welcome "+ username1,height=2,width=30,bg="blue",fg="white",font=("varadane",20,"bold")).place(x=220,y=0)
        label2=tk.Label(win2,text="BOOK NAME",height=1,width=12,bg="yellow",font=("varadane",20,"bold")).place(x=0,y=100)
        label3=tk.Label(win2,text="TAKEN ON",height=1,width=12,bg="yellow",font=("varadane",20,"bold")).place(x=250,y=100)
        label4=tk.Label(win2,text="SUBMITTED ON",height=1,width=12,bg="yellow",font=("varadane",20,"bold")).place(x=500,y=100)
        label4=tk.Label(win2,text="FINE",height=1,width=12,bg="yellow",font=("varadana",20,"bold")).place(x=750,y=100)        
        a=len(l2)
        b=a-1
        i=0
        m=0
        while m<11 and a>0:
            labelof=tk.Label(win2,text=l2[b][1],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=0,y=150+i)
            labelof2=tk.Label(win2,text=l2[b][2],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=250,y=150+i)
            labelof3=tk.Label(win2,text=l2[b][3],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=500,y=150+i)
            labelof4=tk.Label(win2,text=l2[b][4],bg="orange",fg="red",width=20,font=("varadana",12,"bold")).place(x=750,y=150+i)
            a=a-1
            b=b-1
            i+=30
            m+=1            
    win2.mainloop()
################################################################################
def Librarian(username1):
    win3=tk.Tk()
    win3.geometry("700x300+300+250")    
    def Libstu():
        username8=name3_var.get()
        win4=tk.Tk()
        win4.geometry("1000x600+0+0")
        l1=[]
        l2=[]
        l3=[]
        def actiontt():
            v=p.get()
            y=q.get()
            if v=='' or y=='':
                messagebox.showinfo("Fill","Something Went Wrong")
            else:
                submitted=tk.Label(win4,text='Submitted', height= 2, width="13",font=("verdana",15,"bold"))
                submitted.configure(bg="blue",fg="white")
                submitted.place(x=815,y=500)                
                u=[username8,v,y,'','']
                l1.append(u)
                with open("StuData.csv","w",newline='') as f:
                    csv_writer=writer(f)
                    csv_writer.writerows(l1)
                labelofdate2=tk.Label(win4,text=v,bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=30,y=150)
                labeloffine=tk.Label(win4,text=y,bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=280,y=150)                        

        with open("StuData.csv","r") as c:
            a=csv.reader(c)
            for line in a:
                l1.append(line)
        if l1==[[]]:
            label1=tk.Label(win4,text="Details  Of  "+ username8,height=2,width=30,bg="blue",fg="white",font=("varadane",20,"bold")).place(x=150,y=0)
            back_button=tk.Button(win4,text='<--EXIT-->', height= 1, width="10",font=("verdana",15,"bold"),command=action2)
            back_button.configure(bg="red",fg="yellow")
            back_button.place(x=830,y=550)                 
            label2=tk.Label(win4,text="BOOK NAME",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=0,y=100)
            label3=tk.Label(win4,text="TAKEN ON",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=250,y=100)
            label4=tk.Label(win4,text="SUBMITTED ON",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=500,y=100)
            label5=tk.Label(win4,text="FINE",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=750,y=100)
            p=tk.StringVar()
            p=ttk.Entry(win4,width="25",textvariable=p)
            p.place(x=50,y=150)
            p.focus()                
            q=tk.StringVar()
            q=ttk.Entry(win4,width="25",textvariable=q)
            q.place(x=300,y=150)
            q.focus()                
            submit_button=tk.Button(win4,text='Submit', height= 1, width="10",font=("verdana",15,"bold"),command=actiontt)
            submit_button.configure(bg="blue",fg="white")
            submit_button.place(x=830,y=500)                

        else:
            for i in range(1,len(l1)):
                if l1[i][0]==username8:    
                    l2.append(l1[i])
                    l3.append(l1[i])                
            label1=tk.Label(win4,text="Details  Of  "+ username8,height=2,width=30,bg="blue",fg="white",font=("varadane",20,"bold")).place(x=150,y=0)
            back_button=tk.Button(win4,text='<--EXIT-->', height= 1, width="10",font=("verdana",15,"bold"),command=action2)
            back_button.configure(bg="red",fg="yellow")
            back_button.place(x=830,y=550)                 
            label2=tk.Label(win4,text="BOOK NAME",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=0,y=100)
            label3=tk.Label(win4,text="TAKEN ON",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=250,y=100)
            label4=tk.Label(win4,text="SUBMITTED ON",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=500,y=100)
            label5=tk.Label(win4,text="FINE",height=1,width=15,bg="yellow",font=("varadane",20,"bold")).place(x=750,y=100)
            a=len(l2)
            b=a-1
            i=0
            m=0
            h=[]
            f=[]
            def actionee():
                d=q.get()
                e=r.get()
                if d=='' or e=='':
                    messagebox.showinfo("Fill","Something Went Wrong")
                else:
                    submitted=tk.Label(win4,text='Submitted', height= 2, width="13",font=("verdana",15,"bold"))
                    submitted.configure(bg="blue",fg="white")
                    submitted.place(x=815,y=500)                                
                    l2[-1].remove('')
                    l2[-1].remove('')
                    l2[-1].append(d)
                    l2[-1].append(e)
                    for i in l3:
                        l1.remove(i)
                    for i in l2:
                        l1.append(i)
                    labelofdate2=tk.Label(win4,text=d,bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=530,y=150)
                    labeloffine=tk.Label(win4,text=e,bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=780,y=150)            
                    with open("StuData.csv","w",newline='') as f:
                        csv_writer=writer(f)
                        csv_writer.writerows(l1)
            if l2==[]:
                    p=tk.StringVar()
                    p=ttk.Entry(win4,width="25",textvariable=p)
                    p.place(x=50,y=150)
                    p.focus()                
                    q=tk.StringVar()
                    q=ttk.Entry(win4,width="25",textvariable=q)
                    q.place(x=300,y=150)
                    q.focus()                
                    submit_button=tk.Button(win4,text='Submit', height= 1, width="10",font=("verdana",15,"bold"),command=actiontt)
                    submit_button.configure(bg="blue",fg="white")
                    submit_button.place(x=830,y=500)                
            elif l2[-1][-1]=="":
                while m<11 and a>0:
                    labelofbook=tk.Label(win4,text=l2[b][1],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=30,y=150+i)
                    labelofdate1=tk.Label(win4,text=l2[b][2],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=280,y=150+i)
                    if (l2[a-1][3])=='':
                        q=tk.StringVar()
                        q=ttk.Entry(win4,width="25",textvariable=q)
                        q.place(x=530,y=150)
                        q.focus()
                        r=tk.StringVar()
                        r=ttk.Entry(win4,width="25",textvariable=r)
                        r.place(x=780,y=150)
                        r.focus()               
                        submit_button=tk.Button(win4,text='Submit', height= 1, width="10",font=("verdana",15,"bold"),command=actionee)
                        submit_button.configure(bg="blue",fg="white")
                        submit_button.place(x=830,y=500)
                    else:
                        labelofdate2=tk.Label(win4,text=l2[b][3],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=530,y=150+i)
                        labeloffine=tk.Label(win4,text=l2[b][4],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=780,y=150+i)
                    b=b-1
                    m=m+1
                    i+=30
                    a=a-1
            elif len(l2[-1])==5:
                    p=tk.StringVar()
                    p=ttk.Entry(win4,width="25",textvariable=p)
                    p.place(x=50,y=150)
                    p.focus()                
                    q=tk.StringVar()
                    q=ttk.Entry(win4,width="25",textvariable=q)
                    q.place(x=300,y=150)
                    q.focus()                        
                    submit_button=tk.Button(win4,text='Submit', height= 1, width="10",font=("verdana",15,"bold"),command=actiontt)
                    submit_button.configure(bg="blue",fg="white")
                    submit_button.place(x=830,y=500)               
                    while m<10 and a>0:
                        labelofbook=tk.Label(win4,text=l2[b][1],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=30,y=180+i)
                        labelofdate1=tk.Label(win4,text=l2[b][2],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=280,y=180+i)
                        labelofdate2=tk.Label(win4,text=l2[b][3],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=530,y=180+i)
                        labeloffine=tk.Label(win4,text=l2[b][4],bg="orange",fg="red",width=20,font=("varadane",12,"bold")).place(x=780,y=180+i)                    
                        b=b-1
                        m=m+1
                        i+=30
                        a=a-1
        win4.mainloop()
    def back():
        win3.destroy()
    label1=tk.Label(win3,text="Welcome "+ username1,height=2,width=30,bg="blue",fg="white",font=("varadane",20,"bold")).place(x=100,y=0)
    name_label=tk.Label(win3,text='ENTER THE NAME',height="1",width="20",font=("verdana",15,"bold"))
    name_label.place(x=0,y=100)
    name_label.configure(background='red',foreground='yellow')
    
    name3_var=tk.StringVar()
    name3_var=ttk.Entry(win3,width="50",textvariable=name3_var)
    name3_var.place(x=350,y=100)
    name3_var.focus()

    submit_button=tk.Button(win3,text='GET INFO', height= 1, width="10",font=("verdana",15,"bold"),command=Libstu)
    submit_button.configure(bg="blue",fg="white")
    submit_button.place(x=250,y=150)
    
    back_button=tk.Button(win3,text='<--EXIT-->', height= 1, width="9",font=("verdana",15,"bold"),command=back)
    back_button.configure(bg="red",fg="yellow")
    back_button.place(x=550,y=200)
    win3.mainloop()
################################################################################    
label2=tk.Label(win,height="1",width="52")
label2.place(x="0",y="360")
label2.configure(bg='orange')

label3=tk.Label(win,height="35",width="2")
label3.place(x="360",y="0")
label3.configure(bg='orange')

label4=tk.Label(win,height="1",width="300")
label4.place(x="360",y="0")
label4.configure(bg='orange')

label5=tk.Label(win,height="25",width="2")
label5.place(x="0",y="360")
label5.configure(bg='orange')

label6=tk.Label(win,height="80",width="2")
label6.place(x="1350",y="0")
label6.configure(bg='orange')

label7=tk.Label(win,height="1",width="300")
label7.place(x="0",y="520")
label7.configure(bg='orange')
################################################################################
lable9=tk.Label(win,text="---Login Here---" , height= 1, width="17",font=("verdana",20,"bold"))
lable9.place(x=520,y=170)
lable9.configure(background="blue",foreground="white")

label10=tk.Label(win,height=9,width=48)
label10.place(x=19,y=380)
label10.configure(background='yellow')

name_label=tk.Label(win,text='ENTER YOUR USERNAME',height="1",width="20",font=("verdana",15,"bold"))
name_label.place(x=400,y=250)
name_label.configure(background='red',foreground='yellow')

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width="50",textvariable=name_var)
name_entrybox.place(x=700,y=254)
name_entrybox.focus()

passw_label=tk.Label(win,text='ENTER YOUR PASSWORD',height="1",width="20",font=("verdana",15,"bold"))
passw_label.place(x=400,y=300)
passw_label.configure(background='yellow',foreground='green')

passw_var=tk.StringVar()
passw_entrybox=ttk.Entry(win,width="50",textvariable=passw_var,show="*")
passw_entrybox.place(x=700,y=305)
passw_entrybox.focus()

user_type=tk.StringVar()
radiobtn1=tk.Radiobutton(win,text='Student', value='Student',height=1,width=10,font=("varadana",15) ,variable=user_type)
radiobtn1.place(x=550,y=356)
radiobtn4=tk.Radiobutton(win,text='Librarian', value='Librarian',height=1,width=10,font=("varadana",15),variable=user_type)
radiobtn4.place(x=750,y=356)

checkbtn_var=tk.IntVar()
checkbtn=tk.Checkbutton(win,text='Information Checked',font=("varadana",15), variable=checkbtn_var)
checkbtn.place(x=600,y=400)

h=tk.Label(win,text="Do not share your username or password",font=("verdana",15,"bold")).place(x=500,y=570)
i=tk.Label(win,text="You can get your password and username changed in school office",font=("verdana",15,"bold")).place(x=370,y=620)

def Rules():
    with open("rules.txt","r") as r:
        c=r.read()
        win5=tk.Tk()
        win5.geometry("1000x300")
        l=tk.Label(win5,text=c).place(x=0,y=0)
        win5.mainloop()
k=tk.Button(win, text="Rules And Regulation", height=4,width=20,font=("verdana",15,"bold"),command=Rules)
k.configure(bg="blue",fg="white")
k.place(x=45,y=390)
################################################################################
def action():
        username1=name_var.get()
        userpassw=passw_var.get()
        usertype=user_type.get()
        checkbtn=checkbtn_var.get()
        if username1=='' or userpassw=='' or usertype=='' or checkbtn==0:
                messagebox.showinfo("Wrong","Something Went Wrong")
        else:
                l=[]
                l1=[]
                with open("Password.csv","r") as f:
                        c=csv.reader(f)
                        for i in c:
                                l.append(i)
                        for i in range(len(l)):
                                if username1==l[i][0] and userpassw==l[i][1] and usertype==l[i][2]:
                                        l1.append(l[i])
                                else:
                                        continue
                if l1==[]:
                        messagebox.showinfo("wrong","Something went wrong")
                elif l1[0][2]=="Student":
                        Student(username1)
                elif l1[0][2]=="Librarian":
                        Librarian(username1)
################################################################################
submit_button=tk.Button(win,text='LOGIN', height= 1, width="10",font=("verdana",15,"bold"),command=action)
submit_button.configure(bg="blue",fg="white")
submit_button.place(x=650,y=450)
extit=tk.Button(win,text="CLOSE",height=1,width="10",font=("verdana",15,"bold"),command=action2)
extit.configure(bg="blue",fg="white")
extit.place(x=1200,y=650)
################################################################################
win.mainloop()
