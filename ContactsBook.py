#CodSoft Fifth Task Contacts Book in python GUI-based application
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x500')
root.title('Contact Management System')
root.config(bg='#cbdbcd')  

Name = StringVar()
Number = StringVar()

contacts = []  # List to store contacts

input_frame = Frame(root, bg='#cc8f8f', padx=20, pady=20)
input_frame.pack(pady=30, padx=30, fill=BOTH, expand=True)

list_frame = Frame(root, bg='#cc8f8f', padx=20, pady=20)
list_frame.pack(pady=10, padx=30, fill=BOTH, expand=True)

button_frame = Frame(root, bg='#cc8f8f')
button_frame.pack(pady=10, padx=30)

label_font = ('Helvetica', 14, 'bold')
entry_font = ('Helvetica', 12)
button_font = ('Helvetica', 12, 'bold')

Label(input_frame, text='Name:', font=label_font, bg='#cc8f8f').grid(row=0, column=0, padx=10, pady=10, sticky=W)
Entry(input_frame, textvariable=Name, width=50, font=entry_font).grid(row=0, column=1, padx=10, pady=10)

Label(input_frame, text='Phone No.:', font=label_font, bg='#cc8f8f').grid(row=1, column=0, padx=10, pady=10, sticky=W)
Entry(input_frame, textvariable=Number, width=50, font=entry_font).grid(row=1, column=1, padx=10, pady=10)

Label(input_frame, text='Address:', font=label_font, bg='#cc8f8f').grid(row=2, column=0, padx=10, pady=10, sticky=NW)
address = Text(input_frame, width=45, height=5, font=entry_font)
address.grid(row=2, column=1, padx=10, pady=10, sticky=NW)

scroll_bar = Scrollbar(list_frame, orient=VERTICAL)
select = Listbox(list_frame, yscrollcommand=scroll_bar.set, height=12, font=entry_font)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.pack(padx=10, pady=10, fill=BOTH, expand=True)

def add_contact():
    name = Name.get()
    number = Number.get()
    addr = address.get("1.0", END)

    if name.strip() == '' or number.strip() == '' or addr.strip() == '':
        messagebox.showerror("Error", "Please fill all fields.")
        return

    contact_info = f"{name}  |  {number}  |  {addr}"
    contacts.append(contact_info)  # Add contact to the list
    select.insert(END, contact_info)

    Name.set('')
    Number.set('')
    address.delete("1.0", END)

def delete_contact():
    selected_index = select.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return
    
    contacts.pop(selected_index[0])  # Remove contact from the list
    select.delete(selected_index)

def view_contact():
    selected_index = select.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a contact to view.")
        return
    
    selected_contact = select.get(selected_index)
    messagebox.showinfo("Contact Details", selected_contact)

def reset_fields():
    Name.set('')
    Number.set('')
    address.delete("1.0", END)
    select.delete(0, END)

def search_contact():
    query = Name.get().strip().lower()
    select.delete(0, END)

    for contact in contacts:
        if query in contact.lower():
            select.insert(END, contact)

def update_contact():
    selected_index = select.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a contact to update.")
        return

    name = Name.get()
    number = Number.get()
    addr = address.get("1.0", END)

    if name.strip() == '' or number.strip() == '' or addr.strip() == '':
        messagebox.showerror("Error", "Please fill all fields.")
        return

    updated_contact = f"{name}  |  {number}  |  {addr}"
    contacts[selected_index[0]] = updated_contact
    select.delete(selected_index)
    select.insert(selected_index, updated_contact)

Button(button_frame, text="Add", font=button_font, bg='#63002d', fg='white', width=10, command=add_contact).pack(side=LEFT, padx=10, pady=10)
Button(button_frame, text="View", font=button_font, bg='#63002d', fg='white', width=10, command=view_contact).pack(side=LEFT, padx=10, pady=10)
Button(button_frame, text="Delete", font=button_font, bg='#63002d', fg='white', width=10, command=delete_contact).pack(side=LEFT, padx=10, pady=10)
Button(button_frame, text="Reset", font=button_font, bg='#63002d', fg='white', width=10, command=reset_fields).pack(side=LEFT, padx=10, pady=10)

Button(root, text="Search", font=button_font, bg='#63002d', fg='white', width=10, command=search_contact).place(x=400, y=270)
Button(root, text="Update", font=button_font, bg='#63002d', fg='white', width=10, command=update_contact).place(x=500, y=270)

root.mainloop()
