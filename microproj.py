from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import tkinter.messagebox
import csv
#===========================================================            FUNCTIONS              =====================================================
ev=0
def add():
    #...............PERSONAL......................................................................
    l=last_name.get()     #'''last name'''
    f=first_name.get()    #'''first name'''
    try:
        if(l=='' or f==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if (l.isdigit() or f.isdigit()):
            raise NameError
    except NameError:
        tkinter.messagebox.showerror('Error','Your name should only comprise of characters!')
        return


    y=year.get()          #'''year'''
    m=month.get()         #'''month'''
    d=day.get()           #'''day'''
    DOB=y+'/'+m+'/'+d     #'''DOB'''
    try :
        if(y=='' or m=='' or d==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        import datetime
        datetime.datetime(int(y),int(m),int(d))
    except ValueError :
        tkinter.messagebox.showerror('Error','Enter valid DOB!')
        return

    s=sex.get()           #'''sex'''
    s=int(s)
    l2=['Male','Female','Other']

    v=food.get()            #'''V/NV'''
    v=int(v)
    l3=['Veg','Non-veg']


    p=phone.get()         #'''phone no.'''
    m=mobile.get()        #'''mobile no.'''
    try:
        if(p=='' or m==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(p.isdigit()==False and m.isdigit()==False):
            raise ValueError
        if(len(p) and len(m)!=10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error','Phone number should only have 10 digits!')
        return

    e=email.get()         #'''email'''
    try:
        if(e==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        l5=e.split('@')
        if(len(l5)!=2):
            raise IndexError
        l6=l5[1].split('.')
        if(len(l6)!=2):
            raise IndexError
    except IndexError:
        tkinter.messagebox.showerror('Error','Enter valid Email id!')
        return
        
    
    #................ADDRESS...........................................................
    st=street.get()
    lo=local.get()
    p_s=ps.get()
    p_o=po.get()
    d=district.get()
    ci=city.get()
    ur=ub.get()
    ur=int(ur)
    l4=['Urban','Rural']
    sta=state.get()
    co=country.get()

    pi=pin.get()
    if(pi==''):
        tkinter.messagebox.showwarning('','Please fill all the required fields')
        return
    if(len(pi)!=6):
        tkinter.messagebox.showerror('Error','Enter valid PIN!')
        return

    #................GUARDIAN.............................................................

    na=gname.get()               #'''guardian name'''
    try:
        if(na==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(na.isdigit()):
            raise NameError
    except NameError:
        tkinter.messagebox.showerror('Error','Name should only comprise of characters!')
        return

    occ=gocc.get()               #'occupation'''

    cn=gcontact.get()        #'''guard contact'''
    try:
        if(cn==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(cn.isdigit()==False):
            raise ValueError
        if(len(cn)!=10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error','Phone number should only have 10 digits!')
        return

    ea=gemail.get()     #'''guard email'''
    try:
        if(ea==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        l5=ea.split('@')
        if(len(l5)!=2):
            raise IndexError
        l6=l5[1].split('.')
        if(len(l6)!=2):
            raise IndexError
    except IndexError:
        tkinter.messagebox.showerror('Error','Enter valid Email id!')
        return
        
    ga=gaddress.get(1.0,END)    #'''guard address'''
    
    if (l=='' or p=='' or f=='' or y=='' or m=='' or d=='' or s=='' or v=='' or m=='' or e=='' or
        st=='' or lo=='' or p_s=='' or p_o=='' or d=='' or ci=='' or ur=='' or state=='' or co=='' or pin=='' or
        na=='' or occ=='' or cn=='' or ea=='' or ga==''):
        tkinter.messagebox.showwarning('','Please fill all the required fields')
        return

    #............................MARKS....................................................................................

    sch=school.get()
    boa=board.get()
    mat=maths.get()
    phys=phy.get()
    che=chem.get()
    mat=float(mat)
    phys=float(phys)
    che=float(che)
    if(mat=='' or phys=='' or che==''):
        tkinter.messagebox.showwarning('','Please enter your marks!')
        return
    if(mat>100 or mat<0 or phys>100 or phys<0 or che>100 or che<0):
        tkinter.messagebox.showerror('','Marks should be positive and less than 100!')
        return

    zz=tkinter.messagebox.askyesno("sc calc",'Are you sure you want to submit?')
    if zz>0:
        file=open('p.csv')
        list=[row for row in csv.DictReader(file)]
        file.close()
        if len(list)==0:
            file=open('p.csv','w')
            field=['last_name','first_name','DOB','sex','V/NV','Ph_no.','Mobile_no.','Email',
                   'Street','Locality','Police_Station','Post_office','District','City','Urban/Rural','State','Country','Pin',
                   'Guardian_name','Occupation','Contact','G_Email','G_Address',
                   'School','Board','Maths','Physics','Chem','TOTAL']
            w=csv.DictWriter(file,fieldnames=field)
            w.writeheader()
            w.writerow({'last_name':l,'first_name':f,'DOB':DOB,'sex':l2[s-1],'V/NV':l3[v-1],'Ph_no.':p,'Mobile_no.':m,'Email':e,
                   'Street':st,'Locality':lo,'Police_Station':p_s,'Post_office':p_o,'District':d,'City':ci,'Urban/Rural':l4[ur-1],'State':sta,'Country':co,'Pin':pi,
                    'Guardian_name':na,'Occupation':occ,'Contact':cn,'G_Email':ea,'G_Address':ga,
                    'School':sch,'Board':boa,'Maths':mat,'Physics':phys,'Chem':che,'TOTAL':ev})
            file.close()

        else:
            file= open('p.csv','a')
            w=csv.writer(file,delimiter=',')
            w.writerow([l,f,DOB,l2[s-1],l3[v-1],p,m,e,
                        st,lo,p_s,p_o,d,ci,l4[ur-1],sta,co,pi,
                        na,occ,cn,ea,ga,
                        sch,boa,mat,phys,che,ev])
            file.close()
        #____________________________________________________
        last_name.delete(0,END)
        first_name.delete(0,END)
        phone.delete(0,END)
        year.delete(0,END)
        month.delete(0,END)
        day.delete(0,END)
        sex.set(0)
        food.set(0)
        mobile.delete(0,END)
        email.delete(0,END)
        #____________________________________________________
        street.delete(0,END)
        local.delete(0,END)
        ps.delete(0,END)
        po.delete(0,END)
        district.delete(0,END)
        city.delete(0,END)
        ub.set(0)
        state.delete(0,END)
        country.delete(0,END)
        pin.delete(0,END)
        #____________________________________________________
        gname.delete(0,END)
        gocc.delete(0,END)
        gcontact.delete(0,END)
        gemail.delete(0,END)
        gaddress.delete(1.0,END)
        #____________________________________________________
        school.delete(0,END)
        board.delete(0,END)
        maths.delete(0,END)
        phy.delete(0,END)
        chem.delete(0,END)
        total.config(text="Total:")
    else:
        return

def ex():
    ee=tkinter.messagebox.askyesno("sc calc",'Are you sure u want to cancel?')
    if e>0:
        root.destroy()
        return


def res():
    global maths,phy,chem,ev
    try:
        mat=float(maths.get())
        phys=float(phy.get())
        che=float(chem.get())
        ev=mat+phys+che
        total.config(text="Total: %0.2f"%ev)
    except:
        pass
    
    
######``````````````````````````````````````````````````````            FORM PAGE              ````````````````````````````````````````````````````````######
root=Tk()
root.title('Admission Form')
root.geometry('1080x820')

page=Canvas(root)
page.pack(side=LEFT, fill=BOTH)

scrolly=Scrollbar(page, command=page.yview, orient='vertical')
scrolly.pack(side=RIGHT, fill=Y)
page.config(yscrollcommand=scrolly.set)

scrollx=Scrollbar(page, command=page.xview, orient='horizontal')
scrollx.pack(side=BOTTOM, fill=X)
page.config(xscrollcommand=scrollx.set)


logo=Frame(page)
logo.pack()
photo = PhotoImage(file = "Logo.png").subsample(3)
Label(logo, image=photo).grid(column=0, row=0 , rowspan=2)

########################################################            PERSONAL INFO                 ###########################################################
Label(logo, text="St. Thomas' College of Engineering & Technology", font=('Aileron Bold', 22), fg='midnight blue').grid(column=1, row=0, columnspan=5, padx=10)
Label(logo, text="Kolkata, West Bengal", font=('Penna', 15), fg='dark slate blue').grid(column=1, row=1, sticky=W, padx=10)


Person_title=Label(page,fg='white', text='Personal Information', bg='midnight Blue', width=1000).pack(pady=10)
Name=Frame(page)
Name.pack()
Label(Name, text="Last Name: ").grid(column=0, row=0, sticky=E)
last_name=Entry(Name, width=100)
last_name.grid(column=1, row=0, columnspan=20)

Label(Name,text='First and Middle Name: ').grid(column=0, row=1, sticky=E)
first_name=Entry(Name, width=100)
first_name.grid(column=1, row=1, columnspan=20)


Label(Name, text='Date Of Birth: ').grid(column =0, row=2)
Label(Name, text='Year: ', width=10).grid(column=1, row=2, sticky=E)
year=Combobox(Name, width=5)
year['value']=('',)+tuple(i for i in range(1980, datetime.now().year))
year.current(0)
year.grid(column=2, row=2)
#
Label(Name, text='Month: ', width=10).grid(column=3, row=2, sticky=E, pady=10)
month=Combobox(Name, width=5)
month['value']=('',)+tuple(i for i in range(1, 13))
month.current(0)
month.grid(column=4, row=2)
#
Label(Name, text='Day: ',justif=RIGHT,  width=8).grid(column=5, row=2, padx=5)
day=Combobox(Name, width=5)
day['value']=('',)+tuple(i for i in range(1, 32))
day.current(0)
day.grid(column=6, row=2)

sex=StringVar()
sex.set(0)
Label(Name, text='Sex: ').grid(column=7, row=2,padx=20, sticky=E)
rb1=Radiobutton(Name, text="Male", variable=sex, value=1).grid(column=8, row=2)
rb2=Radiobutton(Name, text="Female", variable=sex, value=2).grid(column=9, row=2, padx=10)
rb3=Radiobutton(Name, text="Other", variable=sex, value=3).grid(column=10, row=2)

food=StringVar()
food.set(0)
Label(Name, text='Veg/Non-Veg: ').grid(column=0, row=3)
Radiobutton(Name, text="Veg", variable=food, value=1).grid(column=1, row=3)
Radiobutton(Name, text="Non-Veg", variable=food, value=2).grid(column=2, row=3)

Label(Name, text='Phone Number: ').grid(column=0, row=4, sticky=E)
phone=Entry(Name, width=20)
phone.grid(column=1, row=4, columnspan=2)

Label(Name, text='Mobile Number: ').grid(column=3, row=4, sticky=E)
mobile=Entry(Name, width=20)
mobile.grid(column=4, row=4, columnspan=2)

Label(Name, text='Email Address: ').grid(column=6, row=4, columnspan=2, sticky=E, padx=7)
email=Entry(Name, width=26)
email.grid(column=8, row=4, columnspan=3)

#############################################################      ADDRESS       ###########################################################################

Label(page, text='Permanent Address',bg='midnight Blue', fg='white', width=1000).pack(pady=10)

address=Frame(page)
address.pack()
Label(address, text='Street Name and Number:').grid(column=0, row=0, columnspan=2)
street=Entry(address, width=64)
street.grid(column=2, row=0, columnspan=10, pady=2)

Label(address, text='Locality: ').grid(column=0, row=1)
local=Entry(address, width=20)
local.grid(column=1, row=1)

Label(address, text='Police Station: ').grid(column=2, row=1)
ps=Entry(address, width=20)
ps.grid(column=3, row=1)

Label(address, text='Post Office: ').grid(column=4, row=1)
po=Entry(address, width=20)
po.grid(column=5, row=1)

Label(address, text='District: ').grid(column=0, row=2)
district=Entry(address, width=20)
district.grid(column=1, row=2, pady=2)

Label(address, text='City: ').grid(column=2, row=2)
city=Entry(address, width=20)
city.grid(column=3, row=2)

ub=StringVar()
ub.set(0)
Radiobutton(address, text = "Urban", variable = ub, value = 1).grid(column=4, row=2)
Radiobutton(address, text = "Rural", variable = ub, value = 2).grid(column=5, row=2)

Label(address, text='State: ').grid(column=0, row=3)
state=Entry(address, width=20)
state.grid(column=1, row=3)

Label(address, text='Country: ').grid(column=2, row=3)
country=Entry(address, width=20)
country.grid(column=3, row=3)

Label(address, text='Pin: ').grid(column=4, row=3)
pin=Entry(address, width=20)
pin.grid(column=5, row=3)

###################################################################     Guardians Info     ########################################################################
Label(page, text='Guardian Information',bg='midnight blue', fg='white', width=1000).pack(pady=10)
guard=Frame(page)
guard.pack()

Label(guard, text="Name: ").grid(column=0, row=0, sticky=E)
gname=Entry(guard, width=104)
gname.grid(column=1, row=0, columnspan=8)

Label(guard, text='Occupation: ').grid(column=0, row=4, sticky=E)
gocc=Entry(guard, width=20)
gocc.grid(column=1, row=4, columnspan=2)

Label(guard, text='Contact Number: ').grid(column=3, row=4, sticky=E)
gcontact=Entry(guard, width=20)
gcontact.grid(column=4, row=4, columnspan=2)

Label(guard, text='Email Address: ').grid(column=6, row=4, columnspan=2, sticky=E, padx=7)
gemail=Entry(guard, width=26)
gemail.grid(column=8, row=4, columnspan=3, pady=3)

Label(guard, text='Address: ').grid(column=0, row=5, sticky=N, padx=7)
gadd=Frame(guard)
gadd.grid(column=1, row=5, columnspan=8)

addscroll=Scrollbar(gadd, orient='vertical',bg='ivory4',activebackground='black')
addscroll.pack(side=RIGHT,fill=Y)
gaddress=Text(gadd, height=3, width=90, font=('Calibri', 10),yscrollcommand=addscroll.set)
gaddress.pack(side=LEFT)

addscroll.config( command=gaddress.yview)





#####################################################################     Educational Qualification     ############################################################
Label(page, text='Educational Qualification',bg='midnight blue', fg='white', width=1000).pack(pady=10)
edd=Frame(page)
edd.pack()

Label(edd, text='School: ').grid(column=0, row=0)
school=Entry(edd, width=50)
school.grid(column=1, row=0, columnspan=4)

Label(edd, text='Board: ').grid(column=6, row=0, padx=10)
board=Entry(edd, width=26)
board.grid(column=7, row=0, columnspan=3)

Label(edd, text='Marks',font=('none 10 bold underline'),  width=90).grid(column=0, row=1, columnspan=100, pady=10)
#
Label(edd, text='Maths: ').grid(column=0, row=2, padx=10)
maths=Entry(edd, width=26)
maths.grid(column=1, row=2, columnspan=2)
#
Label(edd, text='Physics: ').grid(column=3, row=2, padx=10)
phy=Entry(edd, width=26)
phy.grid(column=4, row=2, columnspan=2)
#
Label(edd, text='Chemistry: ').grid(column=6, row=2, padx=10)
chem=Entry(edd, width=26)
chem.grid(column=7, row=2, columnspan=2)


#################################################################    Submit   #################################################################
submit=Frame(page)
submit.pack(pady=20)

total= Button(submit, text='Total:', fg='bisque4',width=20,  bd=0, font=('none 10 '),command=lambda:res())
total.grid(column=2, row=0, pady=10)

Label(submit, text="(Tap total to generate total)", fg='bisque4').grid(column=4, row=0, pady=10)

Button(submit, text='CANCEL', fg='white', bg='midnight blue', width=20,command=ex).grid(column=4,row=4, pady=10)
Button(submit, text='SUBMIT', fg='white', bg='midnight blue', width=20,command=add).grid(column=2, row=4, pady=10)

mainloop()
