from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)


#label
my_label = Label(text="I am a Label", font=("Arial",24,"bold"))
#my_label.pack(side="left")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#button

def button_clicked():
    my_label.config(text="I got Clicked")

button1 = Button(text="Click Me", command=button_clicked)
button1.pack()

my_label2 = Label(text="Display Text", font=("Arial",24,"bold"))
#my_label.pack(side="left")
my_label2.pack()

def button2_clicked():
    my_label2.config(text=input.get())

button2 = Button(text="Display text input", command=button2_clicked)
button2.pack()


#entry
input = Entry(width=10)
input.pack()

window.mainloop()