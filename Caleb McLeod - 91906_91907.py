#Date: 28.03.25
#Author: Caleb McLeod
#Purpose: A maths game that asks the user for the area, perimeter, surface area or volume of shapes
#---------------------------------------------------------------------------------------------------

import random
import tkinter as tk
from PIL import Image, ImageTk

gameplay_window = tk.Tk() #Create gameplay window
gameplay_window.title("Gameplay Window")

question_frame = tk.LabelFrame(gameplay_window) 
question_frame.grid(row=2, column=0)

welcome_window = tk.Tk() #Create welcome window
welcome_window.title("Welcome Window")

sign_up_window = tk.Tk() #Create sign up window
sign_up_window.title("Sign Up")

#Database of shapes
shapes = [
    {"level": "easy", "type": "area", "shape": "triangle", "base": 6, "height": 4, "image": "images/easy/area/t6x4.png"},
    {"level": "easy", "type": "area", "shape": "triangle", "base": 7, "height": 4, "image": "images/easy/area/t7x4.png"},
    {"level": "easy", "type": "area", "shape": "triangle", "base": 12, "height": 8, "image": "images/easy/area/t12x8.png"},
    {"level": "easy", "type": "area", "shape": "triangle", "base": 12, "height": 15, "image": "images/easy/area/t12x15.png"},
    {"level": "easy", "type": "area", "shape": "triangle", "base": 20, "height": 4, "image": "images/easy/area/t20x4.png"},
    {"level": "easy", "type": "area", "shape": "rectangle", "base": 3, "height": 6, "image": "images/easy/area/sr3x6.png"},
    {"level": "easy", "type": "area", "shape": "rectangle", "base": 7, "height": 7, "image": "images/easy/area/sr7x7.png"},
    {"level": "easy", "type": "area", "shape": "rectangle", "base": 8, "height": 7, "image": "images/easy/area/sr8x7.png"},
    {"level": "easy", "type": "area", "shape": "rectangle", "base": 9, "height": 5, "image": "images/easy/area/sr9x5.png"},
    {"level": "easy", "type": "area", "shape": "rectangle", "base": 12, "height": 8, "image": "images/easy/area/sr12x8.png"},
    {"level": "easy", "type": "perimeter", "shape": "triangle", "side1": 18, "side2": 22, "side3": 20, "image": "images/easy/perimeter/t18x22x20p.png"},
    {"level": "easy", "type": "perimeter", "shape": "triangle", "side1": 15, "side2": 3, "side3": 8, "image": "images/easy/perimeter/t15x3x8p.png"},
    {"level": "easy", "type": "perimeter", "shape": "triangle", "side1": 12, "side2": 15, "side3": 18, "image": "images/easy/perimeter/t12x15x18p.png"},
    {"level": "easy", "type": "perimeter", "shape": "triangle", "side1": 12, "side2": 10, "side3": 4, "image": "images/easy/perimeter/t12x10x4p.png"},
    {"level": "easy", "type": "perimeter", "shape": "triangle", "side1": 8, "side2": 8, "side3": 8, "image": "images/easy/perimeter/t8x8x8p.png"},
    {"level": "easy", "type": "perimeter", "shape": "rectangle", "side1": 5, "side2": 5, "image": "images/easy/perimeter/sr5x5p.png"},
    {"level": "easy", "type": "perimeter", "shape": "rectangle", "side1": 6, "side2": 4, "image": "images/easy/perimeter/sr6x4p.png"},
    {"level": "easy", "type": "perimeter", "shape": "rectangle", "side1": 10, "side2": 10, "image": "images/easy/perimeter/sr10x10p.png"},
    {"level": "easy", "type": "perimeter", "shape": "rectangle", "side1": 20, "side2": 8, "image": "images/easy/perimeter/sr20x8p.png"},
    {"level": "easy", "type": "perimeter", "shape": "rectangle", "side1": 30, "side2": 24, "image": "images/easy/perimeter/sr30x24p.png"},

]

global question_type
global question_num
global score

question_num = 0
score = 0
question_type = "default"

def display_shape(shape):
    image = Image.open(shape["image"])
    image = image.resize((300,300))
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image

