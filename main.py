from tkinter import *
from tkinter import messagebox


def reset():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def calculate_bmi():
    weight_in_kilograms = int(weight_tf.get())
    height_in_meters = int(height_tf.get()) / 100
    if weight_in_kilograms == 0 or height_in_meters == 0:
        messagebox.showerror('Invalid',"Please enter valid information")
    else:
        bmi = weight_in_kilograms / (height_in_meters ** 2)
        bmi = round(bmi, 2)
        if bmi < 18.5:
            messagebox.showinfo('Underweight', f'BMI = {bmi}\n Category: Underweight')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('Normal', f'BMI = {bmi}.\n Category: Normal')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('Overweight', f'BMI = {bmi}.\n Category: Overweight')
        elif (bmi > 29.9):
            messagebox.showinfo('Obese', f'BMI = {bmi}.\n Category: Obese')
        elif (bmi > 34.9):
            messagebox.showinfo('Morbidly Obese', f'BMI = {bmi}.\n Category: Morbidly Obese')
        else:
            messagebox.showerror('Invalid!', 'Enter correct data')


ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x200')
ws.config(bg='#020803')

var = IntVar()

frame = Frame(
    ws,
    padx=80,
    pady=40
)
frame.pack(fill=BOTH, expand=True)
height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)


weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
