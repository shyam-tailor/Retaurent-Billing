from tkinter import *
from tkinter import ttk
import time
import datetime
#-------------------------------All Functions defines Here---------------------------------------------
root=Tk()

root.geometry("500x500")     
#list  for contain all IntVar Objects
l=[IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
   ,IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
#list  for contain all StringVar Objects
l2=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    ,StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    ,StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

l3=[]#contain all entry Objects
l4=[]#contain all the entry value
#list  for contain all Dishes Objects
l7=['Fries','Noodles','Hamburger','Pizza','PavBhaji','Momos','Cheesesandwich','Patiz','Vanila','Butterscotch','Strawberry','ChoclateMuffin','Pencakes','Kulfi','ChoclateCake','Cookies','Tea','Cola','Coffee',
    'Pineapple','BottleWater','ColdCoffee','VanilaShake','Pupaya Shake']
n=len(l7)
print(n)
x=0

def exit():
         root.destroy()
         return

def f1(event):                       
         Totalbutton['bg']='#03f'
         Totalbutton['fg']='#fff'

def g1(event):
         Totalbutton['bg']='#fff'
         Totalbutton['fg']='#03f'

def f2(event):
         Resetbutton['bg']='#03f'
         Resetbutton['fg']='#fff'

def g2(event):
         Resetbutton['bg']='#fff'
         Resetbutton['fg']='#03f'

def f3(event):
         Exitbutton['bg']='#03f'
         Exitbutton['fg']='#fff'

def g3(event):
         Exitbutton['bg']='#fff'
         Exitbutton['fg']='#03f'
l6=[]#contain active itmems

def checkvar(obj):
         global x
         global l6
         x=x+1
         if(obj[0].get()==1):
                  obj[1].configure(state=NORMAL)
                  obj[2].set("")
                  l6.append(obj[3])
                  l10=set(l6)
                  print("l10=",l10)
         elif(obj[0].get()==0):
                  obj[1].configure(state=DISABLED)
                  obj[2].set("0")

def reset():
         for i in l:
                  i.set(0)
         for i in l2:
                  i.set("0")
         for i in l3:
                  i.configure(state=DISABLED)
sh=StringVar()         
                  
for i in l2:
         i.set("0")
         
for i in l3:
         i.configure(state=DISABLED)
l5=[]#contain Entry Value for all the selected Dishes
         
def costofmeal():
         for i in l2:
                  cost=(i.get())
                  l4.append(float(cost))
         itotal=((l4[0]* 50)+(l4[1] * 40)+(l4[2]*30)+(l4[3]*100)+(l4[4]*60)+(l4[5]*60)+
         (l4[6]*50)+(l4[7]*15)+(l4[8]*35)+(l4[9]*60)+(l4[10]*20)+(l4[11]*50)+(l4[12]*30)+(l4[13]*10)+
                (l4[14]*30)+(l4[15]*30)+(l4[16]*30)+(l4[17]*50)+(l4[18]*80)+(l4[19]*60)+(l4[20]*60)+(l4[21]*30)+(l4[22]*30)+
                 (l4[3]*30))
         if (sh.get()=="Cash"):
                  icost=itotal
                  itax=(icost*3.4)/100
                  l[26].set(itax)
                  l[27].set(icost)
                  l[28].set(icost+itax)
                  ichange=int(l2[24].get())
                  chng=ichange-(icost+itax)
                  l[25].set(chng)
         for i in l4:
                  if i!=0:
                           l5.append(i)
         print("l5=",l5)
                  


Top=Frame(root,bd='3',cursor='arrow',height='100',width='100',relief='solid',bg='#03f')
Top.pack(side=TOP)

guilab=Label(Top,font=('arial',41,'bold'),text="     \t         Fast Food Restaurant \t\t       ",fg='#03f',bg='#fff')
guilab.grid(row=0,column=0)

Top1=Frame(root,bd='1',cursor='arrow',height='800',width='1422',relief='solid',bg='#09f')
Top1.pack(side=TOP)

fr1=Frame(Top1,bd='1',cursor='arrow',height='800',width='466',relief='solid',bg='#fff',padx=10)
fr1.pack(side=LEFT)

fr2=Frame(Top1,bd='1',cursor='arrow',height='1200',width='500',relief='raise',bg='#fff')
fr2.pack(side=LEFT)

fr2a=Frame(fr2,bd='1',cursor='arrow',height='600',relief='solid',bg='#fff',padx=18,pady=15)
fr2a.pack(side=TOP)

fr2b=Frame(fr2,bd='1',cursor='dot',height='600',relief='solid',bg='#fff',padx=38,pady=19)
fr2b.pack(side=BOTTOM)

fr3=Frame(Top1,bd='1',cursor='dot',height='800',width='466',relief='raise',bg='#fff',pady=15)
fr3.pack(side=RIGHT)

s=StringVar()
timeandate=Label(fr3,text=s,font=('arial',18,'bold'),pady=15,bg='#fff',fg='#03f')
timeandate.grid(row=13,column=0)

for i in l:
         i.set(0)
for i in l2:
         i.set("0")
def createntry(frame,var,i):
         En=Entry(frame,font=('arial',18,'bold'),textvariable=var,fg='#03f',width=6,justify='right',state=DISABLED)
         En.grid(row=i,column=1)
         l3.append(En)
#--------------------------------------Frame-1 code starts here-------------------------------------
meallab=Label(fr1,font=('arial',18,'bold'),text="Fast Food",bg='#fff',fg='#03f')
meallab.grid(row=0,column=0)

createntry(fr1,l2[0],1)
Fries=Checkbutton(fr1,text="Fries\t\t     50Rs",variable=l[0],offvalue=0,onvalue=1,font=('arial',18,'bold'),bg='#fff',fg='#03f'
                  ,command=lambda x=(l[0],l3[0],l2[0],l7[0]):checkvar(x))
Fries.grid(row=1,column=0,sticky=W)


createntry(fr1,l2[1],2)
Salad=Checkbutton(fr1,text="Noodles\t\t     40Rs",variable=l[1],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[1],l3[1],l2[1],l7[1]):checkvar(x),bg='#fff',fg='#03f')
Salad.grid(row=2,column=0,sticky=W)

