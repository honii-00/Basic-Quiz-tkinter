# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk
from tkinter import *
import random
from tkinter import ttk


class mQUIZ:

    # constructor
    def __init__(self):
        self.window_m = Tk()
        self.frame = tk.Frame(master=self.window_m, relief=tk.RAISED)
        self.frame.pack()
        # Numbers to use
        self.num1 = random.randint(1, 100)
        self.num2 = random.randint(1, 100)
        # Operation signs
        self.operator = random.choice(['+', '-', '*'])
        # self.operator = random.choice(['+', '-', '*', '/', '%'])
        self.answer = int()
        self.score = 0
        self.mathquiz()

    # Addition
    def add(self):
        return self.num1 + self.num2

    # Subtraction
    def subtract(self):
        return self.num1 - self.num2

    # Multiplication
    def multiply(self):
        return self.num1 * self.num2

    #Division
    def divide(self):
        return self.num1 / self.num2

    #Modulus
    def modulus(self):
        return self.num1 % self.num2

    # def initial_display(self):
    #     first_screen = Toplevel(window_m)
    #     math = tk.Button(master=first_screen, text="MATH", bg="green", fg="white", font=("ariel", 20, "bold"),
    #                      command=self.mathquiz)
    #     math.pack()
    #     english = tk.Button(master=first_screen, text="ENGLISH", bg="green", fg="white", font=("ariel", 20, "bold"))
    #     english.pack()


    def mathquiz(self):

        title = Label(self.frame, text="Math Quiz",
                      font=('Helvetica', 20), bd=10)
        title.pack()

        line = ttk.Separator(self.frame, orient=HORIZONTAL)
        line.pack(fill='x')

        self.numf = tk.Label(master=self.frame, text=f"What is {self.num1} {self.operator} {self.num2}?", bg="green",
                             fg="white",
                             font=("ariel", 20, "bold"))
        self.numf.pack()
        self.entry = tk.Entry(master=self.frame, fg="black", bg="white", width=50)
        self.entry.pack()
        self.check = tk.Button(master=self.frame, text="Check", bg="black", fg="white", command=self.tally_score)
        self.check.pack()



    def tally_score(self):
        if self.operator == '+':
            self.answer = self.add()
        elif self.operator == '-':
            self.answer = self.subtract()
        elif self.operator == '*':
            self.answer = self.multiply()
        # elif self.operator == '/':
        #     self.answer = self.divide()
        #     self.answer = round(self.answer, 2)
        # elif self.operator == '%':
        #     self.answer = self.modulus()

        user_answer = self.entry.get()

        if user_answer == str(self.answer):
            self.score += 1
            result = tk.Label(master=self.frame, text=f"Correct!! {self.score}", font=("ariel", 20, "bold"))
            result.pack(side=tk.BOTTOM)
        else:
            result = tk.Label(master=self.frame, text=f"Incorrect!! {self.score}", font=("ariel", 20, "bold"))
            result.pack(side=tk.BOTTOM)


