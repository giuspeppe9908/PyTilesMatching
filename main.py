import tkinter as tk
from tkinter import messagebox
import random as random
from random import randint
window = tk.Tk()
window.title("Tris Game")
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)
#print(matches)

count = 0
answer_list = []
answer_dict = {}

def something(b, number):
    global count, answer_list, answer_dict

    if b["text"] == ' ' and count < 2:
            b["text"] = matches[number]
            answer_list.append(number)
            answer_dict[b] = matches[number]
            count += 1
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            mylabel.config(text="MATCH!")
            for key in answer_dict:
                key["fg"] = "green"
                key["bg"] = "yellow"
            count = 0
            answer_list = []
            answer_dict = {}
        else:
            mylabel.config(text="DOH!")
            count = 0
            answer_list = []
            messagebox.showinfo("Incorrect!","Incorrect")
            for key in answer_dict:
                key["text"] = " "
            answer_dict = {}

my_frame = tk.Frame(window)
my_frame.pack(pady=10)
#define buttons
b0 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b0, 0))
b1 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b1, 1))
b2 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b2, 2))
b3 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b3, 3))
b4 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b4, 4))
b5 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b5, 5))
b6 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b6, 6))
b7 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b7, 7))
b8 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b8, 8))
b9 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b9, 9))
b10 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b10, 10))
b11 = tk.Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda:something(b11, 11))
#Grid buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)
b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)
mylabel = tk.Label(window, text="")
mylabel.pack(pady=20)
window.mainloop()