createntry(fr1,l2[2],3)
Hamburger=Checkbutton(fr1,text="HamBurger\t     30Rs",variable=l[2],offvalue=0,onvalue=1,
         font=('arial',18,'bold'),command=lambda x=(l[2],l3[2],l2[2],l7[2]):checkvar(x),bg='#fff',fg='#03f')
Hamburger.grid(row=3,column=0,sticky=W)

createntry(fr1,l2[3],4)
Pizza=Checkbutton(fr1,text="Pizza\t\t   100Rs",variable=l[3],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[3],l3[3],l2[3],l7[3]):checkvar(x),bg='#fff',fg='#03f')
Pizza.grid(row=4,column=0,sticky=W)

createntry(fr1,l2[4],5)
pavbhaji=Checkbutton(fr1,text="PavBhaji\t\t     60Rs",variable=l[4],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[4],l3[4],l2[4],l7[4]):checkvar(x),bg='#fff',fg='#03f')
pavbhaji.grid(row=5,column=0,sticky=W)

createntry(fr1,l2[5],6)
Momos=Checkbutton(fr1,text="Momos\t\t     60Rs",variable=l[5],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[5],l3[5],l2[5],l7[5]):checkvar(x),bg='#fff',fg='#03f')
Momos.grid(row=6,column=0,sticky=W)

createntry(fr1,l2[6],7)
CheeseSandwich=Checkbutton(fr1,text="CheeseSandwich\t     50Rs",variable=l[6],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[6],l3[6],l2[6],l7[6]):checkvar(x),bg='#fff',fg='#03f')
CheeseSandwich.grid(row=7,column=0,sticky=W)
                         
createntry(fr1,l2[7],8)                         
patiz=Checkbutton(fr1,text="Patiz\t\t     15Rs",variable=l[7],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[7],l3[7],l2[7]):checkvar(x),bg='#fff',fg='#03f')
patiz.grid(row=8,column=0,sticky=W)

IceandShakeslab=Label(fr1,font=('arial',18,'bold'),text="\nIceCream and Shakes\n",bg='#fff',fg='#03f')
IceandShakeslab.grid(row=9,column=0)