class eQuiz:
    def __init__(self):
        self.window_e = Tk()
        self.engdata()
        self.ia = 0
        self.eng_gui()
        self.score = 0

    def engdata(self):
        self.qna = {
            "question": [
                "Q1. What Indian city is the capital of two states?",
                "Q2. Which city is the capital of India?",
                "Q3. Smallest State of India?",
                "Q4. Where is Taj Mahal Located?",
                "Q5. What is the capital of Canada?",
                "Q6. What is the national language of India?",
                "Q7. Where is the Great Wall of China located?",
                "Q8. Who wrote 'To Kill a Mockingbird'?"
            ],
            "answer": [
                1,
                2,
                3,
                2,
                2,
                0,
                1,
                3
            ],
            "options": [

                ["Chandigarh",
                 "Kolkata",
                 "Delhi",
                 "Bangalore"
                 ],
                ["Jaipur",
                 "Delhi",
                 "Chennai",
                 "Mumbai"
                 ],
                ["Rajasthan",
                 "Punjab",
                 "Goa",
                 "Bihar"
                 ],
                ["Lucknow",
                 "Agra",
                 "Bhopal",
                 "Delhi"
                 ],
                ["Hindi",
                 "English",
                 "Bengali",
                 "Tamil"
                 ],
                ["Ottawa",
                 "Toronto",
                 "Montreal",
                 "Vancouver"
                 ],
                ["USA",
                 "China",
                 "Japan",
                 "Australia"
                 ],
                ["Harper Lee",
                 "J.K. Rowling",
                 "Agatha Christie",
                 "Ernest Hemingway"
                 ]
            ]
        }


    def eng_gui(self):

        self.fr = Frame(self.window_e, width=200, height=400)
        self.fr.pack()
        title = Label(master=self.fr, text="Start Quiz",
                      font=('Helvetica', 20), bd=10)
        title.pack()

        line = ttk.Separator(master=self.fr, orient=HORIZONTAL)
        line.pack(fill='x')
        self.display_que()

    def display_que(self):

        que = Label(master=self.fr, text=self.qna["question"][self.ia], bg="green",
                    fg="black",
                    font=("ariel", 20, "bold"))
        que.pack()
        self.display_ans_options()

    def display_ans_options(self):
        self.var = IntVar()
        self.var.set(0)
        self.rb = []
        for i, ans_items in enumerate(self.qna["options"][self.ia]):
            # Set the text for each radiobutton
            self.rb = Radiobutton(master=self.fr, text=ans_items,
                                  variable=self.var, value=i, font=("ariel", 12))
            self.rb.pack(anchor='w')
        # check_button = ttk.Button(master=fr, text="Next", command=self.eng_check)
        # check_button.pack()
        next_button = ttk.Button(master=self.fr, text="Next", command=self.eng_check)
        next_button.pack()

    def eng_check(self):

        index = self.var.get()
        opt_selected= self.qna["answer"][index]
        act_ans = self.qna["answer"][self.ia]
        print(self.qna["options"][self.ia][index])
        # checks for if the selected option is correct
        if opt_selected == act_ans:
            # if the option is correct it return true
            self.score += 1
            print("true", self.score)

        self.ia += 1

        if self.ia < 4:

            self.display_que()
        elif self.ia == 4:
            score_lbl = Label(master=self.fr, text="Your score is " + str(self.score), bg="green",
                              fg="black",
                              font=("ariel", 20, "bold"))
            score_lbl.pack()
        else:
            self.window_e.quit()


