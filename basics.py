# This is a class that I am going to be using to make sure I
# remember everything I need to know about Python. That way,
# when the mentoring thing comes up, I remember all I learned 
# last semester with Vaskar.
# There's also the fact that Python is a very utilized language,
# and it would just be better for me to be comfortable with it

import tkinter as tk

calculation = ""

def add_calc(sym) :
    global calculation
    calculation += str(sym)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def eval_calc() :
    global calculation
    try :
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    # eval technically a security issue. also runs py code
    # someone could inject py code into file or system
    # if this were a real file on the internet
    except :
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field() :
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()

root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan = 5)

btn_1 = tk.Button(root, text="1", command=lambda: add_calc(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_calc(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_calc(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_calc(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_calc(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_calc(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_calc(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_calc(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_calc(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_div = tk.Button(root, text="0", command=lambda: add_calc(0), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=2)

btn_dot = tk.Button(root, text="+", command=lambda: add_calc("+"), width=5, font=("Arial", 14))
btn_dot.grid(row=2, column=4)

btn_plus = tk.Button(root, text="-", command=lambda: add_calc("-"), width=5, font=("Arial", 14))
btn_plus.grid(row=3, column=4)

btn_min = tk.Button(root, text="*", command=lambda: add_calc("*"), width=5, font=("Arial", 14))
btn_min.grid(row=4, column=4)

btn_eq = tk.Button(root, text="/", command=lambda: add_calc("/"), width=5, font=("Arial", 14))
btn_eq.grid(row=5, column=4)

btn_neg = tk.Button(root, text="=", command=lambda: eval_calc(), width=5, font=("Arial", 14))
btn_neg.grid(row=6, column=4)

btn_neg = tk.Button(root, text="C", command=lambda: clear_field(), width=5, font=("Arial", 14))
btn_neg.grid(row=6, column=3)

btn_neg = tk.Button(root, text="(", command=lambda: add_calc("("), width=5, font=("Arial", 14))
btn_neg.grid(row=6, column=1)

btn_neg = tk.Button(root, text=")", command=lambda: add_calc(")"), width=5, font=("Arial", 14))
btn_neg.grid(row=6, column=2)

btn_neg = tk.Button(root, text=".", command=lambda: add_calc("."), width=5, font=("Arial", 14))
btn_neg.grid(row=5, column=1)

root.mainloop()
