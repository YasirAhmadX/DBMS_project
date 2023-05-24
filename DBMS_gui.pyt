from tkinter import *
from tkinter import messagebox as msg
import mysql.connector


#########################################################################

Host='localhost'
port=3360
User='root'
Passwd=input("User: root\nPassword: ")
Database='Fertilizer_Shop'

TableName='sales'

SalesIDColumnName='S_ID'
ProductColumnName='Pname'
QuantityColumnName='Quantity'
CustomerColumnName='Cname'

IndexOfSalesIDColumn=0  
IndexOfProductColumn=1
IndexOfQuantityColumn=2
IndexOfCustomerColumn=3

##########################################################################
##########################################################################

DB=mysql.connector.connect(host=Host,user=User,passwd=Passwd,database=Database,port=port)
Csr=DB.cursor()

def Menu():
    global L0,B0,B1,B2,B3,B4
    
    window.geometry('150x200')
    
    L0=Label(window,text=' MENU',font=('Times New Roman',18))
    B0=Button(window,text='Enter Data',command=EntryScreen,width=12)
    B1=Button(window,text='View Data',command=ViewScreen,width=12)
    B2=Button(window,text='Update Data',command=ViewScreen,width=12)
    B3=Button(window,text='Delete Data',command=ViewScreen,width=12)
    B4=Button(window,text='Exit',command=exit,width=12)

    L0.grid()
    B0.grid(column=0,row=1)
    B1.grid(column=0,row=2)
    B2.grid(column=0,row=3)
    B3.grid(column=0,row=4)
    B4.grid(column=0,row=5)
def DeleteData():
    global query
    query='delete from '+ TableName + ' where ' + SalesIDColumnName + ' = ' + r
    
    B01.destroy()
    B02.destroy()
    
    B00.configure(text='Confirm Delete!',command=Confirm,width=17)
def UpdatingData():
    global query
    
    n= E01.get()
    g= E02.get()
    a= E03.get()

    query='update '+ TableName + ' set ' + ProductColumnName + '=\'' + n + '\',' + CustomerColumnName + '=\'' + g + '\',' + QuantityColumnName+ '=' + a +' where ' + SalesIDColumnName + '=' + r

    E01.destroy()
    E02.destroy()
    E03.destroy()

    L01.configure(text='Updated name will be: '+n,width=len('Updated name will be: '+n)+4)
    L02.configure(text='Updated gender will be: '+g,width=len('Updated gender will be: '+g)+4)
    L03.configure(text='Updated age will be: '+str(a),width=len('Updated age will be: '+str(a))+4)
    
    B00.configure(text='Confirm!',command=Confirm)
def UpdateData():
    
    B01.destroy()
    B02.destroy()
    
    

    L01.configure(text='Enter new Product Name: ')
    L02.configure(text='Enter Customer Name: ')
    L03.configure(text='Enter Quantity: ')
    
    E01.grid(column=1,row=5)
    E02.grid(column=1,row=6)
    E03.grid(column=1,row=7)

    B00.configure(text='Update!',command=UpdatingData,width=8)
    

def Confirm():
    L00.configure(text='Sales ID: '+str(r),width=len('Sales ID: '+str(r))+4)
    L01.configure(text='Product Name: Record has been deleted/updated',width= 2+ len('Product Name: Record has been deleted/updated'))
    L02.configure(text='Customer Name: Record has been deleted/updated',width= 2+ len('Customer Name: Record has been deleted/updated'))
    L03.configure(text='Quantity: Record has been deleted/updated',width= 2+ len('Quantity: Record has been deleted/updated'))
    
    B00.configure(text='Ok!',command=ViewDone)

    Csr.execute(query)
    
    q='select * from '+ TableName + ' where ' + SalesIDColumnName + ' = ' + r
    Csr.execute(q)
    response2=Csr.fetchall()
    if response!=response2:
        msg.showinfo('Message from Yasir','Data has been altered sucessfully! ')
    else:
        msg.showinfo('Message from Yasir','Operation Failed ! ')

def ViewDone():
    try:
        L00.destroy()
        L01.destroy()
        L02.destroy()
        L03.destroy()
        E00.destroy()
        E01.destroy()
        E02.destroy()
        E03.destroy()
    except:
        pass
    try:
        B00.destroy()
        B01.destroy()
        B02.destroy()
        B03.destroy()
        B04.destroy()
    except:
        pass
    DB.commit()
    Menu()