class pQuiz:
    def __init__(self):
        self.window_p = Tk()
        self.phydata()
        self.ia = 0
        self.phy_gui()
        self.score = 0

    def phydata(self):
        self.qna = {
            "question": [
                "Q1. What is the SI unit of force?",
                "Q2. What is the formula for calculating velocity?",
                "Q3. What is the law of conservation of energy?",
                "Q4. What is the coefficient of friction?",
                "Q5. What is Hooke's law?",
                "Q6. What is the speed of light?",
                "Q7. What is Newton's first law of motion?",
                "Q8. What is Archimedes principle?"
            ],
            "answer": [
                0,
                2,
                3,
                0,
                1,
                3,
                1,
                2
            ],
            "options": [
                [
                    "Newton",
                    "Joule",
                    "Pascal",
                    "Watt"
                    ],
                [
                    "v=d/t",
                    "a=d/t",
                    "v=d/t+1/2at^2",
                    "a=v^2/r"
                    ],
                [
                    "Energy cannot be created or destroyed, only transferred or transformed",
                    "Energy can be created or destroyed",
                    "Energy can only be created",
                    "Energy can only be destroyed"
                    ],
                [
                    "A measure of the force required to move an object over another surface",
                    "The speed at which an object moves over a surface",
                    "The ratio of the force of friction to the normal force",
                    "The amount of energy required to move an object over a surface"
                    ],
                [
                    "The force required to stretch or compress a spring is proportional to the distance of the stretch or compression",
                    "Objects will continue in their current state of motion unless acted upon by an external force",
                    "For every action, there is an equal and opposite reaction",
                    "The force required to move an object is proportional to its mass and acceleration"
                    ],
                [
                    "299,792,458 m/s",
                    "100,000 m/s",
                    "1,000,000 m/s",
                    "500,000,000 m/s"
                    ],
                [
                    "An object at rest will stay at rest, and an object in motion will stay in motion at a constant velocity unless acted upon by an external force",
                    "The acceleration of an object is directly proportional to the force applied to it, and inversely proportional to its mass",
                    "For every action, there is an equal and opposite reaction",
                    "When a force is applied to an object, the object will move in the opposite direction"
                    ],
                [
                    "The upward force exerted on an object in a fluid is equal to the weight of the displaced fluid",
                    "The force required to move an object through a fluid is proportional to the velocity of the object",
                    "The buoyant force acting on an object in a fluid is proportional to the volume of the object",
                    "The amount of fluid displaced by an object is equal to the volume of the object"
                    ]
            ]
            }


    def phy_gui(self):

        self.fr = Frame(self.window_p, width=200, height=400)
        self.fr.pack()
        title = Label(master=self.fr, text="Start Quiz",
                      font=('Helvetica', 20), bd=10)
        title.pack()

        line = ttk.Separator(master=self.fr, orient=HORIZONTAL)
        line.pack(fill='x')
        self.display_que()

    def display_que(self):

        que = Label(master=self.fr, text=self.qna["question"][self.ia], bg="green",
                    fg="black",
                    font=("ariel", 20, "bold"))
        que.pack()
        self.display_ans_options()

    def display_ans_options(self):
        self.var = IntVar()
        self.var.set(0)
        self.rb = []
        for i, ans_items in enumerate(self.qna["options"][self.ia]):
            # Set the text for each radiobutton
            self.rb = Radiobutton(master=self.fr, text=ans_items,
                                  variable=self.var, value=i, font=("ariel", 12))
            self.rb.pack(anchor='w')
        # check_button = ttk.Button(master=fr, text="Next", command=self.eng_check)
        # check_button.pack()
        next_button = ttk.Button(master=self.fr, text="Next", command=self.phy_check)
        next_button.pack()

    def phy_check(self):

        index = self.var.get()
        opt_selected= self.qna["answer"][index]
        act_ans = self.qna["answer"][self.ia]
        print(self.qna["options"][self.ia][index])
        # checks for if the selected option is correct
        if opt_selected == act_ans:
            # if the option is correct it return true
            self.score += 1
            print("true", self.score)

        self.ia += 1

        if self.ia < 4:

            self.display_que()
        elif self.ia == 4:
            score_lbl = Label(master=self.fr, text="Your score is " + str(self.score), bg="green",
                              fg="black",
                              font=("ariel", 20, "bold"))
            score_lbl.pack()
        else:
            self.window_p.quit()




class main_gui:
    def __init__(self):
        self.sub_window = Tk()
        self.first_init()

    def math_class(self):

        mquiz = mQUIZ()
        mquiz.window_m.mainloop()

    def eng_class(self):
        eQUIZ = eQuiz()
        eQUIZ.window_e.mainloop()

    def phy_class(self):
        pQUIZ = pQuiz()
        pQUIZ.window_p.mainloop()

    def first_init(self):

        first_screen = Frame(master=self.sub_window, relief=tk.RAISED)
        first_screen.pack()
        math = tk.Button(master=first_screen, text="MATH", bg="green", fg="white", font=("ariel", 20, "bold"),
                         command=self.math_class)
        math.pack()
        english = tk.Button(master=first_screen, text="ENGLISH", bg="green", fg="white", font=("ariel", 20, "bold"), command=self.eng_class)
        english.pack()
        physics = tk.Button(master=first_screen, text="PHYSICS", bg="green", fg="white", font=("ariel", 20, "bold"),
                            command=self.phy_class)
        physics.pack()


MAIN_GUI = main_gui()
MAIN_GUI.sub_window.mainloop()

