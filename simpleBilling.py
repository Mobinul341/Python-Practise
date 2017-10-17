from tkinter import *
import random
import time
from tkinter import messagebox

root = Tk()
root.geometry('900x700+0+0')
root.title('Goriber Restaurant Billing Software')

textInput = StringVar()
#==============Frames===============#
top = Frame(root, width = 900, relief = SUNKEN)
top.pack(side=TOP)

fr1 = Frame(root, width = 880, height = 600, relief = SUNKEN)
fr1.pack(side= LEFT)

localtime = time.asctime(time.localtime(time.time()))

lebTitle = Label(top, font=('Matura MT Script Capitals', 25, 'bold'), text= "Goriber Food Corner Bill", fg ='green', bd= 10, anchor = 'w' )
lebTitle.grid(row = 0, column =0)
lebTime = Label(top, font = ('Microsoft YaHei UI', 15, 'bold'), text = localtime, fg = 'red', bd = 10, anchor = 'w')
lebTime.grid(row=1, column=0)

#================Restaurant products=============#
rand = StringVar()

rooti = StringVar()
vaji = StringVar()
daal= StringVar()
halua = StringVar()
murgi = StringVar()
khashi = StringVar()
fish = StringVar()
rice = StringVar()
tea= StringVar()

cost = StringVar()
tax = StringVar()
subTotal = StringVar()
total = StringVar()


#===================Billing Funcs==================#

def Ref():
    randNum = random.randint(103, 99999999)
    randRef = str(randNum)
    rand.set(randRef)

    rootiCost = float(rooti.get())
    vajiCost = float(vaji.get())
    daalCost = float(daal.get())
    haluaCost = float(halua.get())
    murgiCost = float(murgi.get())
    khashiCost = float(khashi.get())
    fishCost = float(fish.get())
    riceCost = float(rice.get())
    teaCost = float(tea.get())

    rootirDam = rootiCost * 10
    vajirDam = vajiCost * 20
    daalrDam = daalCost * 20
    haluarDam = haluaCost * 30
    murgirDam = murgiCost * 50
    khashirDam = khashiCost * 100
    fishrDam = fishCost * 40
    ricerDam = riceCost * 30
    tearDam = teaCost * 10

    khabarDam = str('%.2f' %(rootirDam + vajirDam + daalrDam + haluarDam + murgirDam + khashirDam + fishrDam + ricerDam + tearDam)), "Taka"
    khaon = (rootirDam + vajirDam + daalrDam + haluarDam + murgirDam + khashirDam + fishrDam + ricerDam + tearDam)
    taxHishab = ((rootirDam + vajirDam + daalrDam + haluarDam + murgirDam + khashirDam + fishrDam + ricerDam + tearDam)/(15/100))
    shobBill = khaon+taxHishab

    taxDao = str('%.2f'%(taxHishab)), "Taka"
    puraBill = str('%.2f'%(shobBill)), "Taka"
    cost.set(khabarDam)
    subTotal.set(khabarDam)
    tax.set(taxDao)
    total.set(puraBill)

def Reset():
    rand.set("")
    rooti.set("")
    vaji.set("")
    daal.set("")
    halua.set("")
    murgi.set("")
    khashi.set("")
    fish.set("")
    rice.set("")
    tea.set("")
    cost.set("")
    tax.set("")
    subTotal.set("")
    total.set("")

def Exit():
    if messagebox.askokcancel('Exit', "Thank you for using Goriber Restaurant Billing app \n"
                                      "Eat or Don't eat, Rate this project on my GitHub \n"
                                      "Keep inspiring me to develop more."):
        root.destroy()



#=========================================== bill page ==========================#

lblRef = Label(fr1, font=('Segoe UI', 14, 'bold'), text= 'Reference', bd= 10, anchor='w')
lblRef.grid(row = 0, column =0)
txtRef = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = rand, bd= 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtRef.grid(row=0, column=1)

lblRooti = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Rooti', bd= 10, anchor= 'w')
lblRooti.grid(row=1, column=0)
txtRooti = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = rooti, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtRooti.grid(row= 1, column = 1)

lblVaji = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Vaji', bd= 10, anchor= 'w')
lblVaji.grid(row=2, column=0)
txtVaji = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = vaji, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtVaji.grid(row= 2, column = 1)

lblDaal = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Daal', bd= 10, anchor= 'w')
lblDaal.grid(row=3, column=0)
txtDaal = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = daal, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtDaal.grid(row= 3, column = 1)

lblHalua = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Halua', bd= 10, anchor= 'w')
lblHalua.grid(row=4, column=0)
txtHalua = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = halua, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtHalua.grid(row= 4, column = 1)

lblMurgi = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Murgi', bd= 10, anchor= 'w')
lblMurgi.grid(row=5, column=0)
txtMurgi = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = murgi, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtMurgi.grid(row= 5, column = 1)

lblKhashi = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Khashi', bd= 10, anchor= 'w')
lblKhashi.grid(row=6, column=0)
txtKhashi = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = khashi, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtKhashi.grid(row= 6, column = 1)

lblFish = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Fish', bd= 10, anchor= 'w')
lblFish.grid(row=7, column=0)
txtFish = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = fish, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtFish.grid(row= 7, column = 1)

lblRice = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Rice', bd= 10, anchor= 'w')
lblRice.grid(row=8, column=0)
txtRice = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = rice, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtRice.grid(row= 8, column = 1)

lblTea = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Tea', bd= 10, anchor= 'w')
lblTea.grid(row=9, column=0)
txtTea = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = tea, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtTea.grid(row= 9, column = 1)

#===========bill sector=============#

lblCost = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Cost', bd= 10, anchor= 'w')
lblCost.grid(row=0, column=2)
txtCost = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = cost, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtCost.grid(row= 0, column = 3)

lblTax = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Tax', bd= 10, anchor= 'w')
lblTax.grid(row=1, column=2)
txtTax = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = tax, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtTax.grid(row= 1, column = 3)

lblSub = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'SubTotal', bd= 10, anchor= 'w')
lblSub.grid(row=2, column=2)
txtSub = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = subTotal, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtSub.grid(row= 2, column = 3)

lblTotal = Label(fr1, font= ('Segoe UI', 14, 'bold'), text = 'Total', bd= 10, anchor= 'w')
lblTotal.grid(row=3, column=2)
txtTotal = Entry(fr1, font=('Segoe UI', 14, 'bold'), textvariable = total, bd = 10, insertwidth = 4, bg = 'orange', justify = 'right')
txtTotal.grid(row= 3, column = 3)

#======================= Executive Buttons============================#
btnTotal = Button(fr1, padx =9, pady= 5, bd = 7, fg = 'red', font=('Segoe UI',12, 'bold' ), text = 'TOTAL', bg= 'green', command = Ref).grid(row=4, column=3)
btnReset = Button(fr1, padx =9, pady= 5, bd = 7, fg = 'yellow', font=('Segoe UI',12, 'bold' ), text = 'CLEAR', bg= 'blue', command = Reset).grid(row=5, column=3)
btnExit = Button(fr1, padx =9, pady= 5, bd = 7, fg = 'green', font=('Segoe UI',15, 'bold' ), text = 'EXIT', bg= 'red', command = Exit).grid(row=7, column=3)















root.mainloop()