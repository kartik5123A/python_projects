import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------- CREATE NEW CARDS ----------------------------------- #

data = pandas.read_csv("data/french_words.csv")
french_words = data["French"].to_list()
english_words = data["English"].to_list()
total_words = len(french_words) - 1
random_number = 0

def pressed_button():
    global random_number, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image = card_front_image)
    random_number = random.randint(0, total_words)
    random_word_french = french_words[random_number]
    canvas.itemconfig(lang_text, text = "French", fill = "black")
    canvas.itemconfig(word_text, text = f"{random_word_french}", fill = "black")
    flip_timer = window.after(3000, flip_the_card)

# ------------------------ FLIP THE CARDS ------------------------------------ #    

def flip_the_card():
    random_word_english = english_words[random_number]
    canvas.itemconfig(card_image, image = card_back_image)
    canvas.itemconfig(lang_text, text = f"English", fill = "white")
    canvas.itemconfig(word_text, text = f"{random_word_english}", fill = "white")  

# ----------------------- DELETE KNOWN CARD ---------------------------------- #     

def delete_card():
    global total_words
    french_words.remove(french_words[random_number])
    english_words.remove(english_words[random_number])
    total_words = len(french_words) - 1

# -------------------------- UI DESIGN --------------------------------------- #
window = tkinter.Tk()
window.title("Flash Card Capstone Project")
window.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)

flip_timer = window.after(3000, flip_the_card)

# Buttons
right_button_image = tkinter.PhotoImage(file = "images/right.png")
right_button = tkinter.Button(image = right_button_image, highlightthickness = 0, command = lambda: [pressed_button(), delete_card()])
right_button.grid(row = 1, column = 1)

left_button_image = tkinter.PhotoImage(file = "images/wrong.png")
left_button = tkinter.Button(image = left_button_image, highlightthickness = 0, command = pressed_button)
left_button.grid(row = 1, column = 0)

# Card Image
canvas = tkinter.Canvas(width = 800, height = 526)
card_front_image = tkinter.PhotoImage(file = "images/card_front.png")
card_back_image = tkinter.PhotoImage(file = "images/card_back.png")
card_image = canvas.create_image(400, 263, image = card_front_image)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
lang_text = canvas.create_text(400, 150, text = "title", font = ("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

pressed_button()

window.mainloop()