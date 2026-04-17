from tkinter import *
from tkinter import messagebox
import string
import secrets
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(12))
    password_input.insert(0, password)
    window.clipboard_append(password)

# ---------------------------- SEARCHING ------------------------------- #

def search():
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No data available to search through.")
    else:
        try:
            val = data[website_input.get()]
        except KeyError:
            messagebox.showinfo(title="No Result", message="No entries for that website name.")
        else:
            messagebox.showinfo(title=website_input.get(),
                                message=f"Email/Username: {val["email"]}.\nPassword: {val["password"]}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Form validation
    if any(entry in ("", None) for entry in [website, email, password]):
        messagebox.showerror(title="Empty Fields", message="Please fill out all fields")
        return

    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("password.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)

        with open("password.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# WEBSITE
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

# SEARCH BUTTON
search_btn = Button(text="Search", width=11, command=search)
search_btn.grid(row=1, column=2)

#EMAIL/USERNAME
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "example@email.com")

# PASSWORD
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_btn = Button(text="Randomize", width=11, command=generate_random_password)
generate_password_btn.grid(row=3, column=2)

# ADD
add_btn = Button(text="Add", width=32, command=save_information)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()