createntry(fr1,l2[8],10)
Vanila=Checkbutton(fr1,text="Vanila\t\t    30Rs",variable=l[8],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[8],l3[8],l2[8],l7[8]):checkvar(x),bg='#fff',fg='#03f')
Vanila.grid(row=10,column=0,sticky=W)

createntry(fr1,l2[9],11)
ButterScotch=Checkbutton(fr1,text="butterscotch\t     30Rs",variable=l[9],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[9],l3[9],l2[9],l7[9]):checkvar(x),bg='#fff',fg='#03f')
ButterScotch.grid(row=11,column=0,sticky=W)

createntry(fr1,l2[10],12)
Strawberry=Checkbutton(fr1,text="Strawberrry\t     30Rs",variable=l[10],offvalue=0,onvalue=1,
                  font=('arial',18,'bold'),command=lambda x=(l[10],l3[10],l2[10],l7[10]):checkvar(x),bg='#fff',fg='#03f')
Strawberry.grid(row=12,column=0,sticky=W)

lablspace=Label(fr1,text="\n\n\n\n\n\n\n\n\n\n",bg='#fff')
lablspace.grid(row=13,column=1)
#--------------------------------------Frame-1 code ends here---------------------------------------
#--------------------------------------Frame-2 top part code starts here-------------------------------------
dessertslab=Label(fr2a,font=('arial',20,'bold'),text="  \tDesserts      ",bg='#fff',fg='#03f')
dessertslab.grid(row=0,column=0)

createntry(fr2a,l2[11],1)
HashBrown=Checkbutton(fr2a,text="ChoclateMuffin\t        35Rs ",variable=l[11],offvalue=0,onvalue=1,
         font=('arial',18,'bold'),command=lambda x=(l[11],l3[11],l2[11],l7[11]):checkvar(x),bg='#fff',fg='#03f')
HashBrown.grid(row=1,column=0,sticky=W)

createntry(fr2a,l2[12],2)
ToastedBagel=Checkbutton(fr2a,text="Pencakes\t        60Rs ",variable=l[12],offvalue=0,onvalue=1,
         font=('arial',18,'bold'),command=lambda x=(l[12],l3[12],l2[12],l7[12]):checkvar(x),bg='#fff',fg='#03f')
ToastedBagel.grid(row=2,column=0,sticky=W)

createntry(fr2a,l2[13],3)
PancakesSyrup=Checkbutton(fr2a,text="Kulfi\t\t        20Rs ",variable=l[13],offvalue=0,onvalue=1,
                  command=lambda x=(l[13],l3[13],l2[13],l7[13]):checkvar(x),font=('arial',18,'bold'),bg='#fff',fg='#03f')
PancakesSyrup.grid(row=3,column=0,sticky=W)

createntry(fr2a,l2[14],4)
Pineapplestick=Checkbutton(fr2a,text="ChoclateCake\t        50Rs ",variable=l[14],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[14],l3[14],l2[14],l7[14]):checkvar(x),bg='#fff',fg='#03f')
Pineapplestick.grid(row=4,column=0,sticky=W)

createntry(fr2a,l2[15],5)
ChocolateMuffin=Checkbutton(fr2a,text="Cookies\t\t        30Rs",variable=l[15],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[15],l3[15],l2[15],l7[15]):checkvar(x),bg='#fff',fg='#03f')
ChocolateMuffin.grid(row=5,column=0,sticky=W)

lablspace=Label(fr2a,text="\n\n\n\n\n",bg='#fff')
lablspace.grid(row=9,column=1)
#--------------------------------------Frame2 top part coding ends-----------------------------------
#--------------------------------------Frame2 Bottom part coding starts-----------------------------------
Paymentlab=Label(fr2b,font=('arial',18,'bold'),text="Payment Method",bg='#fff',fg='#03f')
Paymentlab.grid(row=0,column=0)

combpaymentmethod=ttk.Combobox(fr2b,textvariable=sh,state='readonly',font=('arial',10,'bold'),width=20)
combpaymentmethod['value']=('Cash','Master Card','Visa Card','Debit Card')
combpaymentmethod.current(0)
combpaymentmethod.grid(row=1,column=0)

