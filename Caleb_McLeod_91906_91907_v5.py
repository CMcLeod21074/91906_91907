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
import threading
import os
from fpdf import FPDF

#___________Windows________________

welcome_window = tk.Tk() #Create welcome window
welcome_window.title("A Game of Cat and Mouse - Home")
welcome_window.geometry("250x300")
welcome_window.configure(background="#6fdc6f")

gameplay_window = tk.Toplevel() #Create gameplay window
gameplay_window.title("Gameplay")
gameplay_window.geometry("710x520")
gameplay_window.configure(background="#6fdc6f")

game_mode_window = tk.Toplevel() #Create game mode selection window
game_mode_window.title("Gamemode Selection")
game_mode_window.geometry("320x190")
game_mode_window.configure(background="#6fdc6f")

score_window = tk.Toplevel() #Create score window
score_window.title("Score")
score_window.configure(background="#6fdc6f")

highscore_window = tk.Toplevel() #Create highscore window
highscore_window.title("My Highscores")
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
question_frame.configure(background="#98e698", border=1, height = 300, width = 500)

score_frame = tk.LabelFrame(score_window)
score_frame.grid(row=2, column=1)
score_frame.configure(background="#6fdc6f")

highscore_frame = tk.LabelFrame(highscore_window)
highscore_frame.grid(row=3, column=1)
highscore_frame.configure(background="#6fdc6f")

#___________Question Images________________

#Database of shapes
shapes_easy = [
    {"type": "area", "shape": "triangle", "base": 6, "height": 4, "image": "images/easy/area/t6x4.png"},
    {"type": "area", "shape": "triangle", "base": 7, "height": 4, "image": "images/easy/area/t7x4.png"},
    {"type": "area", "shape": "triangle", "base": 12, "height": 8, "image": "images/easy/area/t12x8.png"},
    {"type": "area", "shape": "triangle", "base": 12, "height": 5, "image": "images/easy/area/t12x5.png"},
    {"type": "area", "shape": "triangle", "base": 20, "height": 4, "image": "images/easy/area/t20x4.png"},
    {"type": "area", "shape": "rectangle", "base": 3, "height": 6, "image": "images/easy/area/sr3x6.png"},
    {"type": "area", "shape": "rectangle", "base": 7, "height": 7, "image": "images/easy/area/sr7x7.png"},
    {"type": "area", "shape": "rectangle", "base": 8, "height": 7, "image": "images/easy/area/sr8x7.png"},
    {"type": "area", "shape": "rectangle", "base": 9, "height": 5, "image": "images/easy/area/sr9x5.png"},
    {"type": "area", "shape": "rectangle", "base": 12, "height": 8, "image": "images/easy/area/sr12x8.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 18, "side2": 22, "side3": 20, "image": "images/easy/perimeter/t18x22x20p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 15, "side2": 3, "side3": 8, "image": "images/easy/perimeter/t15x3x8p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 12, "side2": 15, "side3": 18, "image": "images/easy/perimeter/t12x15x18p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 12, "side2": 10, "side3": 4, "image": "images/easy/perimeter/t12x10x4p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 8, "side2": 8, "side3": 8, "image": "images/easy/perimeter/t8x8x8p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 5, "side2": 5, "image": "images/easy/perimeter/sr5x5p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 6, "side2": 4, "image": "images/easy/perimeter/sr6x4p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 10, "side2": 10, "image": "images/easy/perimeter/sr10x10p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 20, "side2": 8, "image": "images/easy/perimeter/sr20x8p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 30, "side2": 24, "image": "images/easy/perimeter/sr30x24p.png"},
]

shapes_medium = [
    {"type": "area", "answer": 10, "image": "images/medium/area/m11.png"},
    {"type": "area", "answer": 15, "image": "images/medium/area/m12.png"},
    {"type": "area", "answer": 68, "image": "images/medium/area/m13.png"},
    {"type": "area", "answer": 45, "image": "images/medium/area/m14.png"},
    {"type": "area", "answer": 28, "image": "images/medium/area/m15.png"},
    {"type": "area", "answer": 44, "image": "images/medium/area/m16.png"},
    {"type": "area", "answer": 30, "image": "images/medium/area/m17.png"},
    {"type": "area", "answer": 40, "image": "images/medium/area/m18.png"},
    {"type": "area", "answer": 30, "image": "images/medium/area/m19.png"},
    {"type": "area", "answer": 36, "image": "images/medium/area/m20.png"},
    {"type": "perimeter", "answer": 27, "image": "images/medium/perimeter/m1.png"},
    {"type": "perimeter", "answer": 44, "image": "images/medium/perimeter/m2.png"},
    {"type": "perimeter", "answer": 22, "image": "images/medium/perimeter/m3.png"},
    {"type": "perimeter", "answer": 30, "image": "images/medium/perimeter/m4.png"},
    {"type": "perimeter", "answer": 30, "image": "images/medium/perimeter/m5.png"},
    {"type": "perimeter", "answer": 34, "image": "images/medium/perimeter/m6.png"},
    {"type": "perimeter", "answer": 44, "image": "images/medium/perimeter/m7.png"},
    {"type": "perimeter", "answer": 31, "image": "images/medium/perimeter/m8.png"},
    {"type": "perimeter", "answer": 55, "image": "images/medium/perimeter/m9.png"},
    {"type": "perimeter", "answer": 34, "image": "images/medium/perimeter/m10.png"},
]

