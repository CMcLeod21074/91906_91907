#Date: 28.03.25
#Author: Caleb McLeod
#Purpose: A maths game that asks the user for the area, perimeter, surface area or volume of shapes
#---------------------------------------------------------------------------------------------------

import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
import time

welcome_window = tk.Tk() #Create welcome window
welcome_window.title("Home")
welcome_window.geometry("300x300")
welcome_window.configure(background="#6fdc6f")

gameplay_window = tk.Toplevel() #Create gameplay window
gameplay_window.title("Gameplay")
gameplay_window.geometry("710x500")
gameplay_window.configure(background="#6fdc6f")

game_mode_window = tk.Toplevel() #Create game mode selection window
game_mode_window.title("Gamemode Selection")
game_mode_window.geometry("220x150")
game_mode_window.configure(background="#6fdc6f")

score_window = tk.Toplevel() #Create score window
score_window.title("Score")
score_window.configure(background="#6fdc6f")

highscore_window = tk.Toplevel() #Create highscore window
highscore_window.title("Highscores")
highscore_window.configure(background="#6fdc6f")

sign_up_window = tk.Toplevel() #Create sign up window
sign_up_window.title("Sign Up")
sign_up_window.geometry("300x110")
sign_up_window.configure(background="#6fdc6f")

login_window = tk.Toplevel() #Create login window
login_window.title("Login")
login_window.geometry("300x110")
login_window.configure(background="#6fdc6f")

username_frame = tk.LabelFrame(gameplay_window)
username_frame.grid(row=1, column=0)
username_frame.configure(background="#6fdc6f")

question_frame = tk.LabelFrame(gameplay_window) 
question_frame.grid(row=2, column=1)
question_frame.configure(background="#98e698", border=1)

score_frame = tk.LabelFrame(score_window)
score_frame.grid(row=1, column=1)
score_frame.configure(background="#6fdc6f")

highscore_frame = tk.LabelFrame(highscore_window)
highscore_frame.grid(row=3, column=1)
highscore_frame.configure(background="#6fdc6f")

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

global highscore_count
highscore_count = 0

global line_match
line_match = False

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
    selected_shape = random.choice(shapes_list)
    shapes_list.remove(selected_shape)
    if selected_shape["type"] == "area":
        question_type = "area"
        
    if selected_shape["type"] == "perimeter":
        question_type = "perimeter"
        
    print("Question Num: ", question_num)
    print("Question Type: ", question_type)
    
    question_label_text = "What is the "+question_type+" of this shape?"
    display_question_label = tk.Label(question_frame, text=question_label_text, bg="#98e698", font=("Times New Roman",20))
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
        score = (score+1)
        print("Score: ",score)

        next_question()
        
    else:
        print("Incorrect")
        print("Score: ",score)
        display_question_label.destroy()
        next_question()
        
        
def next_question():
    if question_num <2:
        choose_shape()

    else:
        game_over()

def temp_game_over():
    global login_username
    global score
    global selected_game_mode
    login_username = ("USERNAME")
    score = 8
    selected_game_mode = ("DEFAULT")
    game_over()
    welcome_window.withdraw()
    
def gameplay_home():
    welcome_window.deiconify()
    gameplay_window.withdraw()

def game_mode_home():
    welcome_window.deiconify()
    game_mode_window.withdraw()

def score_home():
    welcome_window.deiconify()
    score_window.withdraw()

def highscore_home():
    welcome_window.deiconify()
    highscore_window.withdraw()

def sign_up_home():
    welcome_window.deiconify()
    sign_up_window.withdraw()

def login_home():
    welcome_window.deiconify()
    login_window.withdraw()    

def quit():
    welcome_window.destroy()

def highscore_append():
    print("HIGHSCORE_APPEND()")
    highscore_database = open("text files/highscore database.txt","r")
    highscore_sort1 = open("text files/highscore sort 1.txt","w")
    highscore_sort2 = open("text files/highscore sort 2.txt","a")
    highscore_sort2.write(line_original)

    for append_line in highscore_database:
        if append_line != line_original:
            final_append = (append_line)
            highscore_sort1.write(final_append)

    highscore_database = open("text files/easy highscore database.txt","w")
    highscore_sort1 = open("text files/easy highscore sort 1.txt","r")
    highscore_database.write(easy_sort1.read())
    highscore_database.close()
    highscore_sort1.close()
    highscore_sort2.close()
    compare_time()