changelab=Label(fr2b,font=('arial',18,'bold'),text="Change",bg='#fff',fg='#03f')
changelab.grid(row=1,column=1)
txtChange=Entry(fr2b,font=('arial',18,'bold'),textvariable=l[25],width=6,fg='#03f',justify='right',state=DISABLED)
txtChange.grid(row=1,column=2)

taxlab=Label(fr2b,font=('arial',18,'bold'),text="Tax",bg='#fff',fg='#03f')
taxlab.grid(row=2,column=1)
txtTax=Entry(fr2b,font=('arial',18,'bold'),textvariable=l[26],width=6,fg='#03f',justify='right',state=DISABLED)
txtTax.grid(row=2,column=2)

subtotallab=Label(fr2b,font=('arial',18,'bold'),text="Sub Total",bg='#fff',fg='#03f')
subtotallab.grid(row=3,column=1)
txtSubTotal=Entry(fr2b,font=('arial',18,'bold'),textvariable=l[27],width=6,justify='right',state=DISABLED)
txtSubTotal.grid(row=3,column=2)

totallab=Label(fr2b,font=('arial',18,'bold'),text="Total",bg='#fff',fg='#03f')
totallab.grid(row=4,column=1)
txtTotal=Entry(fr2b,font=('arial',18,'bold'),textvariable=l[28],width=6,fg='#03f',justify='right',state=DISABLED)
txtTotal.grid(row=4,column=2)

Amount=Entry(fr2b,font=('arial',18,'bold'),textvariable=l2[24],width=6,fg='#03f',justify='right',state=NORMAL)
Amount.grid(row=3,column=0)

Totalbutton=Button(fr2b,font=('arial',18,'bold'),bd=1,padx=18,pady=1,fg='#03f',bg='#fff',text="Total",
                   width=3,command=costofmeal,relief='solid')
Resetbutton=Button(fr2b,font=('arial',18,'bold'),bd=1,padx=18,pady=1,text="Reset",
                   width=3,command=reset,fg='#03f',bg='#fff')
Exitbutton=Button(fr2b,font=('arial',18,'bold'),bd=1,padx=18,pady=1,text="Exit",
                   width=3,command=lambda:exit(),fg='#03f',bg='#fff')
Totalbutton.bind("<Enter>",f1)
Totalbutton.bind("<Leave>",g1)
Totalbutton.grid(row=6,column=0)
Resetbutton.bind("<Enter>",f2)
Resetbutton.bind("<Leave>",g2)
Resetbutton.grid(row=6,column=1)
Exitbutton.bind("<Enter>",f3)
Exitbutton.bind("<Leave>",g3)
Exitbutton.grid(row=6,column=2,pady=10)

lablspace=Label(fr2b,text="\n\n\n\n\n",bg='#fff')
lablspace.grid(row=10,column=1)
#--------------------------------------Frame2 bottom part coding ends-----------------------------------
Drinkslab=Label(fr3,font=('arial',18,'bold'),text="Drinks",bg='#fff',fg='#03f')
Drinkslab.grid(row=0,column=0)

createntry(fr3,l2[16],1)
Tea=Checkbutton(fr3,text="Tea     \t\t        10Rs",variable=l[16],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[16],l3[16],l2[16],l7[16]):checkvar(x),bg='#fff',fg='#03f').grid(row=1,column=0,sticky=W)

createntry(fr3,l2[17],2)
Cola=Checkbutton(fr3,text="Cola     \t\t        30Rs",variable=l[17],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[17],l3[17],l2[17],l7[17]):checkvar(x),bg='#fff',fg='#03f')
Cola.grid(row=2,column=0,sticky=W)

createntry(fr3,l2[18],3)
Coffee=Checkbutton(fr3,text="Coffee     \t        30Rs",variable=l[18],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[18],l3[18],l2[18],l7[18]):checkvar(x),bg='#fff',fg='#03f')
Coffee.grid(row=3,column=0,sticky=W)

createntry(fr3,l2[19],4)
Pineapple=Checkbutton(fr3,text="Pineapple     \t        30Rs",variable=l[19],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[19],l3[19],l2[19],l7[19]):checkvar(x),bg='#fff',fg='#03f')
Pineapple.grid(row=4,column=0,sticky=W)