def ViewData():
    global r,n,a,g,response
    r=E00.get()
    query='select * from '+ TableName + ' where ' + SalesIDColumnName + ' = ' + r
    
    Csr.execute(query)
    response=Csr.fetchall()
    
    if response!=[]:
        n=response[0][IndexOfProductColumn]
        a=response[0][IndexOfQuantityColumn]
        g=response[0][IndexOfCustomerColumn]
        L01.configure(text='Product Name: '+n,width=len('Product Name: '+n)+4)
        L02.configure(text='Customer Name: '+g,width=len('Customer Name: '+g)+4)
        L03.configure(text='Quantity: '+str(a),width=len('Quantity: '+str(a))+4)
        B01.grid(column=1,row=8)
        B02.grid(column=2,row=8)
        
    else:
        L01.configure(text='Product Name: No Matching Data found',width= 2+ len('Product Name: No Matching Data found'))
        L02.configure(text='Customer Name: No Matching Data found',width= 2+ len('Customer Name: No Matching Data found'))
        L03.configure(text='Quantity: No Matching Data found',width= 2+ len('Quantity: No Matching Data found'))
    E00.destroy()
    L00.configure(text='Sales ID: '+str(r),width=len('Sales ID: '+str(r))+4)
    B00.configure(text='Ok!',command=ViewDone,width=6)
    
    B00.grid(column=0,row=8)
        
def ViewScreen():
    global L00,L01,L02,L03,E00,E01,E02,E03,B00,B01,B02

    window.geometry('250x300')

    L0.destroy()
    B0.destroy()
    B1.destroy()
    B2.destroy()
    B3.destroy()
    B4.destroy()
    
    msg.showinfo('Message from Yasir','Enter the Sales_ID of the required sales data')
    L00=Label(window,text='Enter Sales ID: ')
    L01=Label(window,text='Product Name: ')
    L02=Label(window,text='Customer Name: ')
    L03=Label(window,text='Quantity: ')

    E00=Entry(window,width=15,bd=4)
    E01=Entry(window,width=15,bd=4)
    E02=Entry(window,width=15,bd=4)
    E03=Entry(window,width=15,bd=4)

    B00=Button(window,text='Proceed',fg='Blue',command=ViewData)
    B01=Button(window,text='Update',fg='Black',command=UpdateData)
    B02=Button(window,text='Delete',fg='Red',command=DeleteData)
    
    L00.grid(column=0,row=4)
    L01.grid(column=0,row=5)
    L02.grid(column=0,row=6)
    L03.grid(column=0,row=7)
    
    E00.grid(column=1,row=4)
    B00.grid(column=2,row=4)
    
def EntryDone():
    
    n= E01.get()
    g= E02.get()
    a= E03.get()
    
    q='insert into ' + TableName +'('+SalesIDColumnName+','+ProductColumnName+','+QuantityColumnName+','+CustomerColumnName+')'+ ' values(%s,%s,%s,%s)'
    val=(r,n,a,g)
    Csr.execute(q,val)
    query='select * from '+ TableName + ' where ' + SalesIDColumnName + ' = ' + r
    Csr.execute(query)
    Response=Csr.fetchall()
    if Response==[]:
        msg.showinfo('Message from Yasir','Operation Failed!\nData not submitted sucessfully! ')
    else:
        msg.showinfo('Message from Yasir','Data has been submitted sucessfully! ')
    ViewDone()
    
def EnterData():
    global r
    r= E00.get()
    q='select * from '+ TableName +' where '+ SalesIDColumnName +' = '+r
    Csr.execute(q)
    response=Csr.fetchall()
    if response==[]:

        L01.grid(column=0,row=2)
        L02.grid(column=0,row=3)
        L03.grid(column=0,row=4)

        E01.grid(column=1,row=2)
        E02.grid(column=1,row=3)
        E03.grid(column=1,row=4)

        B00.configure(text='Submit',command=EntryDone)
        B00.grid(column=1,row=5)
    else:
        E00.destroy()
        L00.configure(text='Data for Sales_ID '+str(r)+' already exists.',width=len('Data for Sales_ID '+str(r)+' already exists.')+2)
        B00.configure(text='Ok!',command=ViewDone)
        
def EntryScreen():
    global L00,L01,L02,L03,E00,E01,E02,E03,B00

    window.geometry('400x300')
    
    L0.destroy()
    B0.destroy()
    B1.destroy()
    B2.destroy()
    B3.destroy()
    B4.destroy()
    
    msg.showinfo('Message from Yasir','Enter the data(Sales_ID should be unique)')
    L00=Label(window,text='Enter Sales ID: ',width=25)
    L01=Label(window,text='Enter Product Name: ',width=25)
    L02=Label(window,text='Enter Customer Name: ',width=25)
    L03=Label(window,text='Enter Quantity: ',width=25)
        
    E00=Entry(window,width=20,bd=4)
    E01=Entry(window,width=20,bd=4)
    E02=Entry(window,width=20,bd=4)
    E03=Entry(window,width=20,bd=4)

    B00=Button(window,text='Proceed',fg='Blue',command=EnterData)

    L00.grid(column=0,row=0)   
    
    E00.grid(column=1,row=0)

    B00.grid(column=2,row=0)
    
window=Tk()
window.title('DBMS_project(22MIA1064 and 22MIA1049)')

Menu()

window.mainloop()
