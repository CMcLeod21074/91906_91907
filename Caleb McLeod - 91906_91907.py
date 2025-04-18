#Date: 28.03.25
#Author: Caleb McLeod
#Purpose: A maths game that asks the user for the area, perimeter, surface area or volume of shapes
#---------------------------------------------------------------------------------------------------

import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
import time


welcome_window = tk.Tk() #Create welcome window
welcome_window.title("Home")

gameplay_window = tk.Toplevel() #Create gameplay window
gameplay_window.title("Gameplay")

game_mode_window = tk.Toplevel() #Create game mode selection window
game_mode_window.title("Gamemode Selection")

score_window = tk.Toplevel() #Create score window
score_window.title("Score")

sign_up_window = tk.Toplevel() #Create sign up window
sign_up_window.title("Sign Up")

login_window = tk.Toplevel() #Create login window
login_window.title("Login")

question_frame = tk.LabelFrame(gameplay_window) 
question_frame.grid(row=2, column=3)

score_frame = tk.LabelFrame(score_window)
score_frame.grid(row=1, column=1)

#Database of shapes
shapes_easy = [
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



    
def display_shape():
    image = Image.open(selected_shape["image"])
    image = image.resize((300,300))
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image

def choose_shape():
    global question_num
    global selected_shape
    global question_type
    global display_question_label
    user_answer_entry.delete(0, tk.END)
    question_num = (question_num + 1)
    selected_shape = random.choice(shapes_easy)
    shapes_easy.remove(selected_shape)
    if selected_shape["type"] == "area":
        question_type = "area"
        
    if selected_shape["type"] == "perimeter":
        question_type = "perimeter"
        
    print("Question Num: ", question_num)
    print("Question Type: ", question_type)
    
    question_label_text = "What is the "+question_type+" of this shape?"
    display_question_label = tk.Label(question_frame, text=question_label_text, font=(20))
    display_question_label.grid(row=0, column=0)
    display_shape()
    
def verify_answer():
    global correct_answer
    global score
    user_answer = user_answer_entry.get()
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

def temp_game_over():
    global score
    score = 8
    game_over()
    welcome_window.withdraw()
    
def game_over():
    gameplay_window.withdraw()
    score_window.deiconify()
    home_button = tk.Button(score_window, text="Home", command=home)
    home_button.grid(row=0, column=3)
    play_again_button = tk.Button(score_window, text="Play again", command=gameplay)
    play_again_button.grid(row=0, column=0)
    final_score = (score,"/10")
    tk.Label(score_frame, text="Username", font=(25)).grid(row=1, column = 0)
    tk.Label(score_frame, text="\t").grid(row=1, column = 1)
    tk.Label(score_frame, text="Score", font=(25)).grid(row=1, column = 2)
    tk.Label(score_frame, text="\t").grid(row=1, column = 3)
    tk.Label(score_frame, text="Time", font=(25)).grid(row=1, column = 4)
    tk.Label(score_frame, text="\t").grid(row=1, column = 5)
    tk.Label(score_frame, text="Difficulty", font=(25)).grid(row=1, column = 6)
    tk.Label(score_frame, text="\t").grid(row=1, column = 7)

    tk.Label(score_frame, text=login_username, font=(25)).grid(row=2, column = 0)
    tk.Label(score_frame, text="\t").grid(row=2, column = 1)
    tk.Label(score_frame, text=final_score, font=(25)).grid(row=2, column = 2)
    tk.Label(score_frame, text="\t").grid(row=2, column = 3)
    tk.Label(score_frame, text="DEFAULT", font=(25)).grid(row=2, column = 4)
    tk.Label(score_frame, text="\t").grid(row=2, column = 5)
    tk.Label(score_frame, text="DEFAULT", font=(25)).grid(row=2, column = 6)
    tk.Label(score_frame, text="\t").grid(row=2, column = 7)
    print("Final score:",score)
    score_window.mainloop()
    
def gameplay_home():
    welcome_window.deiconify()
    gameplay_window.withdraw()

def game_mode_home():
    welcome_window.deiconify()
    game_mode_window.withdraw()

def score_home():
    welcome_window.deiconify()
    score_window.withdraw()

def sign_up_home():
    welcome_window.deiconify()
    sign_up_window.withdraw()

def login_home():
    welcome_window.deiconify()
    login_window.withdraw()    

def quit():
    welcome_window.destroy()

def game_mode_submit():
    global selected_game_model
    selected_game_mode = str(game_mode.get())
    print(selected_game_mode)

def game_mode_selection():
    global game_mode
    game_mode_window.deiconify()
    game_mode = StringVar() 
    game_mode_easy = tk.Radiobutton(game_mode_window, text="Easy", variable=game_mode, value="Easy")
    game_mode_easy.grid(row=1, column=0)
    game_mode_easy.select()
    game_mode_medium = tk.Radiobutton(game_mode_window, text="Medium", variable=game_mode, value="Medium")
    game_mode_medium.grid(row=2, column=0)
    game_mode_medium.deselect()
    game_mode_hard = tk.Radiobutton(game_mode_window, text="Hard", variable=game_mode, value="Hard")
    game_mode_hard.grid(row=3, column=0)
    game_mode_hard.deselect()
    game_mode_button = tk.Button(game_mode_window, text="Select", command=game_mode_submit)
    game_mode_button.grid(row=5, column=3)
    game_mode_window.mainloop()
    

def welcome():
    start_button = tk.Button(welcome_window, text="Start", command=game_mode_selection)
    start_button.grid(row=0, column=0)
    quit_button = tk.Button(welcome_window, text="Quit", command=quit)
    quit_button.grid(row=0, column=4)
    login_button = tk.Button(welcome_window, text="Login", command=login)
    login_button.grid(row=1, column=1)
    sign_up_button = tk.Button(welcome_window, text="Sign up", command=sign_up)
    sign_up_button.grid(row=2, column=1)
    view_highscores_button = tk.Button(welcome_window, text="View Highscores")
    view_highscores_button.grid(row=3, column=1)
    game_over_button = tk.Button(welcome_window, text="Game over",command=temp_game_over)
    game_over_button.grid(row=4, column=1)
    welcome_window.mainloop()
    
def gameplay():
    global score
    global question_num
    global question_type
    ###########
    #login_username = "Default"
    ###########
    score = 0
    question_num = 0
    question_type = "default"
    welcome_window.withdraw()
    login_window.withdraw()
    score_window.withdraw()
    gameplay_window.deiconify() 
    choose_shape()
    username_label = tk.Label(gameplay_window, text=login_username, font=(20))
    username_label.grid(row=1, column = 0)
    level_label = tk.Label(gameplay_window, text=selected_shape["level"].title(), font=(20))
    level_label.grid(row=1, column = 4)

    submit_button = tk.Button(question_frame, text="Submit", command=verify_answer)
    submit_button.grid(row=1, column=2)
    home_button = tk.Button(gameplay_window, text="Home", command=gameplay_home)
    home_button.grid(row=0, column=4)
    gameplay_window.mainloop()

def sign_up():
    welcome_window.withdraw()
    sign_up_window.deiconify()
    home_button = tk.Button(sign_up_window, text="Home", command=sign_up_home)
    home_button.grid(row=0, column=1)
    sign_up_username_label = tk.Label(sign_up_window, text="Username", font=(20))
    sign_up_username_label.grid(row=1, column=0)
    sign_up_password_label = tk.Label(sign_up_window, text="Password", font=(20))
    sign_up_password_label.grid(row=2, column=0)
    append_sign_up_button = tk.Button(sign_up_window, text="Sign up", command=append_sign_up)
    append_sign_up_button.grid(row=3, column=1)
    sign_up_window.mainloop()

def append_sign_up():
    username = str(sign_up_username_entry.get())
    password = "," + str(sign_up_password_entry.get()) + "\n"
    account_info = (username + password)
    login_database = open("login database.txt","a")
    login_database.write(account_info)
    login_database.close()
    sign_up_return = askyesno(title="Sign up successful", message="Sign up successful. Would you like to return to the menu?")

    if sign_up_return == True:
        sign_up_home()
        sign_up_username_entry.delete(0, tk.END)
        sign_up_password_entry.delete(0, tk.END)
        
    elif sign_up_return == False:
        sign_up_username_entry.delete(0, tk.END)
        sign_up_password_entry.delete(0, tk.END)

def login():
    welcome_window.withdraw()
    login_window.deiconify()
    login_username_entry.delete(0, tk.END)
    login_password_entry.delete(0, tk.END)
    home_button = tk.Button(login_window, text="Home", command=login_home)
    home_button.grid(row=0, column=1)
    login_username_label = tk.Label(login_window, text="Username", font=(20))
    login_username_label.grid(row=1, column=0)
    login_password_label = tk.Label(login_window, text="Password", font=(20))
    login_password_label.grid(row=2, column=0)
    append_login_button = tk.Button(login_window, text="Login", command=append_login)
    append_login_button.grid(row=3, column=1)
    login_window.mainloop()

def append_login():
    global login_username
    global login_password
    login_username = str(login_username_entry.get())
    login_password = str(login_password_entry.get())
    print("LOGIN: ",login_username)
    print("PASSWORD: ",login_password)
    login_database = open("login database.txt","r")
    for line in login_database:
        login_list = line.strip("\n").split(",")
        print(login_list[0])
        print(login_list[1])
        
        if login_list[0] == login_username and login_list[1] == login_password:
            print("Match")
            no_login_found = False
            login_database.close()
            gameplay()
            
        else:
            no_login_found = True

    if no_login_found == True:
        no_login_message = askyesno(title="Error", message="No account found with that username or password. Would you like to sign up?")
        if no_login_message == True:
            login_window.withdraw()
            sign_up()
            login_username_entry.delete(0, tk.END)
            login_password_entry.delete(0, tk.END)
            
        elif no_login_message == False:
            login_username_entry.delete(0, tk.END)
            login_password_entry.delete(0, tk.END)
                
    login_database.close()
    
def main():
    global user_answer_entry
    global sign_up_username_entry
    global sign_up_password_entry
    global login_username_entry
    global login_password_entry  
    login_window.withdraw()
    sign_up_window.withdraw()
    gameplay_window.withdraw()
    score_window.withdraw()
    game_mode_window.withdraw()
    user_answer_entry = tk.Entry(question_frame, font=(14))
    user_answer_entry.grid(row=1, column=1)
    sign_up_username_entry = tk.Entry(sign_up_window, font=(14))
    sign_up_username_entry.grid(row=1, column=1)
    sign_up_password_entry = tk.Entry(sign_up_window, show="●", font=(14))
    sign_up_password_entry.grid(row=2, column=1)
    login_username_entry = tk.Entry(login_window, font=(14))
    login_username_entry.grid(row=1, column=1)
    login_password_entry = tk.Entry(login_window, show="●", font=(14))
    login_password_entry.grid(row=2, column=1)
    welcome()

image_label = tk.Label(question_frame)
image_label.grid(row=1, column=0)

main()
