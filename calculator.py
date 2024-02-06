from tkinter import *

calci=Tk()
calci.title('CALCULATOR')
calci.geometry('455x425')
calci.resizable(0, 0)

#Function
def btn_click(item):
    global equation
    equation=equation+str(item)
    input_text.set(equation)

def btn_clear():
    global equation
    equation= ""
    input_text.set("")

def btn_equal():
    global equation
    result=str(eval(equation))    
    input_text.set(result)
    equation= ""

equation= ""
input_text=StringVar()    

#Input Field Frame
input=Frame(calci, width=275, height=90)
input.pack(side=TOP)
input_field=Entry(input, font=('arial',18,'bold'), width=65, justify=RIGHT,textvariable=input_text)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

#Button Frame
btn_frame=Frame(calci, width=350, height=310)
btn_frame.pack()

#Button 0th Row
clear=Button(btn_frame,text="C",width=40,height=4,command=lambda:btn_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btn_frame,text="/",width=12,height=4,command=lambda:btn_click('/')).grid(row=0,column=3,padx=1,pady=1)

#Button 1st Row
seven=Button(btn_frame,text="7",width=12,height=4,command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,text="8",width=12,height=4,command=lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text="9",width=12,height=4,command=lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btn_frame,text="*",width=12,height=4,command=lambda:btn_click('*')).grid(row=1,column=3,padx=1,pady=1)

#Button 2nd Row
four=Button(btn_frame,text="4",width=12,height=4,command=lambda:btn_click(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,text="5",width=12,height=4,command=lambda:btn_click(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(btn_frame,text="6",width=12,height=4,command=lambda:btn_click(6)).grid(row=2,column=2,padx=1,pady=1)
sub=Button(btn_frame,text="-",width=12,height=4,command=lambda:btn_click('-')).grid(row=2,column=3,padx=1,pady=1)

#Button 3rd Row
one=Button(btn_frame,text="1",width=12,height=4,command=lambda:btn_click(1)).grid(row=3,column=0,padx=1,pady=1)
two=Button(btn_frame,text="2",width=12,height=4,command=lambda:btn_click(2)).grid(row=3,column=1,padx=1,pady=1)
three=Button(btn_frame,text="3",width=12,height=4,command=lambda:btn_click(3)).grid(row=3,column=2,padx=1,pady=1)
add=Button(btn_frame,text="+",width=12,height=4,command=lambda:btn_click('+')).grid(row=3,column=3,padx=1,pady=1)

#Button 4th Row
zero=Button(btn_frame,text="0",width=12,height=4,command=lambda:btn_click(0)).grid(row=4,column=0,padx=1,pady=1)
decimal=Button(btn_frame,text=".",width=12,height=4,command=lambda:btn_click('.')).grid(row=4,column=1,padx=1,pady=1)
equal_to=Button(btn_frame,text="=",width=26,height=4,command=lambda:btn_equal()).grid(row=4,column=2,columnspan=3,padx=1,pady=1)

calci.mainloop()
