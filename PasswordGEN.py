#CodSoft Third Task Password Generator in python GUI-based application
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

def generate_password(len):
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    selected_char = random.sample(list_of_chars, len)
    pass_str = "".join(selected_char)
    pass_label.config(text=pass_str)
    print("Generated Password is:", pass_str, "\n")

def selection():
    len = length.get()
    if len != 0:
        generate_password(len)
    else:
        mb.showerror("Invalid Selection", "Length of Password is not defined.")

def get_length():
    print("Selected Length of Password:", length.get(), "characters")

def reset():
    length.set(0)
    pass_label.config(text="")

if __name__ == "__main__":
    gui_root = Tk()
    gui_root.title("Random Password Generator")
    gui_root.geometry("500x350")
    gui_root.config(bg="#f6e0b5")

    heading_frame = Frame(gui_root, bg="#66545e")
    heading_frame.pack(fill="x", pady=10)

    heading = Label(heading_frame, text="RANDOM PASSWORD GENERATOR", font=("Bahnschrift SemiBold", 17), bg="#66545e", fg="#FFFFFF")
    heading.pack(pady=10)

    subheading = Label(heading_frame, text="Customize the Length of the Password:", font=("Bahnschrift SemiBold", 14), bg="#a39193", fg="#FFFFFF")
    subheading.pack(fill="x")

    options_frame = Frame(gui_root, bg="#f6e0b5")
    options_frame.pack(pady=20)

    length = IntVar()
    length.set(0)

    radiobutton_labels = ["4 Characters", "6 Characters", "8 Characters", "10 Characters", "12 Characters", "16 Characters"]
    radiobutton_values = [4, 6, 8, 10, 12, 16]

    for text, value in zip(radiobutton_labels, radiobutton_values):
        Radiobutton(options_frame, text=text, variable=length, value=value, font=("Times New Roman", 12), bg="#f6e0b5", command=get_length).pack(side=LEFT, padx=10)

    button_frame = Frame(gui_root, bg="#f6e0b5")
    button_frame.pack(pady=10)

    get_pass = Button(button_frame, text="Get Password", font=("Bahnschrift SemiBold", 12), width=14, bg="#aa6f73", fg="#FFFFFF", activebackground="#66545e", activeforeground="#FFFFFF", relief=GROOVE, command=selection)
    get_pass.pack(side=LEFT, padx=10)

    clear_all = Button(button_frame, text="Reset", font=("Bahnschrift SemiBold", 12), width=14, bg="#eea990", fg="#FFFFFF", activebackground="#66545e", activeforeground="#FFFFFF", relief=GROOVE, command=reset)
    clear_all.pack(side=LEFT, padx=10)

    result_frame = Frame(gui_root, bg="#f6e0b5")
    result_frame.pack(pady=20)

    pass_label = Label(result_frame, text="", font=("Consolas", 15, "bold"), bg="#f6e0b5", fg="#000000")
    pass_label.pack()

    gui_root.mainloop()
