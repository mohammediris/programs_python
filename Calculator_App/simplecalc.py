from tkinter import*

total_value = 0.0
previous_value = 0.0
previous_op = 'null'
previous_state = 'clear'

def button_click(digit):
    global previous_op
    global previous_state
    current = e.get()
    e.delete(0,END)
    e.insert(0, current + digit)
    previous_state = 'click'
      
def button_clear():
    global total_value
    global previous_op
    global previous_state
    total_value = 0
    e.delete(0,END)
    previous_state ='clear'
    previous_op = ''

def button_add():
    global total_value
    global previous_op
    global previous_state
    if previous_state == 'clear':
        pass
    else:
        str_current_number = e.get()
        e.delete(0,END)
        total_value = float(str_current_number)
        previous_op = 'add'

def button_sub():
    global total_value
    global previous_op
    global previous_state
    if previous_state == 'clear':
        pass
    else:
        str_current_number = e.get()
        e.delete(0,END)
        total_value = float(str_current_number)
        previous_op = 'sub'
            
def button_mul():
    global total_value
    global previous_op
    global previous_state
    if previous_state == 'clear':
        pass
    else:
        str_current_number = e.get()
        e.delete(0,END)
        total_value = float(str_current_number)
        previous_op = 'mul'
    
def button_div():
    global total_value
    global previous_op
    global previous_state
    if previous_state == 'clear':
        pass
    else:
        str_current_number = e.get()
        e.delete(0,END)
        total_value = float(str_current_number)
        previous_op = 'div'
       
def button_equal():
    global total_value
    global previous_op
    global previous_state
    if previous_state == 'clear':
        pass
    else:
        str_current_number = e.get()
        e.delete(0,END)
        if previous_op != 'null':
            if previous_op =='add':
                total_value = float(total_value) + float(str_current_number)
                e.insert(0,str(total_value))
                total_value = 0
                previous_state = 'equal'
                previous_op = 'null'
            elif previous_op =='sub':
                total_value = total_value - float(str_current_number)
                e.insert(0,str(total_value))
                total_value = 0
                previous_state = 'equal'
                previous_op = 'null'
            elif previous_op =='mul':
                total_value = total_value * float(str_current_number)
                e.insert(0,str(total_value))
                total_value = 0
                previous_state = 'equal'
                previous_op = 'null'
            elif previous_op =='div':
                total_value = total_value / float(str_current_number)
                e.insert(0,str(total_value))
                total_value = 0
                previous_state = 'equal'
                previous_op = 'null'
            
        else:
            previous_state = 'clear'



root = Tk()

root.title("Calculator by schoolofiris.org")
root.iconbitmap('picture.ico')
e = Entry(root, width=32,font="Arial",justify=['right'],borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

# defining buttons
button_1 = Button(root,text = '1',font = "Arial",padx=34,pady=14,command= lambda: button_click('1'))
button_2 = Button(root,text = '2',font = "Arial",padx=34,pady=14,command=lambda: button_click('2'))
button_3 = Button(root,text = '3',font = "Arial",padx=34,pady=14,command=lambda: button_click('3'))
button_4 = Button(root,text = '4',font = "Arial",padx=34,pady=14,command=lambda: button_click('4'))
button_5 = Button(root,text = '5',font = "Arial",padx=34,pady=14,command=lambda: button_click('5'))
button_6 = Button(root,text = '6',font = "Arial",padx=34,pady=14,command=lambda: button_click('6'))
button_7 = Button(root,text = '7',font = "Arial",padx=34,pady=14,command=lambda: button_click('7'))
button_8 = Button(root,text = '8',font = "Arial",padx=34,pady=14,command=lambda: button_click('8'))
button_9 = Button(root,text = '9',font = "Arial",padx=34,pady=14,command=lambda: button_click('9'))
button_0 = Button(root,text = '0',font = "Arial",padx=34,pady=14,command=lambda: button_click('0'))
button_dot = Button(root,text = '.',font = "Arial",padx=36,pady=14,command=lambda: button_click('.'))
button_add = Button(root,text = '+',font = "Arial",padx=32,pady=50,command=button_add)
button_multiply = Button(root,text = 'x',font = "Arial",padx=32,pady=14,command=button_mul)
button_division = Button(root,text = '/',font = "Arial",padx=34,pady=14,command=button_div)
button_subtract = Button(root,text = '-',font = "Arial",padx=34,pady=14,command=button_sub)
button_equal = Button(root,text = '=',font = "Arial",padx=129,pady=15,command=button_equal)
button_clear = Button(root,text = 'C',font = "Arial",padx=32,pady=14,command=button_clear)
# buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_clear.grid(row=4,column=2)
button_add.grid(row=4,column=3,rowspan=2)
button_equal.grid(row=5,column=0,columnspan=3)
button_multiply.grid(row=1,column=3)
button_division.grid(row=2,column=3)
button_subtract.grid(row=3,column=3)

root.mainloop()
