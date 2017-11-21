from Tkinter import *
import tkMessageBox
from random import *

window=Tk()
greeting=Label(window,text="Guess the capitals of the world!")
greeting.pack()
country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna", "Russia": "Moscow",
                            "Australia": "Canberra"}
number = randint(0, 4)
country_name = country_capital_dict.keys()[number]
v = StringVar()
question = Label(window,textvariable=v)
v.set("What is the capital of %s?" %country_name)
s = v.get()
question.pack()
guess_field = Entry(window)
guess_field.pack()

def game():
    country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna", "Russia": "Moscow",
                            "Australia": "Canberra"}
    number = randint(0, 4)
    country_name = country_capital_dict.keys()[number]
    user_guess = str(guess_field.get())
    check_answer(country_name, country_capital_dict, user_guess)


def check_answer(country_name,dict,user_guess):
    capital = dict[country_name]


    if user_guess == capital:
        tkMessageBox.showinfo ("Congratulations! You are right! The capital of %s is indeed %s!" % (country_name, capital))

    else:
        tkMessageBox.showinfo("Sorry, your answer is wrong.")


submit_answer=Button(window, text="Submit your answer", command=check_answer)
submit_answer.pack()

window.mainloop()