def choose_shape():
    global question_num
    global selected_shape
    global question_type
    global display_question_label
    user_entry.delete(0, tk.END)
    question_num = (question_num + 1)
    selected_shape = random.choice(shapes)
    shapes.remove(selected_shape)
    if selected_shape["type"] == "area":
        question_type = "area"
        
    if selected_shape["type"] == "perimeter":
        question_type = "perimeter"
        
    print("Question Num: ", question_num)
    print("Question Type: ", question_type)
    
    question_label_text = "What is the "+question_type+" of this shape?"
    display_question_label = tk.Label(question_frame, text=question_label_text, font=(20))
    display_question_label.grid(row=0, column=0)
    display_shape(selected_shape)
    
def verify_answer():
    global correct_answer
    global score
    user_answer = user_entry.get()
    user_answer = int(user_answer)
    if selected_shape["type"] == "area":
        if selected_shape["shape"] == "triangle":
            correct_answer = (selected_shape["base"] * selected_shape["height"]) //2
        if selected_shape["shape"] == "rectangle":
            correct_answer = (selected_shape["base"] * selected_shape["height"])

    if selected_shape["type"] == "perimeter":
        if selected_shape["shape"] == "triangle":
            correct_answer = (selected_shape["side1"] + selected_shape["side2"] + selected_shape["side3"])
        if selected_shape["shape"] == "rectangle":
            correct_answer = ((selected_shape["side1"] * 2) + (selected_shape["side2"] * 2))

    print(correct_answer)
    
    if user_answer == int(correct_answer):
        print("Correct")
        display_question_label.destroy()
        next_question()
        score = (score+1)
        print("Score: ",score)

    else:
        print("Incorrect")
        print("Score: ",score)
        display_question_label.destroy()
        next_question()
        
        
def next_question():

    if question_num <10:
        choose_shape()

    else:
        game_over()
        
def game_over():
    gameplay_window.withdraw()
    print("Final score:",score)
    
def home():
    welcome_window.deiconify()
    sign_up_window.withdraw()
    gameplay_window.withdraw()

def quit():
    welcome_window.destroy()
    gameplay_window.destroy()

def welcome():
    start_button = tk.Button(welcome_window, text="Start", command=gameplay)
    start_button.grid(row=0, column=0)
    quit_button = tk.Button(welcome_window, text="Quit", command=quit)
    quit_button.grid(row=0, column=4)
    login_button = tk.Button(welcome_window, text="Login")
    login_button.grid(row=1, column=1)
    sign_up_button = tk.Button(welcome_window, text="Sign up", command=sign_up)
    sign_up_button.grid(row=2, column=1)
    view_highscores_button = tk.Button(welcome_window, text="View Highscores")
    view_highscores_button.grid(row=3, column=1)
    welcome_window.mainloop()
    
def gameplay():
    welcome_window.withdraw()
    gameplay_window.deiconify() 
    choose_shape()
    
    level_label = tk.Label(gameplay_window, text=selected_shape["level"].title(), font=(20))
    level_label.grid(row=1, column = 1)

    submit_button = tk.Button(question_frame, text="Submit", command=verify_answer)
    submit_button.grid(row=1, column=2)
    home_button = tk.Button(gameplay_window, text="Home", command=home)
    home_button.grid(row=0, column=1)
    gameplay_window.mainloop()


def sign_up():
    welcome_window.withdraw()
    sign_up_window.deiconify()
    home_button = tk.Button(sign_up_window, text="Home", command=home)
    home_button.grid(row=0, column=1)
    sign_up_window.mainloop()
    
def main():
    global user_entry
    global username_entry
    global password_entry
    sign_up_window.withdraw()
    gameplay_window.withdraw()
    user_entry = tk.Entry(question_frame, font=(14))
    user_entry.grid(row=1, column=1)
    username_entry = tk.Entry(sign_up_window, font=(14))
    username_entry.grid(row=1, column=1)
    password_entry = tk.Entry(sign_up_window, font=(14))
    password_entry.grid(row=2, column=1)
    
    
    welcome()

image_label = tk.Label(question_frame)
image_label.grid(row=1, column=0)

main()
