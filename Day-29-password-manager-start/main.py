import tkinter
import tkinter.messagebox
import tkinter.ttk
import random
import pyperclip
import json

# ------------------------------ SEARCH PASSWORD -------------------------------- #

def search_pass():
    website = web_input.get()
    with open("web_password.json") as data_file:
        data = json.load(data_file)    
        try:   
            email = data[website]["email"]
            password = data[website]["password"]  
            pyperclip.copy(password) 
            tkinter.messagebox.showinfo(title = "Your Password", message = f"The information for {website} is:\n Email/Username: {email},\n Password: {password}")             
        except KeyError:
           tkinter.messagebox.showerror(title = "Error", message = f"Are you sure you saved {website} password because it's not saved.")
   

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_input.delete(0, "end")
    pass_list = []
    gen_pass = ""
    
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    pass_list = password_letters + password_numbers + password_symbols

    random.shuffle(pass_list)

    # for i in range(0, len(pass_list) - 1):
    #      gen_pass += pass_list[i] 
    gen_pass = "".join(pass_list)

    pass_input.insert(0, f"{gen_pass}")  
    pyperclip.copy(gen_pass)        

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():

    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showerror(title = "Error", message = "You haven't provided us all information to proceed.")
    else:
       # messagebox to confirm
       is_ok = tkinter.messagebox.askokcancel(title = website, message = f"These are the details you entered : \n Email/Username : {email}, \n Password : {password}.\n Is this info correct or not?")

       if is_ok:

         try: 
            with open("web_password.json", "r") as data_file:
               data = json.load(data_file)
               data.update(new_data)
         except:
            data_file = open("web_password.json", "w")
            data_file.close()
            data = new_data
         finally:      
            with open("web_password.json", "w") as data_file:
                json.dump(data, data_file, indent = 4)   

         web_input.delete(0, "end")
         email_input.delete(0, "end")
         email_input.insert(0, "agarwalkatik5123@gmail.com")
         pass_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50)

# Lock image
canvas = tkinter.Canvas(width = 200, height = 200)
lock_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

# Website Label
web_label = tkinter.Label(text = "Website")
web_label.grid(row = 1, column = 0)

# Website Input
web_input = tkinter.Entry(width = 25)
web_input.grid(row = 1, column = 1, columnspan = 2, sticky = "EW")
web_input.focus()

# Email Label
email_label = tkinter.Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)

# Email Input
email_input = tkinter.Entry(width = 35)
email_input.grid(row = 2, column = 1, columnspan = 2, sticky = "EW")
email_input.insert(0, "agarwalkartik5123@gmail.com")

# Password Label
pass_label = tkinter.Label(text = "Password")
pass_label.grid(row = 3, column = 0)

# Password Input
pass_input = tkinter.ttk.Entry(width = 21, show = "*")
pass_input.grid(row = 3, column = 1, sticky = "EW")

# Generate Password Button
gen_pass_button = tkinter.Button(text = "Generate Password", command = generate_pass, highlightthickness = 0)
gen_pass_button.grid(row = 3, column = 2, sticky = "EW")

# Add Button
add_button = tkinter.Button(text = "Add", width = 36, command = save_pass, highlightthickness = 0)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky = "EW")

# Search Button
search_button = tkinter.Button(text = "Search Password", command = search_pass, highlightthickness = 0)
search_button.grid(row = 1, column = 2, sticky = "EW")

window.mainloop()