def compare_time():
    print("COMPARING TIME")
    global original_line
    global line_original
    global line_match
    do_append=False
    
    highscore_sort2 = open("text files/highscore sort 2.txt","r")
    highscore_sort2_count = 0
    
    for line in highscore_sort2:
        highscore_sort2_count=highscore_sort2_count+1
    highscore_sort2.close()

    highscore_sort2_count = int(highscore_sort2_count)

    if highscore_count == highscore_sort2_count:
        line_match = True

    highscore_database = open("text files/highscore database.txt","r")
    for line_original in highscore_database:
        original_line = line_original.strip("\n").split(",")
        original = original_line[2]
        original = float(original)
        name_original = original_line[0]
        score_original = original_line[1]
        score_original = int(score_original)
        
        highscore_database = open("text files/highscore database.txt","r")
        for line in highscore_database:
            compare_line = line.strip("\n").split(",")
            compare = compare_line[2]
            compare = float(compare)
            name_compare = compare_line[0]
            score_compare = compare_line[1]
            score_compare = int(score_compare)
      
            if name_original != name_compare and original < compare:
                do_append=True

            if name_original != name_compare and original == compare:

                if score_original > score_compare:
                    do_append=True

                if score_original == score_compare:
                    do_append=True
               
                if score_original < score_compare:
                    do_append=False
                    break

            if name_original != name_compare and original > compare:
                do_append=False
                break

        if do_append == True and line_match == False:
            highscore_append()
            
    highscore_database.close()
    compare_score()

def compare_score():
    print("COMPARING SCORE")
    global selected_game_mode
    compare_score = 10
    for x in range(11):
        highscore_sort2 = open("text files/highscore sort 2.txt","r")
        highscore_sort1 = open("text files/highscore sort 1.txt","a")
        for line in highscore_sort2:
                highscore_list = line.strip("\n").split(",")
                original_score = int(highscore_list[1])
                difficulty = str(highscore_list[3])
                difficulty = difficulty.title()
                if original_score == compare_score:
                    highscore_sort1.write(line)
        compare_score = (compare_score-1)

    highscore_sort2.close()
    highscore_sort1.close()


def update_highscores():
    highscore_mode = str(highscore_mode_combobox.get())

    highscore_sort1 = open("text files/highscore sort 1.txt","r")
    for line in highscore_sort1:
        print(line)
        highscore_list = line.strip("\n").split(",")
        difficulty = str(highscore_list[3])
        difficulty = difficulty.title()
        if difficulty == selected_view_mode:
            print(line)

    highscore_sort1.close()
    
    if highscore_mode == "Easy":
        print("Easy")
        
    elif highscore_mode == "Medium":
        print("Medium")

    elif highscore_mode == "Hard":
        print("Hard")

