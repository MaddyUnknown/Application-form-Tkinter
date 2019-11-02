from tkinter.ttk import *
from tkinter import *
from datetime import datetime

######``````````````````````````````````````````````````````            FORM PAGE              ````````````````````````````````````````````````````````######
root=Tk()
root.title('Admission Form')
root.geometry('1080x720')

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
Radiobutton(Name, text="Male", variable=sex, value=1).grid(column=8, row=2)
Radiobutton(Name, text="Female", variable=sex, value=2).grid(column=9, row=2, padx=10)
Radiobutton(Name, text="Other", variable=sex, value=3).grid(column=10, row=2)

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
state=Entry(address, width=20)
state.grid(column=3, row=3)

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

gaddress=Text(gadd, height=3, width=90, font=('Calibri', 10))
gaddress.pack(side=LEFT)
addscroll=Scrollbar(gadd, orient='vertical', command=gaddress.yview)
gaddress.config(yscrollcommand=addscroll.set)
addscroll.pack(fill=Y, side=RIGHT)


#####################################################################     Educational Qualification     ############################################################
Label(page, text='Educational Qualification',bg='midnight blue', fg='white', width=1000).pack(pady=10)
edd=Frame(page)
edd.pack()

Label(edd, text='School: ').grid(column=0, row=0)
school=Entry(edd, width=50)
school.grid(column=1, row=0, columnspan=4)

Label(edd, text='Board: ').grid(column=6, row=0, padx=10)
school=Entry(edd, width=26)
school.grid(column=7, row=0, columnspan=3)

Label(edd, text='Marks',font=('bold', 10),  width=90).grid(column=0, row=1, columnspan=100, pady=10)
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

total= Label(edd, text='Total:    ', fg='ivory3', font=('bold', 10),  width=90)
total.grid(column=0, row=3, columnspan=100, pady=10)


#################################################################    Submit   #################################################################
submit=Frame(page)
submit.pack(pady=20)

Button(submit, text='SUBMIT', fg='white', bg='midnight blue', width=20).pack(side=LEFT, padx=20, pady=20)
Button(submit, text='CANCEL', fg='white', bg='midnight blue', width=20).pack(side=LEFT, padx=20)

mainloop()
