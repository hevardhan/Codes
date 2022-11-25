import tkinter as t
from tkinter import END
import pandas as pd


#dictionary : 
user_data ={
    "test":"1234"}

data={}


data_list=[]
rd = pd.read_excel("data.xlsx")
l = rd.values.tolist()
for x in range(len(l)):
    g = l[x]
    g = list(map(str,g))
    data[g[0]]=g[1:5]
    
            
                
        
print(data)      

#------------------------------------------------------------------#
def add():
    n = t.Tk()
    n.title("Add Data")
    x = 0
    while x < 1 :
        t.Label(n, text="Enter the Name of the Student :").grid(row=0)
        t.Label(n, text="Enter the BEEE Mark :").grid(row=2)
        t.Label(n, text="Enter the IPP Mark :").grid(row=3)
        t.Label(n, text="Enter the CHE Mark :").grid(row=4)
        t.Label(n, text="Enter the LA Mark :").grid(row=5)
        
        name = t.Entry(n)
        beee = t.Entry(n)
        ipp = t.Entry(n)
        che = t.Entry(n)
        la = t.Entry(n)
        name.grid(row=0, column=1)
        beee.grid(row=2, column=1)
        ipp.grid(row=3, column=1)
        che.grid(row=4, column=1)
        la.grid(row=5, column=1)
        x = 1
        
    
        
        def data_add():
            
            
            n_v = name.get()
            b_v = beee.get()
            i_v = ipp.get()
            c_v = che.get()
            l_v = la.get()
            data[n_v]=[b_v,i_v,c_v,l_v]
            print(data)
            name.delete(0, END)
            beee.delete(0, END)
            ipp.delete(0, END)
            che.delete(0, END)
            la.delete(0, END)
            name_list = list(data.keys())
            value_list = list(data.values())
            table = pd.DataFrame(value_list,index=name_list,columns=['a','b','c','d'])
            table.to_excel("data.xlsx",sheet_name="1")
            
          
        t.Button(n, text="ADD",command=data_add).grid(row=8,column=0)
        t.Button(n, text="SAVE",command=n.destroy).grid(row=8,column=1)
    
    n.mainloop()
def delete():
    o = t.Tk()
    o.title("Delete Data")
    
    t.Label(o, text="Enter the Name of the Student : ").grid(row=0)
    del_name = t.Entry(o)
    del_name.grid(row=0, column=1)
    
    def data_del():
        remove = del_name.get()
        if remove in data:
            data.pop(remove)
            name_list = list(data.keys())
            value_list = list(data.values())
            table = pd.DataFrame(value_list,index=name_list,columns=['a','b','c','d'])
            table.to_excel("data.xlsx",sheet_name="1")
            del_name.delete(0, END)
            t.Label(o, text="Data Deleted Successfully !!").grid(row=5)
            
            
        else :
            t.Label(o, text="Entered Name is Not in the Data").grid(row=5)
        
    t.Button(o, text="Delete", command=data_del).grid(row=3)
    t.Button(o, text="Save", command=o.destroy).grid(row=3, column=1)
    o.mainloop()
def ops():
    b = t.Tk()
    b.geometry("500x250")
    b.title("Data")
    t.Label(b, text="Please choose your the Opperation").grid(row=6, column=1)
    t.Button(b, text="ADD DATA", command=add).grid(row=7,column=1)
    t.Button(b, text="DELETE DATA", command=delete).grid(row=7,column=2)
    b.mainloop()
def show_entry_fields():
    user_name = n3.get()
    password = n4.get()
    
    if user_name in user_data:
        if user_data[user_name] ==password :
            t.messagebox.showinfo("","Login Succesfull !!")
            n3.delete(0, END)
            n4.delete(0, END)
            m.destroy()
            ops()    
        else :
            t.messagebox.showerror("","Invalid Password")
            n3.delete(0, END)
            n4.delete(0, END)
    else:
        t.messagebox.showerror("","Username Doesn't Exist !!!")
        n3.delete(0, END)
        n4.delete(0, END)
def sign_up():
    s = t.Tk()
    s.title("Sign up portal")
    t.Label(s, text="Sign up Portal").grid(row=0)
    t.Label(s, text="Enter your User Id : ").grid(row = 1)
    t.Label(s, text="Enter your Password : ").grid(row=2)
    user_id = t.Entry(s)
    pswd = t.Entry(s)
    user_id.grid(row=1, column=1)
    pswd.grid(row=2, column=1)
    def done():
        user_data[user_id.get()]=pswd.get()
        print(user_data)
        t.messagebox.showinfo("","Sign up Successfull!!")
        
    t.Button(s, text="Sign Up", command=done).grid(row=5)
    s.mainloop()

    
m = t.Tk()
m.geometry("250x150")
m.title("Mark Entry Portal")   
n1=t.Label(m, text="Username :").grid(row=0)
n2=t.Label(m, text="Password :").grid(row=1)
n3=t.Entry(m)
n4=t.Entry(m)
n3.grid(row=0, column=1)
n4.grid(row=1, column=1)
n5 = t.Button(m, text='Log in', command=show_entry_fields).grid(row=3, column=1, sticky=t.W, pady=4)
n6 = t.Button(m, text="Sign Up", command=sign_up).grid(row=3,column=2)



m.mainloop()