def game_over():
    global score
    gameplay_window.withdraw()
    score_window.deiconify()     
    final_score = (score, "/10")
    final_time = (00.30)
    final_time = str(final_time)
    score = str(score)
    append_score = str("," + score)
    append_time = str("," + final_time)
    append_game_mode = str("," + selected_game_mode + "\n")
    home_button = tk.Button(score_window, text="Home", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=score_home)
    home_button.grid(row=0, column=3)
    play_again_button = tk.Button(score_window, text="Play again", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=gameplay)
    play_again_button.grid(row=0, column=0)
    
    game_over_username_heading = tk.Label(score_frame, text="Username", bg="#6fdc6f", font=("Times New Roman",14))
    game_over_username_heading.grid(row=1, column = 0)
    game_over_tab1 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab1.grid(row=1, column = 1)
    game_over_score_heading = tk.Label(score_frame, text="Score", bg="#6fdc6f", font=("Times New Roman",14))
    game_over_score_heading.grid(row=1, column = 2)
    game_over_tab2 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab2.grid(row=1, column = 3)
    game_over_time_heading = tk.Label(score_frame, text="Time", bg="#6fdc6f", font=("Times New Roman",14))
    game_over_time_heading.grid(row=1, column = 4)
    game_over_tab3 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab3.grid(row=1, column = 5)
    game_over_difficulty_heading = tk.Label(score_frame, text="Difficulty", bg="#6fdc6f", font=("Times New Roman",14))
    game_over_difficulty_heading.grid(row=1, column = 6)

    game_over_username = tk.Label(score_frame, text=login_username, bg="#6fdc6f", font=("Times New Roman",10))
    game_over_username.grid(row=2, column = 0)
    game_over_tab4 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab4.grid(row=2, column = 1)
    game_over_score = tk.Label(score_frame, text=final_score, bg="#6fdc6f", font=("Times New Roman",10))
    game_over_score.grid(row=2, column = 2)
    game_over_tab5 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab5.grid(row=2, column = 3)
    game_over_time = tk.Label(score_frame, text=final_time, bg="#6fdc6f", font=("Times New Roman",10))
    game_over_time.grid(row=2, column = 4)
    game_over_tab6 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab6.grid(row=2, column = 5)
    game_over_difficulty = tk.Label(score_frame, text=selected_game_mode, bg="#6fdc6f", font=("Times New Roman",10))
    game_over_difficulty.grid(row=2, column = 6)
    print("Final score:",score)
    

    score_data = str(login_username + append_score + append_time + append_game_mode)

    print("APPENDING")
    highscore_database = open("text files/highscore database.txt","a")
    highscore_database.write(score_data)
    print("highscore database")
    highscore_database.close()
    
    compare_time()

    score_window.mainloop()

def view_highscores():
    update_highscores()  
    welcome_window.withdraw()
    highscore_window.deiconify()
    home_button = tk.Button(highscore_window, text="Home", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=highscore_home)
    home_button.grid(row=0, column=3)
    highscore_placing_heading = tk.Label(highscore_frame, text="Placing", bg="#6fdc6f", font=("Times New Roman",14))
    highscore_placing_heading.grid(row=1, column = 0)
    highscore_tab1 = tk.Label(highscore_frame, text="\t", bg="#6fdc6f")
    highscore_tab1.grid(row=1, column = 1)
    highscore_username_heading = tk.Label(highscore_frame, text="Username", bg="#6fdc6f", font=("Times New Roman",14))
    highscore_username_heading.grid(row=1, column = 2)
    highscore_tab2 = tk.Label(highscore_frame, text="\t", bg="#6fdc6f")
    highscore_tab2.grid(row=1, column = 3)
    highscore_score_heading = tk.Label(highscore_frame, text="Score", bg="#6fdc6f", font=("Times New Roman",14))
    highscore_score_heading.grid(row=1, column = 4)
    highscore_tab3 = tk.Label(highscore_frame, text="\t", bg="#6fdc6f")
    highscore_tab3.grid(row=1, column = 5)
    highscore_time_heading = tk.Label(highscore_frame, text="Time", bg="#6fdc6f", font=("Times New Roman",14))
    highscore_time_heading.grid(row=1, column = 6)
    button = tk.Button(highscore_window, text="Select", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=update_highscores)
    button.grid(row=2, column=1)

    global highscore_count
    highscore_database = open("text files/highscore database.txt","r")
    highscore_sort1 = open("text files/highscore sort 1.txt","w")
    highscore_sort2 = open("text files/highscore sort 2.txt","a")

    for line in highscore_database:
        highscore_count=highscore_count+1
    highscore_database.close()

    highscore_count = int(highscore_count)
    
    compare_time()
    update_highscores()

def game_mode_submit():
    global selected_game_mode
    selected_game_mode = str(game_mode.get())
    print(selected_game_mode)
    gameplay()

