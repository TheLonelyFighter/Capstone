
from numpy import TooHardError
import pygame
from pygame import *
from tkinter import *
from tkinter import messagebox as mb
import json

pygame.init()


class Quiz:

    def __init__(self):

        self.q_no = 0

        self.display_title()
        self.display_question()

        self.opt_selected = IntVar()

        self.opts = self.radio_buttons()

        self.display_options()

        self.buttons()

        self.data_size = len(question)

        self.correct = 0

    def display_result(self):

        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        mb.showinfo(
            "Result", f"{result}\n{correct}\n{wrong}\n\n The Correct answers were: \n 1.Dry Gravel \n 2. Wet Asphalt \n 3. Dry Asphalt \n 4.Snow \n 5. Ice \n 6. Wet Gravel")

    def check_ans(self, q_no):

        if self.opt_selected.get() == answer[q_no]:

            return True

    def next_btn(self):

        if self.check_ans(self.q_no):

            self.correct += 1

        self.q_no += 1
        print(self.q_no)

        if self.q_no == self.data_size:

            self.display_result()

            gui.destroy()
        else:

            self.display_question()
            self.display_options()

    def buttons(self):

        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="cyan", fg="black", font=("ariel", 20, "bold"))

        next_button.place(x=300, y=380)

        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="cyan", fg="black", font=("ariel", 16, " bold"))

        quit_button.place(x=700, y=700)

    def display_options(self):
        val = 0

        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):

        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 18, 'bold'), anchor='w')

        q_no.place(x=70, y=200)

    def display_title(self):

        title1 = Label(gui, text="Guess The Road Condition!  By: Ice Riderzzz",
                      width=50, bg="cyan", fg="black", font=("ariel", 20, "bold"))

        title1.place(x=0, y=2)


        title2 = Label(gui, text=r"https://github.com/TheLonelyFighter/Capstone",
                      width=50, bg="white", fg="black", font=("Courier", 10, "italic"))

        title2.place(x=0, y=600)


    def radio_buttons(self):

        q_list = []
        y_pos = 270
        x_pos = 140
        while len(q_list) < 6:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list)+1, font=("ariel", 14))

            q_list.append(radio_btn)
            radio_btn.place(x=x_pos, y=y_pos)
            if len(q_list) == 1:
                x_pos += 150
            elif len(q_list) == 2:
                x_pos += 150
            elif len(q_list) == 3:
                y_pos +=40
                x_pos -= 300
            elif len(q_list) == 4:
                x_pos += 150
            elif len(q_list) == 5:
                x_pos +=150
        return q_list


gui = Tk()
gui.geometry('800x800')

myframe = Frame(gui)
myframe.pack()

gui.title("Guess The Road Condition!  By: Ice Riderzzz")


with open('json_for_quiz_game.json') as f:
    data = json.load(f)


def unpause():
    pygame.mixer.music.unpause()


def pause():
    pygame.mixer.music.pause()


question = (data['question'])
options = (data['options'])
answer = (data['answer'])


quiz = Quiz()


def play_dry_gravel():
    pygame.mixer.music.load('dry_gravel.wav')
    pygame.mixer.music.play(-1)


def play_wet_asphalt():
    pygame.mixer.music.load('wet_asphalt_new.wav')
    pygame.mixer.music.play(-1)


def play_dry_asphalt():
    pygame.mixer.music.load('dry_asphalt_new.wav')
    pygame.mixer.music.play(-1)

def play_ice():
    pygame.mixer.music.load('ice.wav')
    pygame.mixer.music.play(-1)  #continuous

def play_snow():
    pygame.mixer.music.load('snow.wav')
    pygame.mixer.music.play(-1)

def play_wet_gravel():
    pygame.mixer.music.load('wet_gravel.wav')
    pygame.mixer.music.play(-1)




button1 = Button(gui, text="Sound 3",
                 command=play_dry_asphalt, width=20)
button1.pack(pady=5)
button1.place(x=460, y=100)
button2 = Button(gui, text="Sound 2",
                 command=play_wet_asphalt, width=20)
button2.pack(pady=10)
button2.place(x=300, y=100)
button3 = Button(gui, text="Sound 1",
                 command=play_dry_gravel, width=20)
button3.pack(pady=15)
button3.place(x=140, y=100)

button6 = Button(gui, text="Sound 4",
                 command=play_snow, width=20)
button6.pack(pady=15)
button6.place(x=140, y=130)

button7 = Button(gui, text="Sound 5",
                 command=play_ice, width=20)
button7.pack(pady=15)
button7.place(x=300, y=130)

button7 = Button(gui, text="Sound 6",
                 command=play_wet_gravel, width=20)
button7.pack(pady=15)
button7.place(x=460, y=130)


button4 = Button(gui, text="Continue", command=unpause, width=15)
button4.pack(pady=5)
button4.place(x=240, y=70)

button5 = Button(gui, text="Pause", command=pause, width=15)
button5.pack(pady=5)
button5.place(x=360, y=70)


gui.configure(background='grey')
gui.mainloop()



#TODO 
""" Pickle or sqlite3 for data collection,
change GUI friendlier """


