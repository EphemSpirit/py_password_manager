from tkinter import *
from tkinter import messagebox
import string
import secrets

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(12))
    password_input.insert(0, password)
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # Form validation
    if any(entry in ("", None) for entry in [website, email, password]):
        messagebox.showerror("Empty Fields", "Please fill out all fields")
        return

    # confirmation
    answer = messagebox.askquestion("Entry", "Are you sure you want to save this data?", icon="question")
    if answer == "yes":
        with open("password.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

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