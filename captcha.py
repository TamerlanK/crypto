from tkinter import *
import random as r
import string

window = Tk()
window.geometry('300x375')
window.title('Captcha')

captcha = ''


def create():
    global captcha
    canvas.delete('all')
    e.delete(0, END)
    alphabet = string.ascii_letters + string.digits
    symbols = r.sample(alphabet, 5)
    colors = ['red', 'blue', 'green', 'black', 'orange', 'purple', 'brown', 'magenta', 'cyan']
    fonts = ['Verdana', 'Times', 'Arial', 'Papyrus', 'Console', 'Courier', 'Roman', 'Bahnschrift', 'Dubai']
    captcha = "".join(symbols)
    print(captcha)
    for i in range(5):
        canvas.create_text((50 + i * 40) + r.randint(0, 20), 80 + r.randint(0, 20), text=symbols[i],
                           font=r.choice(fonts) + ' 28 bold',
                           fill=r.choice(colors))

    for i in range(5):
        canvas.create_line(r.randrange(10, 280), r.randrange(10, 150), r.randrange(10, 280), r.randrange(10, 150),
                           fill=r.choice(colors), width=r.randint(0, 4))
    radius = r.randrange(5, 20)
    for i in range(5):
        canvas.create_oval((x0 := r.randrange(10, 280)), (y0 := r.randrange(10, 140)), x0 + radius,
                           y0 + radius, fill=r.choice([None, (clr := r.choice(colors))]), outline=clr)
    return captcha


def submit():
    global captcha
    userinput = e.get()
    canvas.delete('all')
    if captcha == userinput:
        print('Verified')
        canvas.create_text(150, 75, text='Verified', fill='green', font='Verdana 20 bold')
    elif captcha != userinput:
        print('Not verified')
        canvas.create_text(150, 75, text='Not Verified', fill='red', font='Verdana 20 bold')
    e.delete(0, END)


canvas = Canvas(width=280, height=150, bg='white')
canvas.place(x=8, y=10)

createButton = Button(text='Create', font='Verdana 14 bold', command=create)
createButton.place(x=110, y=180)

e = Entry(width=18, font='Verdana 14 bold')
e.place(x=20, y=240)

submitButton = Button(text='Submit', font='Verdana 14 bold', command=submit)
submitButton.place(x=105, y=280)

window.mainloop()
