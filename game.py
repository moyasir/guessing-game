from tkinter import ttk
import tkinter as tk
import random # number guessing game

window = tk.Tk()
window.title('Guessing game')
win_num=random.randint(1,100)

# labels
username_label = tk.Label(window, text='Enter your name: ')
username_label.grid(row=0, column=0, sticky=tk.W)



user_name,age=input('Enter your name, age : ').split(',')
guess=1
if int(age)>=18:
    print(f'Hi {user_name.title().strip()} you\'re eligible. \nLet\'s play...')
    user_num=int(input(f'Guess any number from one to hundred : '))
    while True:
        if user_num==win_num:
            print(f'Congrat\'s {user_name.title().strip()} you won the game in {guess} times.')
            break
        else:
            if user_num<win_num:
                print(f'Oop\'s you\'ve entered a low number.')
            else:
                print(f'Oop\'s you\'ve entered a High number.')
            user_num=int(input(f'Pleas guess a number again: '))
            guess+=1
            continue
else:
    print(f'Sorry {user_name.title().strip()} your\'re not eligible.')

window.mainloop()
