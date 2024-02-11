import tkinter as tk  
from tkinter import ttk
import random

window = tk.Tk()

lbl_input = tk.Label(
    window,
    width=50,
    height=3,
    text='choice rock, paper, or scissors'
)

lbl_input.grid(row=0,  column=0, columnspan=2)


a = ['rock','paper','scissors']

ai_random = random.choice(a)

def insert_game(btn_text):
    
    current = lbl_input['text']
    
    if btn_text == ai_random :
        lbl_input['text'] = f'equal. your choices is {btn_text} and ai_random choices is {ai_random}' 
    
    elif btn_text == 'rock' and ai_random == 'paper':
        lbl_input['text'] = f'you lose. your choices is {btn_text} and ai_random choices is {ai_random}' 
        
    elif btn_text == 'paper' and ai_random == 'scissors':
        lbl_input['text'] = f'you lose. your choices is {btn_text} and ai_random choices is {ai_random}' 
        
    elif btn_text == 'scissors' and ai_random == 'rock':
        lbl_input['text'] = f'you lose. your choices is {btn_text} and ai_random choices is {ai_random}' 

    elif btn_button == 'C':
        lbl_input['text'] = lbl_input['text']
        
    else:
        lbl_input['text'] = f'you win. your choices is {btn_text} and ai_random choices is {ai_random}' 

btn_button = tk.Button(
    window,
    width=5, 
    text='C',
    command=lambda: insert_game('C')
)

btn_button.grid(row=0, column=3, padx=10,)

calc_data = (
    {
        'text':'rock',
        'command': lambda: insert_game("rock"),
    },
    {
        'text':'paper',
        'command': lambda: insert_game("paper"),
    },
    {
        'text':'scissors',
        'command': lambda: insert_game("scissors"),
    },
)

calc_object = []

for i in calc_data:
    btn = tk.Button(
        window,
        width=8,
        height=3,
        text=i['text'],
        command=i['command'],
    )
    calc_object.append(btn)
    
for i , calc_obj in enumerate(calc_object):
    calc_obj.grid(row=(i // 3) + 1, column= (i % 3) , sticky ='ewns' )



window.mainloop()