def game_mode_selection():
    global game_mode
    login_window.withdraw()
    game_mode_window.deiconify()
    game_mode = StringVar() 
    game_mode_easy = tk.Radiobutton(game_mode_window, text="Easy", variable=game_mode, value="Easy", bg="#6fdc6f")
    game_mode_easy.grid(row=1, column=0)
    game_mode_easy.select()
    game_mode_medium = tk.Radiobutton(game_mode_window, text="Medium", variable=game_mode, value="Medium", bg="#6fdc6f")
    game_mode_medium.grid(row=2, column=0)
    game_mode_medium.deselect()
    game_mode_hard = tk.Radiobutton(game_mode_window, text="Hard", variable=game_mode, value="Hard", bg="#6fdc6f")
    game_mode_hard.grid(row=3, column=0)
    game_mode_hard.deselect()
    game_mode_button = tk.Button(game_mode_window, text="Select", bg="#c1f0c1", fg="black", command=game_mode_submit)
    game_mode_button.grid(row=5, column=3)
    game_mode_home_button = tk.Button(game_mode_window, text="Home", bg="#c1f0c1", fg="black", command=game_mode_home)
    game_mode_home_button.grid(row=0, column=3)
    game_mode_label = tk.Label(game_mode_window, text="Select a game mode:   ", bg="#6fdc6f", font=("Times New Roman",14))
    game_mode_label.grid(row=0, column =0) 
    game_mode_window.mainloop()
    