createntry(fr3,l2[20],5)
BottleWater=Checkbutton(fr3,text="BottleWate     \t        50Rs",variable=l[20],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[20],l3[20],l2[20],l7[20]):checkvar(x),bg='#fff',fg='#03f')
BottleWater.grid(row=5,column=0,sticky=W)

createntry(fr3,l2[21],6)
ColdCoffee=Checkbutton(fr3,text="Cold Coffee     \t        80Rs",variable=l[21],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[21],l3[21],l2[21],l7[21]):checkvar(x),bg='#fff',fg='#03f')
ColdCoffee.grid(row=6,column=0,sticky=W)

Shakeslab=Label(fr3,font=('arial',19,'bold'),text="\n Shakes\n ",bg='#fff',fg='#03f')
Shakeslab.grid(row=7,column=0)

createntry(fr3,l2[22],8)
VanilaShake=Checkbutton(fr3,text="Vanila Shake     \t        60Rs",variable=l[22],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[22],l3[22],l2[22],l7[22]):checkvar(x),bg='#fff',fg='#03f')
VanilaShake.grid(row=8,column=0,sticky=W)

createntry(fr3,l2[23],9)
Vanilacone=Checkbutton(fr3,text="Pupaya Shake     \t        70Rs",variable=l[23],offvalue=0,onvalue=1,font=('arial',18,'bold'),command=lambda x=(l[23],l3[23],l2[23],l7[23]):checkvar(x),bg='#fff',fg='#03f')
Vanilacone.grid(row=9,column=0,sticky=W)

lablspace=Label(fr3,text="\n\n\n\n\n",bg='#fff')
lablspace.grid(row=10,column=1)
lablspace=Label(fr3,text="\n\n\n\n\n\n",bg='#fff')
lablspace.grid(row=14,column=1)

k=1

def secwin():
         root.iconify()
         root1=Tk()
         root1.geometry('500x500')
         Topframe=Frame(root1,bd='2',height=830,width=1500,relief=SOLID,bg='#0c161c')
         Topframe.place(x=0,y=0)

         Firmlab=Label(Topframe,font=('arial',25,'bold'),text='Fast Food Restaurent',bg='#0c161c',fg='#fff')
         Firmlab.place(x=570,y=0)

         #-------------------------------------Label and Entry starts here------------------------------------------------------


         Firmlab=Label(Topframe,font=('arial',18,'bold'),text='Reciept No',bg='#0c161c',fg='#fff')
         Firmlab.place(x=0,y=50+60)
         E1=Entry(Topframe,font=('arial',18,'bold'),fg='#0c161c',width=10,justify='right',state=NORMAL)
         E1.place(x=300,y=50+60)


         Datelab=Label(Topframe,font=('arial',18,'bold'),text='Date',bg='#0c161c',fg='#fff')
         Datelab.place(x=1050,y=50+60)
         E2=Entry(Topframe,font=('arial',18,'bold'),fg='#0c161c',width=10,justify='left',state=NORMAL)
         E2.place(x=1280,y=50+60)


         Stulab=Label(Topframe,font=('arial',18,'bold'),text='Customer Name',bg='#0c161c',fg='#fff')
         Stulab.place(x=0,y=50+120)
         E1=Entry(Topframe,font=('arial',18,'bold'),fg='#0c161c',width=30,justify='left',state=NORMAL)
         E1.place(x=300,y=50+120)
         print(l6)
         listbox=Listbox(root1,height=300,width=500)
         listbox.place(x=1000,y=100)
         for i in range(n):
                  global k
                  listbox.insert(k,(l10[i],l5[i]))
                  k=k+1
         
                  
         
         


         #---------------------------------------Label and Entry ends here------------------------------------------------------

         #---------------------------------------Button codes Start Here--------------------------------------
         bt=Button(Topframe,relief='solid',width=6,height=1,bd='2',text="Submit",font=('arial',18,'bold'))
         bt.place(x=700,y=50+700)

         bt2=Button(Topframe,relief='solid',width=6,height=1,bd='2',text="Reset",font=('arial',18,'bold'))
         bt2.place(x=900,y=50+700)
         #---------------------------------------Button codes Ends Here-------------------------------------

                  



def f():
         global timeandate,s
         timeandate['text']=time.ctime()
         root.after(1000,f)
f()

root.mainloop()
