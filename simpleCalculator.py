from tkinter import *
import time ;
from tkinter import messagebox

root = Tk()
root.geometry("400x650+0+0")
root.title("Goriber Calculator")

textInput= StringVar()
operator = ""

Tops = Frame(root,width= 400, relief= SUNKEN )
Tops.pack(side= TOP)

fr= Frame(root, width= 350, height=600, relief= SUNKEN)
fr.pack(side= TOP)
#==========Time Variable================#
localtime= time.asctime(time.localtime(time.time()))
#================== Title label===========#
lblInfo= Label(Tops, font= ('arial', 18, 'bold'), text= "Goriber Calculator ", fg = "dark red", bd = 10, anchor = 'w')
lblInfo.grid(row=0, column=0)
lblInfo= Label(Tops, font= ('Verdana', 15, 'bold'), text= localtime, fg="orange", bd=10, anchor= 'w' )
lblInfo.grid(row=1, column = 0)
#=============== Method banaisi====================#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)
    



def btnClickDisplay():
    global operator
    operator = ""
    textInput.set("")
def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    textInput.set(sumup)
    operator= ""
def btnClearDisplay():
    global operator
    operator = ""
    textInput.set("")
def squart():
    global operator
    rt= float(operator)**0.5
    textInput.set(rt)
    operator= ""

def Exit():
    if messagebox.askokcancel("Quit", "Thank you to using Goriber Calculator.\n "
                                      "Rate it on my GitHub.\n"
                                      "Inspire me to develop GORIBER SCIENTIFIC Calculator"
                              ):
        root.destroy()



#================Calculator er puran button r display============#
txtDisplay= Entry(fr, font=("verdana", 15, 'bold'), textvariable = textInput, bd= 30,insertwidth = 4, bg='dark blue', justify = 'center' )
txtDisplay.grid(columnspan = 4)


btn7 = Button(fr,padx= 15, pady= 15, bd= 7, fg= 'black',font=('arial', 20, 'bold'),text= "7", bg= "powder blue", command= lambda: btnClick(7)).grid(row=3, column= 0)
btn8 = Button(fr, padx= 15, pady= 15,bd=7, fg='black', font=('arial', 20, 'bold'), text="8", bg= 'powder blue', command = lambda: btnClick(8)).grid(row=3, column=1)
btn9= Button(fr, padx= 15, pady= 15, bd= 7, fg= 'black', font=('arial', 20, 'bold'), text= "9", bg= 'powder blue', command = lambda: btnClick(9)).grid(row=3, column=2)
addition = Button(fr, padx=15, pady= 15, bd=7, fg= 'black', font= ('arial', 20, 'bold'), text= "+", bg= 'powder blue', command= lambda: btnClick('+')).grid(row=3, column=3)

btn4 = Button(fr,padx= 15, pady= 15, bd= 7, fg= 'black',font=('arial', 20, 'bold'),text= "4", bg= "powder blue", command= lambda: btnClick(4)).grid(row=4, column= 0)
btn5 = Button(fr, padx= 15, pady= 15,bd=7, fg='black', font=('arial', 20, 'bold'), text="5", bg= 'powder blue', command = lambda: btnClick(5)).grid(row=4, column=1)
btn6= Button(fr, padx= 15, pady= 15, bd= 7, fg= 'black', font=('arial', 20, 'bold'), text= "6", bg= 'powder blue', command = lambda: btnClick(6)).grid(row=4, column=2)
subtraction = Button(fr, padx=15, pady= 19, bd=7, fg= 'black', font= ('arial', 20, 'bold'), text= "-", bg= 'powder blue', command= lambda: btnClick('-')).grid(row=4, column=3)

btn1 = Button(fr,padx= 15, pady= 15, bd= 7, fg= 'black',font=('arial', 20, 'bold'),text= "1", bg= "powder blue", command= lambda: btnClick(1)).grid(row=5, column= 0)
btn2 = Button(fr, padx= 15, pady= 15,bd=7, fg='black', font=('arial', 20, 'bold'), text="2", bg= 'powder blue', command = lambda: btnClick(2)).grid(row=5, column=1)
btn3= Button(fr, padx= 15, pady= 15, bd= 7, fg= 'black', font=('arial', 20, 'bold'), text= "3", bg= 'powder blue', command = lambda: btnClick(3)).grid(row=5, column=2)
multiply = Button(fr, padx=15, pady= 15, bd=7, fg= 'black', font= ('arial', 20, 'bold'), text= "X", bg= 'powder blue', command= lambda: btnClick('*')).grid(row=5, column=3)

btn0 = Button(fr,padx= 15, pady= 15, bd= 7, fg= 'black',font=('arial', 20, 'bold'),text= "0", bg= "powder blue", command= lambda: btnClick(0)).grid(row=6, column= 0)
btnDot = Button(fr, padx= 17, pady= 17,bd=7, fg='black', font=('arial', 20, 'bold'), text=".", bg= 'powder blue', command = lambda: btnClick('.')).grid(row=6, column=1)
division = Button(fr, padx=17, pady= 17, bd=7, fg= 'black', font= ('arial', 20, 'bold'), text= "/", bg= 'powder blue', command= lambda: btnClick('/')).grid(row=6, column=2)
equal= Button(fr, padx=15, pady= 15, bd= 7, fg= 'black', font= ('arial', 20, 'bold'),text= '=', bg= 'powder blue', command= lambda:btnEqualInput()).grid(row=6, column=3)

clear = Button(fr, padx= 15, pady = 15, bd= 7, fg = 'black', font= ('arial', 20, 'bold'), text= "C", bg= 'powder blue', command= lambda:btnClearDisplay()).grid(row=7, column= 0)
sqroot = Button(fr, padx= 15, pady= 15, fg= 'black', font= ('arial',20, 'bold'), text="√", bg= 'powder blue', command= lambda:squart()).grid(row=7, column=1)
reset= Button(fr, padx=15, pady= 17, bd= 7, fg= 'black', font=('arial', 15, 'bold'), text='CE', bg= 'powder blue', command= lambda:btnClearDisplay()).grid(row=7, column=2)
thanks= Button(fr, padx= 15, pady=18, bd= 7, fg= 'black', font=('arial', 15,'bold'), text= "Bye", bg= 'powder blue', command=lambda:Exit()).grid(row=7, column=3)


root.mainloop()
