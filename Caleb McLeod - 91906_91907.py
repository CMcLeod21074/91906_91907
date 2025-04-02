#Date: 28.03.25
#Author: Caleb McLeod
#Purpose: A maths game that asks the user for the area, perimeter, surface area or volume of shapes
#---------------------------------------------------------------------------------------------------

import random
import tkinter as tk
from PIL import Image, ImageTk



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


maximum_questions = 10
question_num = 0
global question_type
question_type = "default"

def display_shape(shape):
    image = Image.open(shape["image"])
    image = image.resize((300,300))
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root)
    image_label.pack()
    image_label.config(image=image)
    image_label.image = image

def choose_shape():
    global question_num
    global selected_shape
    global question_type
    global display_question_label
    question_num = (question_num + 1)
    selected_shape = random.choice(shapes)
    shapes.remove(selected_shape)
    print(selected_shape["type"])
    if selected_shape["type"] == "area":
        question_type = "area"
        
    if selected_shape["type"] == "perimeter":
        question_type = "perimeter"
    print(question_type)
    
    question_label_text = "What is the "+question_type+" of this shape?"
    display_question_label = tk.Label(root, text=question_label_text)
    display_question_label.pack()
    display_shape(selected_shape)
    

    
def verify_answer():
    global correct_answer
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
        root.after(1000, next_question)
        display_question_label.destroy()

    else:
        print("Incorrect")
        root.after(1000, next_question)
        display_question_label.destroy()
        
        
def next_question():
    image_label.destroy()
    choose_shape()
    
    
root = tk.Tk()






choose_shape()

user_entry = tk.Entry(root, font=("Arial", 14))
user_entry.pack()

submit_button = tk.Button(root, text="Submit", command=verify_answer)
submit_button.pack()
#print(correct_answer)

root.mainloop()
    
