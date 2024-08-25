from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json



def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)
def search():
    website_n = entry_1.get()
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data File Found!")
    else:
        if website_n in data:
            messagebox.showinfo(title=website_n, message=f"Email: {data[website_n]['email']}\nPassword: {data[website_n]["password"]}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website_n} exists")
    finally:
        entry_1.delete(0, END)
        entry_3.delete(0, END)
        entry_1.focus()

def save_password():
    website_n = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {
        website_n: {
            "email": email,
            "password": password
        }
    }

    if len(website_n) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            entry_1.delete(0, END)
            entry_3.delete(0, END)
            entry_1.focus()

window = Tk()
window.title("Password Manager")
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

#Labels
label_1 = Label(text="Website:")
label_1.config(padx=5, pady=5)
label_1.grid(row=1, column=0)

label_2 = Label(text="Email/Username:")
label_2.config(padx=5, pady=5)
label_2.grid(row=2, column=0)

label_3 = Label(text="Password:")
label_3.config(padx=5, pady=5)
label_3.grid(row=3, column=0)

#Entries
entry_1 = Entry(width=20)
entry_1.place(x=110, y=211)
entry_1.focus()

entry_2 = Entry(width=40)
entry_2.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
entry_2.insert(0, "your@email.com")

entry_3 = Entry(width=21)
entry_3.place(x=110, y=265)

#Buttons
button_1 = Button(text="Generate Password", command=generate_password)
button_1.place(x=245, y=262)

button_2 = Button(text="Add", command=save_password)
button_2.config(width=34)
button_2.grid(row=4, column=1, columnspan=2, padx=5, pady=1)

button_3 = Button(text="Search",width=14, command=search)
button_3.place(x=245, y=208)



window.mainloop()


