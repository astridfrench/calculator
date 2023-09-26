#Name: Astrid French

from tkinter import* #python library for GUI

def press_button(num):
    global equation_text #declare global variable

    equation_text = equation_text + str(num) #append to the num buttons
    equation_label.set(equation_text) #set value of the tkinter widget, which is the label


def equals():
    global equation_text

    try: 
        total = str(eval(equation_text)) #to evaluate the string into total variable
        equation_label.set(total) #Set to the total
        equation_text = total

    except SyntaxError:
        equation_label.set("syntax error") #set to "syntax error"
        equation_text = "" #to reset variable to empty

    except ZeroDivisionError:
        equation_label.set("Error") #set to "error" when its divide to 0
        equation_text = "" #to reset variable to empty


def clear():
    global equation_text
    equation_label.set("") #to clear the label empty
    equation_text = "" #to reset variable to empty


window = Tk() #to call from tkinter library and create the window
window.title("Astrid's calculator") #to make the title
window.geometry("500x500") #the size of the window
window.configure(bg="light blue") #the window color

equation_text= ""
equation_label = StringVar()

label =Label(window, textvariable= equation_label, font = ('consolas', 20), bg="#B19CD9", width = 32, height=2)
label.pack()

frame = Frame(window) #to make frame for the bottons
frame.pack()

#to make buttons
button1 = Button(frame, text = 1, height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button(1))
button1.grid(row= 0, column= 0)

button2 = Button(frame, text = 2, height=4 , width = 12, font = 50, bg = "#FFC0CB", 
                 command = lambda: press_button(2))
button2.grid(row= 0, column= 1)

button3 = Button(frame, text = 3, height=4 , width = 12, font = 35, bg ="#FFC0CB", 
                 command = lambda: press_button(3))
button3.grid(row= 0, column= 2)

button4 = Button(frame, text = 4, height=4 , width = 12, font = 35, bg = "#FFC0CB",
                 command = lambda: press_button(4))
button4.grid(row= 1, column= 0)

button5 = Button(frame, text = 5, height=4 , width = 12, font = 35, bg= "#FFC0CB", 
                 command = lambda: press_button(5))
button5.grid(row= 1, column= 1)

button6 = Button(frame, text = 6, height=4 , width = 12, font = 35, bg = "#FFC0CB",
                 command = lambda: press_button(6))
button6.grid(row= 1, column= 2)

button7 = Button(frame, text = 7, height=4 , width = 12, font = 35, bg ="#FFC0CB", 
                 command = lambda: press_button(7))
button7.grid(row= 2, column= 0)

button8 = Button(frame, text = 8, height=4 , width = 12, font = 35, bg = "#FFC0CB",
                 command = lambda: press_button(8))
button8.grid(row= 2, column= 1)

button9 = Button(frame, text = 9, height=4 , width = 12, font = 35, bg= "#FFC0CB", 
                 command = lambda: press_button(9))
button9.grid(row= 2, column= 2)

button0 = Button(frame, text = 0, height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button(0))
button0.grid(row= 3, column= 0)

plus = Button(frame, text = '+', height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button('+'))
plus.grid(row= 0, column= 3)

minus = Button(frame, text = '-', height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button('-'))
minus.grid(row= 1, column= 3)

multiply = Button(frame, text = '*', height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button('*'))
multiply.grid(row= 2, column= 3)

divide = Button(frame, text = '/', height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button('/'))
divide.grid(row= 3, column= 3)

equal = Button(frame, text = '=', height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = equals)
equal.grid(row= 3, column= 2)

decimal = Button(frame, text = '.', height=4 , width = 12, font = 35, bg= "#FFC0CB",
                 command = lambda: press_button('.'))
decimal.grid(row= 3, column= 1)

clear = Button(window, text = 'clear', height=4 , width = 20, font = 35, bg= "#FFC0CB",
                 command = clear)
clear.pack()


window.mainloop()