shapes_hard = [{"type": "area", "shape": "triangle", "base": 6, "height": 4, "image": "images/easy/area/t6x4.png"},
    {"type": "area", "shape": "triangle", "base": 7, "height": 4, "image": "images/easy/area/t7x4.png"},
    {"type": "area", "shape": "triangle", "base": 12, "height": 8, "image": "images/easy/area/t12x8.png"},
    {"type": "area", "shape": "triangle", "base": 12, "height": 5, "image": "images/easy/area/t12x5.png"},
    {"type": "area", "shape": "triangle", "base": 20, "height": 4, "image": "images/easy/area/t20x4.png"},
    {"type": "area", "shape": "rectangle", "base": 3, "height": 6, "image": "images/easy/area/sr3x6.png"},
    {"type": "area", "shape": "rectangle", "base": 7, "height": 7, "image": "images/easy/area/sr7x7.png"},
    {"type": "area", "shape": "rectangle", "base": 8, "height": 7, "image": "images/easy/area/sr8x7.png"},
    {"type": "area", "shape": "rectangle", "base": 9, "height": 5, "image": "images/easy/area/sr9x5.png"},
    {"type": "area", "shape": "rectangle", "base": 12, "height": 8, "image": "images/easy/area/sr12x8.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 18, "side2": 22, "side3": 20, "image": "images/easy/perimeter/t18x22x20p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 15, "side2": 3, "side3": 8, "image": "images/easy/perimeter/t15x3x8p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 12, "side2": 15, "side3": 18, "image": "images/easy/perimeter/t12x15x18p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 12, "side2": 10, "side3": 4, "image": "images/easy/perimeter/t12x10x4p.png"},
    {"type": "perimeter", "shape": "triangle", "side1": 8, "side2": 8, "side3": 8, "image": "images/easy/perimeter/t8x8x8p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 5, "side2": 5, "image": "images/easy/perimeter/sr5x5p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 6, "side2": 4, "image": "images/easy/perimeter/sr6x4p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 10, "side2": 10, "image": "images/easy/perimeter/sr10x10p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 20, "side2": 8, "image": "images/easy/perimeter/sr20x8p.png"},
    {"type": "perimeter", "shape": "rectangle", "side1": 30, "side2": 24, "image": "images/easy/perimeter/sr30x24p.png"},
    {"type": "area", "shape": "invalid", "answer": 10, "image": "images/medium/area/m11.png"},
    {"type": "area", "shape": "invalid", "answer": 15, "image": "images/medium/area/m12.png"},
    {"type": "area", "shape": "invalid", "answer": 68, "image": "images/medium/area/m13.png"},
    {"type": "area", "shape": "invalid", "answer": 45, "image": "images/medium/area/m14.png"},
    {"type": "area", "shape": "invalid", "answer": 28, "image": "images/medium/area/m15.png"},
    {"type": "area", "shape": "invalid", "answer": 44, "image": "images/medium/area/m16.png"},
    {"type": "area", "shape": "invalid", "answer": 30, "image": "images/medium/area/m17.png"},
    {"type": "area", "shape": "invalid", "answer": 40, "image": "images/medium/area/m18.png"},
    {"type": "area", "shape": "invalid", "answer": 30, "image": "images/medium/area/m19.png"},
    {"type": "area", "shape": "invalid", "answer": 36, "image": "images/medium/area/m20.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 27, "image": "images/medium/perimeter/m1.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 44, "image": "images/medium/perimeter/m2.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 22, "image": "images/medium/perimeter/m3.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 30, "image": "images/medium/perimeter/m4.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 30, "image": "images/medium/perimeter/m5.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 34, "image": "images/medium/perimeter/m6.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 44, "image": "images/medium/perimeter/m7.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 31, "image": "images/medium/perimeter/m8.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 55, "image": "images/medium/perimeter/m9.png"},
    {"type": "perimeter", "shape": "invalid", "answer": 34, "image": "images/medium/perimeter/m10.png"},
]



highscore_database = open("text files/highscore database.txt","r")

global stop_move
stop_move = False

global catchup

global win

global highscore_difficulty
global highscore_score
global highscore_time

user_x = 200
user_y = 70
user_step = 30

com_x = 80
com_y = 65
com_step = 30

user_x = int(user_x)
catch_up = (user_x - 60)


def display_shape(): # Function that displays the selected shape.
    image = Image.open(selected_shape["image"])
    image = image.resize((300,300))
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image

def choose_shape(): # Function that randomly selects a shape.
    global question_num
    global selected_shape
    global question_type
    global display_question_label
    global selected_game_mode
    
    user_answer_entry.delete(0, tk.END) # Resets user answer input to 0.
    question_num = (question_num + 1)
    selected_shape = random.choice(shapes_list)
    shapes_list.remove(selected_shape)

    if selected_shape["type"] == "area":
        question_type = "area"
        
    if selected_shape["type"] == "perimeter":
        question_type = "perimeter"
    
    question_label_text = "What is the \n"+question_type+" of this shape?" # Question text.
    display_question_label = tk.Label(question_frame, text=question_label_text, bg="#98e698", font=("Times New Roman",20))
    display_question_label.grid(row=0, column=0)
    display_shape()
    
def verify_answer(): # unction that checks if the users input is valid and, if so whether it is the correct answer.
    global correct_answer
    global score
    global wrong_move
    
    user_answer = user_answer_entry.get()
    
    user_answer_check = user_answer.isdigit() # Checks if user input is an integer.
    
    if user_answer_check == False: # If the user has not entered an integer, an error mesage is displayed.
        messagebox.showwarning(title="Invalid Input", message="Please only enter integers into answer input")
        user_answer_entry.delete(0, tk.END)
        
    
    user_answer = int(user_answer)

    if selected_game_mode == "Easy":
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

    if selected_game_mode == "Medium":
        correct_answer = (selected_shape["answer"])
        correct_answer = int(correct_answer)

    if selected_game_mode == "Hard":
        if selected_shape["shape"] == "invalid":
            correct_answer = (selected_shape["answer"])
            correct_answer = int(correct_answer)
        elif selected_shape["type"] == "area":
            if selected_shape["shape"] == "triangle":
                correct_answer = (selected_shape["base"] * selected_shape["height"]) //2
            if selected_shape["shape"] == "rectangle":
                correct_answer = (selected_shape["base"] * selected_shape["height"])

        if selected_shape["type"] == "perimeter":
            if selected_shape["shape"] == "triangle":
                correct_answer = (selected_shape["side1"] + selected_shape["side2"] + selected_shape["side3"])
            if selected_shape["shape"] == "rectangle":
                correct_answer = ((selected_shape["side1"] * 2) + (selected_shape["side2"] * 2))
            
    display_question_label.destroy()
    if user_answer == int(correct_answer):
        score = (score+1)
        move_user()
        
    else:
        stop_move = True
        incorrect_move_com()
    next_question()
        
            
def next_question(): # Function that moves program onto the next question.
    global stop_move
    global display_question_label
    if question_num <20:
        choose_shape()
        stop_move = False

    else:
        stop_move = True
        game_over()
    
    
def gameplay_home(): # Home button from the gameplay window.
    global stop_move
    global user_x
    global com_x
    global display_question_label
    global level_label
    global move_com_id

    gameplay_window.after_cancel(move_com_id) # Cancels the computer characters movement.
    stop_move = True
    
    username_label.destroy()
    level_label.destroy()    
    display_question_label.destroy()
    welcome_window.deiconify()
    gameplay_window.withdraw()

def valid_answer_check():
    user_answer = user_answer_entry.get()
    
    user_answer_check = user_answer.isdigit()
    
    if user_answer_check == False or user_answer == "0": # If the user has not entered an integer or has entered 0, an error mesage is displayed.
        messagebox.showwarning(title="Invalid Input", message="Please only enter integers above zero into answer input")
        user_answer_entry.delete(0, tk.END)

    else:
        verify_answer()

#___________Home Buttons________________

def game_mode_home(): # Home button from the game mode selection window.
    welcome_window.deiconify()
    game_mode_window.withdraw()

def score_home(): # Home button from the gameover/score window.
    global game_over_username
    global game_over_score  
    global game_over_time
    global game_over_difficulty
    welcome_window.deiconify()
    score_window.withdraw()
    username_label.destroy()
    level_label.destroy()    
    display_question_label.destroy()
    game_over_username.destroy()
    game_over_score.destroy()   
    game_over_time.destroy()
    game_over_difficulty.destroy()
    
def highscore_home(): # Home button from the view highscore window.
    global highscore_difficulty
    global highscore_username_easy
    global highscore_score_easy
    global highscore_time_easy
    global highscore_difficulty_medium
    global highscore_username_medium
    global highscore_score_medium
    global highscore_time_medium
    global highscore_difficulty_hard
    global highscore_username_hard
    global highscore_score_hard
    global highscore_time_hard
    
    welcome_window.deiconify()
    highscore_window.withdraw()

    highscore_difficulty_easy.destroy()
    highscore_score_easy.destroy()
    highscore_time_easy.destroy()
    highscore_difficulty_medium.destroy()
    highscore_score_medium.destroy()
    highscore_time_medium.destroy()
    highscore_difficulty_hard.destroy()
    highscore_score_hard.destroy()
    highscore_time_hard.destroy()
    

def sign_up_home(): # Home button from the sign up window.
    welcome_window.deiconify()
    sign_up_window.withdraw()

def login_home(): # Home button from the login window.
    welcome_window.deiconify()
    login_window.withdraw()    

def quit_game(): # Quit button from the welcome window.
    welcome_window.destroy()


#___________Moving Characters________________

def move_user(): # Moves the user character (Mouse) forward when they get the right answer.
    global user_x
    global stop_move
    global catch_up
    global win
    user_x = (user_x + user_step)
    canvas.coords(mouse, user_x, user_y)
    user_x = int(user_x)
    catch_up = (user_x - 60) 
    
    if user_x >=500:
        stop_move = True
        win = True
        game_over()

def incorrect_move_com(): # Moves the computer character (Cat) forward if an incorrect answer is input.
    global com_x
    global user_x
    global catchup
    global win
    global com_step
    global move_com_id
    
    com_x = (com_x + com_step)
    canvas.coords(cat, com_x, com_y)

    catch_up = (user_x - 60)
    
    if com_x >= catch_up:
        gameplay_window.after_cancel(move_com_id)
        win = False
        game_over()

def move_com(): # Moves the computer character (Cat) forward every 8 seconds.
    global com_x
    global user_x
    global catchup
    global win
    global com_step
    global move_com_id
    global stop_move
    global computer_delay
    
    com_x = int(com_x)

    catch_up = (user_x - 60)

    if stop_move == False:
        if com_x >= catch_up:
            win = False
            game_over()
        else:
            com_x = (com_x + com_step)
            canvas.coords(cat, com_x, com_y)
            move_com_id = gameplay_window.after(computer_delay,move_com)
    
#___________End of Game________________

def game_over(): # Function that displas game over screen, indicating whether the user has won or lost.
    global score
    global win
    global home_icon
    global move_com_id
    global login_username
    global final_score
    global final_time
    global selected_game_mode
    global game_over_username
    global game_over_score  
    global game_over_time
    global game_over_difficulty


    gameplay_window.after_cancel(move_com_id)
    stop_move = True
    
    gameplay_window.withdraw()
    score_window.deiconify()

    home_icon = Image.open("images/icons/home.png")
    home_icon = home_icon.resize((25,25))
    home_icon = ImageTk.PhotoImage(home_icon)
    
    final_score = (score)
    
    end_time = time.time()
    end_time = int(end_time)
    final_time = (end_time - user_time)
    final_time = str(final_time)
    display_final_time = str(final_time + " seconds")

    if win == True:
        score_text = ("Congratulations! You Won!")

    elif win == False:
        score_text = ("Sorry, You Lost")

    
    score = str(score)
    append_score = str("," + score)
    append_time = str("," + str(float(final_time)))
    append_game_mode = str("," + selected_game_mode + "\n")
   
    home_button = tk.Button(score_window, image=home_icon, bg="#c1f0c1", command=score_home)
    home_button.grid(row=0, column=3)
    play_again_button = tk.Button(score_window, text="Play again", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=play_again)
    play_again_button.grid(row=0, column=0)
    print_pdf_button = tk.Button(score_window, text="Print score summary", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=print_pdf)
    print_pdf_button.grid(row=4, column=1)

    win_lose_label = tk.Label(score_window, text=score_text, bg="#6fdc6f", font=("Times New Roman",20))
    win_lose_label.grid(row=1, column=1)
    
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
    game_over_time = tk.Label(score_frame, text=display_final_time, bg="#6fdc6f", font=("Times New Roman",10))
    game_over_time.grid(row=2, column = 4)
    game_over_tab6 = tk.Label(score_frame, text="\t", bg="#6fdc6f")
    game_over_tab6.grid(row=2, column = 5)
    game_over_difficulty = tk.Label(score_frame, text=selected_game_mode, bg="#6fdc6f", font=("Times New Roman",10))
    game_over_difficulty.grid(row=2, column = 6)
    
    score_data = str(login_username + append_score + append_time + append_game_mode)

    highscore_database = open("text files/highscore database.txt","a")
    highscore_database.write(score_data)

    highscore_database.close()

    
    highscore_database = open("text files/highscore database.txt","r") # Checks if the user already has an existing highscore, if they do, it will update with new highscore.

    highscore_dict = dict()

    for line in highscore_database:
        highscore_list = line.strip("\n").split(",")
        compare_username = str(highscore_list[0])
        compare_difficulty = str(highscore_list[3])
        compare_score = int(highscore_list[1])
        compare_time = float(highscore_list[2])
        if compare_username in highscore_dict:
            user_dict = highscore_dict[compare_username]
            if compare_difficulty in user_dict:
                user_diff = user_dict[compare_difficulty]
                if compare_score > user_diff[0] or (compare_score == user_diff[0] and compare_time < user_diff[1]):
                    user_diff[0] = compare_score
                    user_diff[1] = compare_time
            else:
                user_dict.update({compare_difficulty:[compare_score,compare_time]})
        else:
            highscore_dict.update({compare_username:{compare_difficulty:[compare_score,compare_time]}})


    highscore_database.close()
    highscore_database = open("text files/highscore database.txt","w")
    for name in highscore_dict:
        for difficulty in highscore_dict[name]:
            append_user_score = highscore_dict[name][difficulty][0]
            append_user_time = highscore_dict[name][difficulty][1]
            data_append = (name + "," + str(append_user_score) + "," + str(append_user_time) + "," + difficulty + "\n")
            highscore_database.write(data_append)

    highscore_database.close()
    
def print_pdf(): # Converts the users score summary to a pdf and prints it.
    global login_username
    global final_score
    global final_time
    global selected_game_mode

    do_print = askyesno(title="Print score summary", message="Do you want to print a copy of your score summary?", icon='question')

    if do_print == True:       
        final_time = str(final_time + " seconds")
        final_score = str(final_score)
    
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 16)
        pdf.image("images/Logo.png")
        pdf.cell(200, 10, txt="A Game of Cat and Mouse", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Times", 'B', 12)
        pdf.cell(45, 10, "Username", 1, align='C')
        pdf.cell(45, 10, "Score", 1, align='C')
        pdf.cell(45, 10, "Time", 1, align='C')
        pdf.cell(45, 10, "Difficulty", 1, align='C')
        pdf.ln()

        pdf.set_font("Times", size=12)
        pdf.cell(45, 10, login_username, 1, align='C')
        pdf.cell(45, 10, final_score, 1, align='C')
        pdf.cell(45, 10, final_time, 1, align='C')
        pdf.cell(45, 10, selected_game_mode, 1, align='C')
        pdf.ln()

        summary_name = str(login_username + " - Score Summary.pdf")
        pdf_location = (summary_name)
        pdf.output(pdf_location)

        try:
            os.startfile(pdf_location)
        
        except Exception as e:
            error_message1 = ("Could not open PDF. Error:", e)
            messagebox.showinfo(title="Error", message = error_message1)

        try:
            os.startfile(pdf_location, "print")
        except Exception as e:
            error_message2 = ("Could not print PDF. Error:", e)
            messagebox.showinfo(title="Error", message = error_message2)

#___________Displaying Highscores________________
    
def display(): # Displays the highscores when the user alters the combobox entry.
    global highscore_mode_combobox
    global highscore_difficulty_easy
    global highscore_username_easy
    global highscore_score_easy
    global highscore_time_easy
    global highscore_difficulty_medium
    global highscore_username_medium
    global highscore_score_medium
    global highscore_time_medium
    global highscore_difficulty_hard
    global highscore_username_hard
    global highscore_score_hard
    global highscore_time_hard
    
    global login_username

    #for x in range(3):
         
       
    try:             
        row = 2
        highscore_database = open("text files/highscore database.txt","r")
    
        for line in highscore_database:          
            highscore_list = line.strip("\n").split(",")
            username_view = str(highscore_list[0])
            display_time = str(highscore_list[2] + " seconds")
            difficulty_view = str(highscore_list[3])
                
            if username_view == login_username:
                if difficulty_view == "Easy":
                    highscore_difficulty_easy = tk.Label(highscore_frame, text=highscore_list[3], bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_difficulty_easy.grid(row=2, column=0)
                    highscore_score_easy = tk.Label(highscore_frame, text=highscore_list[1], bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_score_easy.grid(row=2, column=4)
                    highscore_time_easy = tk.Label(highscore_frame, text=display_time, bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_time_easy.grid(row=2, column=6)

                if difficulty_view == "Medium":
                    highscore_difficulty_medium = tk.Label(highscore_frame, text=highscore_list[3], bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_difficulty_medium.grid(row=3, column=0)
                    highscore_score_medium = tk.Label(highscore_frame, text=highscore_list[1], bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_score_medium.grid(row=3, column=4)
                    highscore_time_medium = tk.Label(highscore_frame, text=display_time, bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_time_medium.grid(row=3, column=6)

                if difficulty_view == "Hard":
                    highscore_difficulty_hard = tk.Label(highscore_frame, text=highscore_list[3], bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_difficulty_hard.grid(row=4, column=0)
                    highscore_score_hard = tk.Label(highscore_frame, text=highscore_list[1], bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_score_hard.grid(row=4, column=4)
                    highscore_time_hard = tk.Label(highscore_frame, text=display_time, bg="#6fdc6f", font=("Times New Roman",10))
                    highscore_time_hard.grid(row=4, column=6)
                
        
        highscore_database.close()

    except NameError:
        welcome_window.deiconify()
        highscore_window.withdraw()
        messagebox.showwarning(title="Error", message = "Please login to view your highscores")
    
def view_highscores(): # Highscore viewing.
    global home_icon
    global highscore_mode_combobox
    global highscore_difficulty
    global highscore_username
    global highscore_score
    global highscore_time
    
    welcome_window.withdraw()
    game_mode_window.withdraw()
    highscore_window.deiconify()

    home_button = tk.Button(highscore_window, image = home_icon, bg="#c1f0c1", fg="black", command=highscore_home)
    home_button.grid(row=0, column=3)

    highscore_title_label = tk.Label(highscore_window, text="My Highscores:", bg="#6fdc6f", font=("Times New Roman",20))
    highscore_title_label.grid(row=1, column=1)
    
    highscore_difficulty_heading = tk.Label(highscore_frame, text="Difficulty", bg="#6fdc6f", font=("Times New Roman",14)) #Highscore headings
    highscore_difficulty_heading.grid(row=1, column = 0)
    highscore_tab1 = tk.Label(highscore_frame, text="\t", bg="#6fdc6f")
    highscore_tab1.grid(row=1, column = 1)
    highscore_score_heading = tk.Label(highscore_frame, text="Score", bg="#6fdc6f", font=("Times New Roman",14))
    highscore_score_heading.grid(row=1, column = 4)
    highscore_tab3 = tk.Label(highscore_frame, text="\t", bg="#6fdc6f")
    highscore_tab3.grid(row=1, column = 5)
    highscore_time_heading = tk.Label(highscore_frame, text="Time", bg="#6fdc6f", font=("Times New Roman",14))
    highscore_time_heading.grid(row=1, column = 6)

    display()

#___________Selecting Game Mode________________
   
def game_mode_submit(): # Confirms the users selected game mode.
    global selected_game_mode
    global computer_delay
    
    selected_game_mode = str(game_mode.get())

    if selected_game_mode == "Easy":
        computer_delay = 8000

    if selected_game_mode == "Medium":
        computer_delay = 12000

    if selected_game_mode == "Hard":
        computer_delay = 15000

    gameplay()

def game_mode_selection(): # Radio button selection for user to select theie desired game mode.
    global game_mode
    global home_icon

    home_icon = Image.open("images/icons/home.png")
    home_icon = home_icon.resize((25,25))
    home_icon = ImageTk.PhotoImage(home_icon)
   
    login_window.withdraw()
    game_mode_window.deiconify()
    game_mode = StringVar()
    
    game_mode_easy = tk.Radiobutton(game_mode_window, text="Easy ── (Triangles, Sqaures and Rectangles)", variable=game_mode, value="Easy", bg="#6fdc6f")
    game_mode_easy.grid(row=1, column=0, sticky="w")
    game_mode_easy.select()
    game_mode_medium = tk.Radiobutton(game_mode_window, text="Medium ── (Irregular Shapes)", variable=game_mode, value="Medium", bg="#6fdc6f")
    game_mode_medium.grid(row=2, column=0, sticky="w")
    game_mode_medium.deselect()
    game_mode_hard = tk.Radiobutton(game_mode_window, text="Hard ── (Miscellaneous)", variable=game_mode, value="Hard", bg="#6fdc6f")
    game_mode_hard.grid(row=3, column=0, sticky="w")
    game_mode_hard.deselect()
    game_mode_button = tk.Button(game_mode_window, text="Select", bg="#c1f0c1", fg="black", command=game_mode_submit)
    game_mode_button.grid(row=5, column=3)
    game_mode_home_button = tk.Button(game_mode_window, image=home_icon, bg="#c1f0c1", command=game_mode_home)
    game_mode_home_button.grid(row=0, column=3)
    game_mode_label = tk.Label(game_mode_window, text="Select a game mode:   ", bg="#6fdc6f", font=("Times New Roman",14))
    game_mode_label.grid(row=0, column =0)

    view_highscore_label = tk.Label(game_mode_window, text="Or view your highscores:", bg="#6fdc6f", font=("Times New Roman",14))
    view_highscore_label.grid(row=6, column =0)
    view_highscores_button1 = tk.Button(game_mode_window, width = 13, text="My Highscores", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=view_highscores)
    view_highscores_button1.grid(row=7, column=0)
    
#___________Main Gameplay________________

def welcome(): 
    quit_button = tk.Button(welcome_window, text="Quit", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=quit_game)
    quit_button.grid(row=0, column=2)
    login_button = tk.Button(welcome_window, width = 13, text="Login", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=login)
    login_button.grid(row=2, column=1)
    sign_up_button = tk.Button(welcome_window, width = 13, text="Sign up", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=sign_up)
    sign_up_button.grid(row=3, column=1)
    view_highscores_button = tk.Button(welcome_window, width = 13, text="My Highscores", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=view_highscores)
    view_highscores_button.grid(row=4, column=1)
    logo = Image.open("images/icons/logo.png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(welcome_window, bg="#6fdc6f", image=logo)
    logo_label.grid(row=1, column=1)
    welcome_window.mainloop()

def gameplay(): # Main game function.
    global home_icon
    global score
    global question_num
    global question_type
    global shapes_list
    global user_time
    global username_label
    global level_label
    global stop_move
    global catch_up
    global com_x
    global user_x
    global move_com_id
    global selected_game_mode
    global login_username
    global computer_delay
    

    catch_up = (user_x - 60)
    
    stop_move = False

    move_com_id = gameplay_window.after(computer_delay,move_com) # Moves computer character every 8 seconds.
    
    home_icon = Image.open("images/icons/home.png") # Home button icon.
    home_icon = home_icon.resize((25,25))
    home_icon = ImageTk.PhotoImage(home_icon)

    if selected_game_mode == "Easy":      
        shapes_list = shapes_easy.copy()

    if selected_game_mode == "Medium":      
        shapes_list = shapes_medium.copy()

    if selected_game_mode == "Hard":      
        shapes_list = shapes_hard.copy()
       
    score = 0
    question_num = 0
    question_type = "default"
    welcome_window.withdraw()
    score_window.withdraw()
    game_mode_window.withdraw()
    gameplay_window.deiconify() 
    choose_shape()

    user_answer_entry.focus_set() # Sets cursor to entry box.

    user_time = time.time()

    user_time = int(user_time)
    
    if selected_game_mode == "Medium":
        level_label_size = 10
    else:
        level_label_size = 14

    user_x = 200 # Starting co-ordinates for mouse character.
    com_x = 100 # Starting co-ordinates for cat character.

    canvas.coords(cat, com_x, com_y) # Starting co-ordinates for cat character.
    canvas.coords(mouse, user_x, user_y) # Starting co-ordinates for mouse character.

    username_label = tk.Label(username_frame, text=login_username, bg="#6fdc6f", font=("Times New Roman",14))
    username_label.grid(row=1, column = 0)
    level_label = tk.Label(gameplay_window, text=selected_game_mode, bg="#6fdc6f", font=("Times New Roman",level_label_size))
    level_label.grid(row=1, column = 4)
    
    username_label.config(text=login_username)
    level_label.config(text=selected_game_mode)
    
    submit_button = tk.Button(question_frame, text="Submit", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=valid_answer_check)
    submit_button.grid(row=1, column=2)
    gameplay_window.bind("<Return>",lambda event: valid_answer_check())    
    home_button = tk.Button(gameplay_window, image=home_icon, bg="#c1f0c1",command=gameplay_home)
    home_button.grid(row=0, column=4)

def play_again(): # Function that resets game when play again button is clicked.
    global user_x
    global com_x
    global display_question_label
    global level_label
    
    username_label.destroy()
    level_label.destroy()    
    display_question_label.destroy()       
    gameplay()

#___________Login/Sign Up________________

def sign_up(): # Function that leads user to sign up window.
    global home_icon
    welcome_window.withdraw()
    sign_up_window.deiconify()

    home_icon = Image.open("images/icons/home.png")
    home_icon = home_icon.resize((25,25))
    home_icon = ImageTk.PhotoImage(home_icon)

    sign_up_username_entry.focus_set()
    
    home_button = tk.Button(sign_up_window, image=home_icon, bg="#c1f0c1", command=sign_up_home)
    home_button.grid(row=0, column=1)
    sign_up_username_label = tk.Label(sign_up_window, text="Username", bg="#6fdc6f", font=("Times New Roman",14))
    sign_up_username_label.grid(row=1, column=0)
    sign_up_password_label = tk.Label(sign_up_window, text="Password", bg="#6fdc6f", font=("Times New Roman",14))
    sign_up_password_label.grid(row=2, column=0)
    append_sign_up_button = tk.Button(sign_up_window, text="Sign up", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=append_sign_up)
    append_sign_up_button.grid(row=3, column=1)
    sign_up_window.bind("<Return>",lambda event: append_sign_up())  

def append_sign_up(): # Function that appends username and password to .txt file.
    username = str(sign_up_username_entry.get())
    password = "," + str(sign_up_password_entry.get()) + "\n"
    account_info = (username + password)
    
    login_database = open("text files/login database.txt","r")

    username_exists = False
    
    for line in login_database:
        account_info_list = line.strip("\n").split(",")
        compare_username = str(account_info_list[0])
        if compare_username == username:
            username_exists = True

    if username_exists == True:
        messagebox.showwarning(title="Username Exists", message="This username already exists. Please choose a different username.")
        sign_up_username_entry.delete(0, tk.END)
        sign_up_password_entry.delete(0, tk.END)

    else:
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

def login(): # Function that leads user to login window.
    global home_icon
    
    welcome_window.withdraw()
    login_window.deiconify()
    login_username_entry.delete(0, tk.END) # Clears username and password entries.
    login_password_entry.delete(0, tk.END)

    login_username_entry.focus_set()

    home_icon = Image.open("images/icons/home.png")
    home_icon = home_icon.resize((25,25))
    home_icon = ImageTk.PhotoImage(home_icon)
    
    home_button = tk.Button(login_window, image = home_icon, bg="#c1f0c1", command=login_home)
    home_button.grid(row=0, column=1)
    login_username_label = tk.Label(login_window, text="Username", bg="#6fdc6f", font=("Times New Roman",14))
    login_username_label.grid(row=1, column=0)
    login_password_label = tk.Label(login_window, text="Password", bg="#6fdc6f", font=("Times New Roman",14))
    login_password_label.grid(row=2, column=0)
    append_login_button = tk.Button(login_window, text="Login", bg="#c1f0c1", fg="black", font=("Times New Roman",10), command=append_login)
    append_login_button.grid(row=3, column=1)
    login_window.bind("<Return>",lambda event: append_login()) 
    

def append_login(): # Function that checks login information (username and password) against .txt file.
    global login_username
    global login_password
    login_username = str(login_username_entry.get())
    login_password = str(login_password_entry.get())

    login_database = open("text files/login database.txt","r")
    for line in login_database:
        login_list = line.strip("\n").split(",")

        if login_list[0] == login_username and login_list[1] == login_password:
            no_login_found = False
            break
        
        else:
            no_login_found = True
            
    if no_login_found == False:  # If an acccount is found with that username the program continues.    
        game_mode_selection()
        login_database.close()

    if no_login_found == True: # If an acccount is not found with that username an error message is displayed.
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

#___________Main Function________________
    
def main(): #Main function
    global user_answer_entry
    global sign_up_username_entry
    global sign_up_password_entry
    global login_username_entry
    global login_password_entry
    global highscore_mode_combobox
    
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
    sign_up_password_entry = tk.Entry(sign_up_window, show="●", font=("Times New Roman",14)) # Hides password - replaces with "...".
    sign_up_password_entry.grid(row=2, column=1)
    
    login_username_entry = tk.Entry(login_window, font=("Times New Roman",14))
    login_username_entry.grid(row=1, column=1)
    
    
    login_password_entry = tk.Entry(login_window, show="●", font=("Times New Roman",14)) # Hides password - replaces with "...".
    login_password_entry.grid(row=2, column=1)  
    
    welcome()

image_label = tk.Label(question_frame, bg="#98e698")
image_label.grid(row=1, column=0)
canvas = tk.Canvas(gameplay_window, width=560, height=100, bg="#6fdc6f") # Canvas for cat and mouse to move on.
canvas.grid(row=1, column=1)

bg_image = Image.open("images/characters_background/background.png") # Background for mouse character and cat character to move on.
bg_image = ImageTk.PhotoImage(bg_image)

cat_image = Image.open("images/characters_background/cat.png") # Computer character - Cat.
cat_image = cat_image.resize((145,145))
cat_image = ImageTk.PhotoImage(cat_image)

mouse_image = Image.open("images/characters_background/mouse.png") # User character - Mouse.
mouse_image = ImageTk.PhotoImage(mouse_image)

bg = canvas.create_image(280, 0, image=bg_image)
mouse = canvas.create_image(user_x, user_y, image=mouse_image)
cat = canvas.create_image(com_x, com_y, image=cat_image)

home_icon = Image.open("images/icons/home.png")
home_icon = home_icon.resize((25,25))
home_icon = ImageTk.PhotoImage(home_icon)

main()