def welcome():
    start_button = tk.Button(welcome_window, text="Start", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=game_mode_selection)
    start_button.grid(row=0, column=0)
    quit_button = tk.Button(welcome_window, text="Quit", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=quit)
    quit_button.grid(row=0, column=2)
    login_button = tk.Button(welcome_window, width = 13, text="Login", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=login)
    login_button.grid(row=2, column=1)
    sign_up_button = tk.Button(welcome_window, width = 13, text="Sign up", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=sign_up)
    sign_up_button.grid(row=3, column=1)
    view_highscores_button = tk.Button(welcome_window, width = 13, text="View Highscores", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=view_highscores)
    view_highscores_button.grid(row=4, column=1)
    game_over_button = tk.Button(welcome_window, width = 13, text="Game over", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=temp_game_over)
    game_over_button.grid(row=5, column=1)
    logo = Image.open("images/characters_background/logo3.png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(welcome_window, bg="#6fdc6f", image=logo)
    logo_label.grid(row=1, column=1)
    welcome_window.mainloop()
    
def gameplay():
    global score
    global question_num
    global question_type
    global shapes_list
    ###########
    #login_username = "Default"
    ###########
    shapes_list = shapes_easy.copy()
    score = 0
    question_num = 0
    question_type = "default"
    welcome_window.withdraw()
    score_window.withdraw()
    game_mode_window.withdraw()
    gameplay_window.deiconify() 
    choose_shape()
    if selected_game_mode == "Medium":
        level_label_size = 10
    else:
        level_label_size = 14
    username_label = tk.Label(username_frame, text=login_username, bg="#6fdc6f", font=("Times New Roman",14))
    username_label.grid(row=1, column = 0)
    level_label = tk.Label(gameplay_window, text=selected_game_mode, bg="#6fdc6f", font=("Times New Roman",level_label_size))
    level_label.grid(row=1, column = 4)
    submit_button = tk.Button(question_frame, text="Submit", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=verify_answer)
    submit_button.grid(row=1, column=2)
    home_button = tk.Button(gameplay_window, text="Home", bg="#c1f0c1", fg="black", font=("Times New Roman",10) , command=gameplay_home)
    home_button.grid(row=0, column=4)
    gameplay_window.mainloop()

def sign_up():
    welcome_window.withdraw()
    sign_up_window.deiconify()
    home_button = tk.Button(sign_up_window, text="Home", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=sign_up_home)
    home_button.grid(row=0, column=1)
    sign_up_username_label = tk.Label(sign_up_window, text="Username", bg="#6fdc6f", font=("Times New Roman",14))
    sign_up_username_label.grid(row=1, column=0)
    sign_up_password_label = tk.Label(sign_up_window, text="Password", bg="#6fdc6f", font=("Times New Roman",14))
    sign_up_password_label.grid(row=2, column=0)
    append_sign_up_button = tk.Button(sign_up_window, text="Sign up", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=append_sign_up)
    append_sign_up_button.grid(row=3, column=1)
    sign_up_window.mainloop()

def append_sign_up():
    username = str(sign_up_username_entry.get())
    password = "," + str(sign_up_password_entry.get()) + "\n"
    account_info = (username + password)
    login_database = open("text files/login database.txt","a")
    login_database.write(account_info)
    login_database.close()
    sign_up_return = askyesno(title="Sign up successful", message="Sign up successful. Would you like to return to the menu?", icon='question')

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
    home_button = tk.Button(login_window, text="Home", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=login_home)
    home_button.grid(row=0, column=1)
    login_username_label = tk.Label(login_window, text="Username", bg="#6fdc6f", font=("Times New Roman",14))
    login_username_label.grid(row=1, column=0)
    login_password_label = tk.Label(login_window, text="Password", bg="#6fdc6f", font=("Times New Roman",14))
    login_password_label.grid(row=2, column=0)
    append_login_button = tk.Button(login_window, text="Login", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=append_login)
    append_login_button.grid(row=3, column=1)
    login_window.mainloop()

def append_login():
    global login_username
    global login_password
    login_username = str(login_username_entry.get())
    login_password = str(login_password_entry.get())
    print("LOGIN: ",login_username)
    print("PASSWORD: ",login_password)
    login_database = open("text files/login database.txt","r")
    for line in login_database:
        login_list = line.strip("\n").split(",")
        print(login_list[0])
        print(login_list[1])
        
        if login_list[0] == login_username and login_list[1] == login_password:
            print("Match")
            no_login_found = False
            print("Closing")
            break
        
            
        else:
            no_login_found = True
            
    if no_login_found == False:        
        game_mode_selection()
        login_database.close()

    if no_login_found == True:
        no_login_message = askyesno(title="No Account Found", message="No account found with that username or password. Would you like to sign up?", icon='warning')
        if no_login_message == True:
            login_window.withdraw()
            login_username_entry.delete(0, tk.END)
            login_password_entry.delete(0, tk.END)
            sign_up()
            
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
    global highscore_mode_combobox
    highscore_sort1 = open("text files/highscore sort 1.txt","w")
    highscore_sort1.write("")
    highscore_sort2 = open("text files/highscore sort 2.txt","w")
    highscore_sort2.write("")
    login_window.withdraw()
    sign_up_window.withdraw()
    gameplay_window.withdraw()
    score_window.withdraw()
    highscore_window.withdraw()
    game_mode_window.withdraw()
    user_answer_entry = tk.Entry(question_frame, font=("Times New Roman",14))
    user_answer_entry.grid(row=1, column=1)
    sign_up_username_entry = tk.Entry(sign_up_window, font=("Times New Roman",14))
    sign_up_username_entry.grid(row=1, column=1)
    sign_up_password_entry = tk.Entry(sign_up_window, show="●", font=("Times New Roman",14))
    sign_up_password_entry.grid(row=2, column=1)
    login_username_entry = tk.Entry(login_window, font=("Times New Roman",14))
    login_username_entry.grid(row=1, column=1)
    login_password_entry = tk.Entry(login_window, show="●", font=("Times New Roman",14))
    login_password_entry.grid(row=2, column=1)
    highscore_mode_combobox = ttk.Combobox(highscore_window, font=("Times New Roman",14), values=["Easy","Medium","Hard"], state="readonly", justify="center")
    highscore_mode_combobox.grid(row=1, column=1)
    highscore_mode_combobox.set("Easy")
    welcome()

image_label = tk.Label(question_frame, bg="#98e698")
image_label.grid(row=1, column=0)
canvas = tk.Canvas(gameplay_window, width=560, height=100, bg="#6fdc6f")
canvas.grid(row=1, column=1)

bg_image = Image.open("images/characters_background/background.png")
bg_image = ImageTk.PhotoImage(bg_image)

cat_image = Image.open("images/characters_background/cat.png")
cat_image = ImageTk.PhotoImage(cat_image)

mouse_image = Image.open("images/characters_background/mouse2.png")
mouse_image = ImageTk.PhotoImage(mouse_image)

bg = canvas.create_image(280, 0, image=bg_image)
cat = canvas.create_image(100, 50, image=cat_image)
mouse = canvas.create_image(200, 50, image=mouse_image)

main()
