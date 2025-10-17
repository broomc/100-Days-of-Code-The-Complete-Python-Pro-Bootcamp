from tkinter import *


def calculate():
    #print("I got clicked")
    #print(input.get())
    miles = float(input.get())
    km = miles*1.60934
    rounded_km = round(km,1)
    print(f"Kilometres = {km}")
    result_label.config(text=rounded_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#Labels
is_equal_to_label = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

Km_label = Label(text="Km", font=("Arial", 16, "bold"))
Km_label.grid(column=2, row=1)
Km_label.config(padx=10, pady=10)

result_label = Label(text="0", font=("Arial", 16, "bold"))
result_label.grid(column=1,row=1)
result_label.config(padx=10,pady=10)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)









window.mainloop()