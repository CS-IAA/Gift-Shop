'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Fun Game program
Version 1.0
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo #popup
from PIL import Image, ImageTk # so you can use Pillow

root = Tk() #creates GUI
root.title("International Gift Shop") #title

def about():
    messagebox.showinfo("Version", "International Gift Shop\nVersion 1.0")

def hel():
    showinfo("Help", "The customer, who is located in the United States, is buying and sending a gift of their choice to someone of another country. They must enter their's and the receiver's  names and residential information along with the shipping type. They must enter a message to the receiver and select a gift. The zip codes that they enter must be 5 digits and cannot be negative numbers. They also cannot include decimals.\n\nCOMING SOON: As of right now we ship to 50 different countries and have eleven gifts to choose from. We plan on adding more countries that our customers can ship to as well as more gifts that they can choose from.")

def country_ship(*args): #changes shipping price for each country
    if country.get() == "Brazil":
        ships.delete(0,) #delets any existing value in the 0th index
        ships.insert(0, "One week - $15") #adds price for first week in the 0th index
        ships.delete(1,)
        ships.insert(1, "Two weeks - $10")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $5")
    elif country.get() == "Argentina":
        ships.delete(0,)
        ships.insert(0, "One week - $20")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $15")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $10")
    elif country.get() == "Australia":
        ships.delete(0,)
        ships.insert(0, "One week - $45")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $40")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $35")
    elif country.get() == "Austria":
        ships.delete(0,)
        ships.insert(0, "One week - $23")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $18")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $13")
    elif country.get() == "Bangladesh":
        ships.delete(0,)
        ships.insert(0, "One week - $40")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $35")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $30")
    elif country.get() == "Bolivia":
        ships.delete(0,)
        ships.insert(0, "One week - $14")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $9")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $4")
    elif country.get() == "Canada":
        ships.delete(0,)
        ships.insert(0, "One week - $10")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $5")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $3")
    elif country.get() == "Chile":
        ships.delete(0,)
        ships.insert(0, "One week - $20")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $15")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $10")
    elif country.get() == "China":
        ships.delete(0,)
        ships.insert(0, "One week - $42")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $37")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $32")
    elif country.get() == "Colombia":
        ships.delete(0,)
        ships.insert(0, "One week - $12")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $8")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $3")
    elif country.get() == "Costa Rica":
        ships.delete(0,)
        ships.insert(0, "One week - $10")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $6")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $3")
    elif country.get() == "Denmark":
        ships.delete(0,)
        ships.insert(0, "One week - $21")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $16")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $11")
    elif country.get() == "Ecuador":
        ships.delete(0, )
        ships.insert(0, "One week - $12")
        ships.delete(1, )
        ships.insert(1, "Two weeks - $8")
        ships.delete(2, )
        ships.insert(2, "Three weeks - $3")
    elif country.get() == "Egypt":
        ships.delete(0, )
        ships.insert(0, "One week - $22")
        ships.delete(1, )
        ships.insert(1, "Two weeks - $17")
        ships.delete(2, )
        ships.insert(2, "Three weeks - $12")
    elif country.get() == "France":
        ships.delete(0,)
        ships.insert(0, "One week - $20")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $15")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $10")
    elif country.get() == "Germany":
        ships.delete(0,)
        ships.insert(0, "One week - $21")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $16")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $11")
    elif country.get() == "Greece":
        ships.delete(0,)
        ships.insert(0, "One week - $23")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $18")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $13")
    elif country.get() == "Hungary":
        ships.delete(0,)
        ships.insert(0, "One week - $23")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $18")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $13")
    elif country.get() == "Iceland":
        ships.delete(0,)
        ships.insert(0, "One week - $16")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $11")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $6")
    elif country.get() == "India":
        ships.delete(0,)
        ships.insert(0, "One week - $40")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $35")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $30")
    elif country.get() == "Indonesia":
        ships.delete(0,)
        ships.insert(0, "One week - $44")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $39")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $29")
    elif country.get() == "Ireland":
        ships.delete(0,)
        ships.insert(0, "One week - $17")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $12")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $7")
    elif country.get() == "Italy":
        ships.delete(0,)
        ships.insert(0, "One week - $23")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $18")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $13")
    elif country.get() == "Japan":
        ships.delete(0,)
        ships.insert(0, "One week - $43")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $38")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $33")
    elif country.get() == "Kuwait":
        ships.delete(0,)
        ships.insert(0, "One week - $24")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $19")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $14")
    elif country.get() == "Latvia":
        ships.delete(0,)
        ships.insert(0, "One week - $22")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $16")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $10")
    elif country.get() == "Malaysia":
        ships.delete(0,)
        ships.insert(0, "One week - $44")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $39")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $33")
    elif country.get() == "Mexico":
        ships.delete(0,)
        ships.insert(0, "One week - $7")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $5")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $3")
    elif country.get() == "Netherlands":
        ships.delete(0,)
        ships.insert(0, "One week - $20")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $15")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $10")
    elif country.get() == "Nigeria":
        ships.delete(0,)
        ships.insert(0, "One week - $17")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $12")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $7")
    elif country.get() == "Norway":
        ships.delete(0,)
        ships.insert(0, "One week - $18")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $13")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $8")
    elif country.get() == "Pakistan":
        ships.delete(0,)
        ships.insert(0, "One week - $37")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $32")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $17")
    elif country.get() == "Panama":
        ships.delete(0,)
        ships.insert(0, "One week - $11")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $6")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $3")
    elif country.get() == "Peru":
        ships.delete(0,)
        ships.insert(0, "One week - $19")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $14")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $9")
    elif country.get() == "Philippines":
        ships.delete(0,)
        ships.insert(0, "One week - $45")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $40")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $35")
    elif country.get() == "Poland":
        ships.delete(0,)
        ships.insert(0, "One week - $21")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $16")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $11")
    elif country.get() == "Portugal":
        ships.delete(0,)
        ships.insert(0, "One week - $15")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $10")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $5")
    elif country.get() == "Qatar":
        ships.delete(0,)
        ships.insert(0, "One week - $24")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $19")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $14")
    elif country.get() == "Russia":
        ships.delete(0,)
        ships.insert(0, "One week - $50")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $45")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $40")
    elif country.get() == "Saudi Arabia":
        ships.delete(0,)
        ships.insert(0, "One week - $26")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $21")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $16")
    elif country.get() == "Singapore":
        ships.delete(0,)
        ships.insert(0, "One week - $44")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $39")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $34")
    elif country.get() == "South Korea":
        ships.delete(0,)
        ships.insert(0, "One week - $42")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $37")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $32")
    elif country.get() == "Spain":
        ships.delete(0,)
        ships.insert(0, "One week - $15")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $10")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $5")
    elif country.get() == "Sri Lanka":
        ships.delete(0,)
        ships.insert(0, "One week - $39")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $34")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $29")
    elif country.get() == "Sweden":
        ships.delete(0,)
        ships.insert(0, "One week - $19")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $14")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $9")
    elif country.get() == "Switzerland":
        ships.delete(0,)
        ships.insert(0, "One week - $24")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $19")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $14")
    elif country.get() == "Turkey":
        ships.delete(0,)
        ships.insert(0, "One week - $28")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $23")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $18")
    elif country.get() == "United Arab Emirates":
        ships.delete(0,)
        ships.insert(0, "One week - $27")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $12")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $17")
    elif country.get() == "United Kingdom":
        ships.delete(0,)
        ships.insert(0, "One week - $17")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $12")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $7")
    elif country.get() == "Venezuela":
        ships.delete(0,)
        ships.insert(0, "One week - $13")
        ships.delete(1,)
        ships.insert(1, "Two weeks - $8")
        ships.delete(2,)
        ships.insert(2, "Three weeks - $3")

def gift_pic(*args): #creats entire new tkinter window and adds a picture and a few words related to the gift upon it being clicked.
    try:
        if gift.curselection()[0] == 1:
            window = Toplevel() #new tkinter window opened
            window.title("Gift") #title of new tiknter
            mainframe2 = ttk.Frame(window, padding="5 10") #frame
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="Because this monkey is just so cute and we know can't help ourselves!") #message
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('monkey.jpg') #opens gift picture
            canvas.image = ImageTk.PhotoImage(im) #adds that to canvas
            canvas.create_image(0, 0, image=canvas.image, anchor="nw") #grids the image

        elif gift.curselection()[0] == 10:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="An essential for gamers. Know a gamer? Make their day shine!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('switch.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")

        elif gift.curselection()[0] == 6:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="With a single touch from you, yours and your loved one's lamp will light up!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('lamp.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")

        elif gift.curselection()[0] == 3:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="A metal heart that displays ones heart filled with light toward another!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('heart.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")

        elif gift.curselection()[0] == 0:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="Because who wouldn't want a 1,000 Emoji stickers?")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('sticker.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")
        elif gift.curselection()[0] == 4:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="No more pointless mornings with this R2-D2 coffee press!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('coffee.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")
        elif gift.curselection()[0] == 8:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=450, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="Now you can sleep under the stars all year long!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('8K.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")
        elif gift.curselection()[0] == 5:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="At least you won't lost your dice anymore...right?")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('dice.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")
        elif gift.curselection()[0] == 7:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N,W,E,S))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="It levitates. What more needs to be said?")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('speak.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")
        elif gift.curselection()[0] == 2:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="Just add milk and chocolate syrup and then press the button! It's messless!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('mug.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")
        elif gift.curselection()[0] == 9:
            window = Toplevel()
            window.title("Gift")
            mainframe2 = ttk.Frame(window, padding="5 10")
            mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
            mainframe2.columnconfigure(0, weight=1)
            mainframe2.rowconfigure(0, weight=1)

            drag = ttk.Frame(window, padding="5 10")  # creating another Frame to put the image in
            drag.grid(column=2, row=2, sticky=(N, E))
            drag.columnconfigure(0, weight=1)
            drag.rowconfigure(0, weight=1)
            canvas = Canvas(drag, width=400, height=300)
            canvas.pack()

            sk = ttk.Label(window, text="With this shark by your side, you'll never be lonely!")
            sk.grid(column=1, row=3, columnspan=2, sticky=(N, W))

            im = Image.open('stapler.jpg')
            canvas.image = ImageTk.PhotoImage(im)
            canvas.create_image(0, 0, image=canvas.image, anchor="nw")

    except:
        pass

def check():
    # checks to make sure that the user has done everything before checking to see if it was done correctly
    if len(ships.curselection()):
        if len(Fname.get()):
            if len(Lname.get()):
                if len(address.get()):
                    if len(city.get()):
                        if len(States.get()):
                            if len(zipcode.get()):
                                if len(rmessage.get("1.0", "end-1c")) > 0:
                                    if len(gift.curselection()):
                                        if len(rFname.get()):
                                            if len(rLname.get()):
                                                if len(rcountry.get()):
                                                    if len(raddress.get()):
                                                        if len(rcity.get()):
                                                            if len(rzipcode.get()):
                                                                confirm()
                                                            else:
                                                                showinfo("Error", "Please enter in all of the information!")
                                                        else:
                                                            showinfo("Error", "Please enter in all of the information!")
                                                    else:
                                                        showinfo("Error", "Please enter in all of the information!")
                                                else:
                                                    showinfo("Error", "Please enter in all of the information!")
                                            else:
                                                showinfo("Error", "Please enter in all of the information!")
                                        else:
                                            showinfo("Error", "Please enter in all of the information!")
                                    else:
                                        showinfo("Error", "Please enter in all of the information!")
                                else:
                                    showinfo("Error", "Please enter in all of the information!")
                            else:
                                showinfo("Error", "Please enter in all of the information!")
                        else:
                            showinfo("Error", "Please enter in all of the information!")
                    else:
                        showinfo("Error", "Please enter in all of the information!")
                else:
                    showinfo("Error", "Please enter in all of the information!")
            else:
                showinfo("Error", "Please enter in all of the information!")
        else:
            showinfo("Error", "Please enter in all of the information!")
    else:
        showinfo("Error", "Please enter in all of the information!")  # popup if they don't enter something

def confirm():
    try:
        if int(zipcode.get()) >= 0 and len(zipcode.get()) == 5: #makes sure zip code is positive and a integer and is 5 digits
            if int(rzipcode.get()) >= 0 and len(rzipcode.get()) == 5:
                calculate()
            else:
                showinfo("Error", "Please make sure you enter only positive numbers in numerical integer form with 5 digits for the receiver's zip code!")
        else:
            showinfo("Error", "Please make sure you enter only positive numbers in numerical integer form with 5 digits for your zip code!")
    except ValueError:
        showinfo("Error", "Please make sure you enter only positive numbers in numerical form for both zip codes! Also, make sure that the zipcodes do not have a decimal.")

def calculate():
    box1 = ships.get(ANCHOR) #gets what they selected for price
    ship_cost = int(box1.split("$", 1)[1]) #to get just the price and not 'first week - $'
    box2 = gift.get(ANCHOR)
    price = int(box2.split("$", 1)[1]) #price of the gift
    tax_tax = (float(price) * 0.0825) #how much tax there is on the gift
    tax_tax = round(tax_tax, 2) #rounds tax to the second digit
    total_pricez = (float(price) + tax_tax) #adds how much tax there is on the gift with the price
    total_price = total_pricez + ship_cost #adds in shipping fee-tax w/ shipping
    total_price = round(total_price, 2) #rounds the total price to the second digit
    total.set("Total: $"+ str(total_price)) #str because cant add a string and a integer together
    tax.set("Tax: $"+str(tax_tax))
    showinfo("Success", "Congratulations, your gift was successfully sent!")

def clear():
    ships.select_clear(0, END)  # clears the selection
    gift.select_clear(0, END)  # clears the selection
    rmessage.delete("1.0", END)  # deletes message to receiver from textbox
    rmessage.insert(END, "")  # adds blank space into text widget
    Fname.set('')  # clears the first name
    Lname.set('')  # clears the left name
    address.set('')  # clears the street address
    city.set('')  # clears the city
    States.set('')  # clears the state
    zipcode.set('')  # clears the zip code
    rFname.set('')  # clears the receiver's first name
    rLname.set('')  # clears the receiver's last name
    rcountry.set('')  # clears the receivers country
    raddress.set('')  # clears the receivers address
    rcity.set('')  # clears the receivers city
    rzipcode.set('')  # clears the receivers zip code
    tax.set("Tax: $")  # clears the tax
    total.set("Total: $")  # clears the total price
    ships.delete(0, ) #to get rid of shipping prices from country
    ships.insert(0, "One week") #inserts in original value
    ships.delete(1, )
    ships.insert(1, "Two weeks")
    ships.delete(2, )
    ships.insert(2, "Three weeks")

root.option_add('*tearOff', FALSE) #gets rid of dashed line
menu = Menu(root) #creates menu
root.config(menu=menu) #adds ability to create options

subMenu = Menu(menu) #creats submenu
menu.add_cascade(label="File", menu=subMenu) # creates a menu option
subMenu.add_command(label="Exit", command=root.destroy) #file option

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu) #creates another menu option
helpMenu.add_command(label="Help", command=hel) #file option
helpMenu.add_command(label="About", command=about) #file option

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

years = ['2017', '2018', '2019', '2020']
ship_day = ['One week', 'Two weeks', 'Five weeks']
gifts = ['1,000 Emoji Sticker Set - $20', 'Fingerling Toy Monkey - $20', 'Chocolate Milk Mixing Mug - $25', \
         'Metal Heart with LED Lights - $55', 'Star Wars R2-D2 Coffee Press - $55', 'Giant Wooden Yard Dice - $70', \
         'Long Distance Touch Lamp - $100', 'Levitating Bluetooth Speaker - $135', '8,000 Stars Home Planetarium - $175', \
         'Shark Bite Stapler - $195', 'Nintendo Switch - $400']

Fname = StringVar()
Lname = StringVar()
States = StringVar()
city = StringVar()
address = StringVar()
zipcode = StringVar()
giftItem = StringVar(value=gifts)
rFname = StringVar()
rLname = StringVar()
rcountry = StringVar()
rcity = StringVar()
raddress = StringVar()
rzipcode = StringVar()
shipping = StringVar(value=ship_day)
tax = StringVar()
total = StringVar()

ttk.Entry(mainframe, textvariable=Fname, width = 22).grid(column = 2, row = 2, sticky = W)
ttk.Entry(mainframe, textvariable=Lname, width = 22).grid(column = 2, row = 3, sticky = W)
ttk.Entry(mainframe, textvariable=address, width = 22).grid(column = 2, row = 6, sticky = W)
ttk.Entry(mainframe, textvariable=city, width = 22).grid(column = 2, row = 5, sticky = W)
ttk.Entry(mainframe, textvariable=zipcode, width = 22).grid(column = 2, row = 7, sticky = W)
ttk.Entry(mainframe, textvariable=rFname, width = 22).grid(column = 4, row = 2, sticky = W)
ttk.Entry(mainframe, textvariable=rLname, width = 22).grid(column = 4, row = 3, sticky = W)
ttk.Entry(mainframe, textvariable=raddress, width = 22).grid(column = 4, row = 6, sticky = W)
ttk.Entry(mainframe, textvariable=rcity, width = 22).grid(column = 4, row = 5, sticky = W)
ttk.Entry(mainframe, textvariable=rzipcode, width = 22).grid(column = 4, row = 7, sticky = W)

country = ttk.Combobox(mainframe, textvariable=rcountry, width=19, state = 'readonly')
country.grid(column = 4, row = 4, sticky = W)
country.bind("<<ComboboxSelected>>", country_ship)

country['values'] = ('Argentina', 'Australia', 'Austria', 'Bangladesh', 'Bolivia', 'Brazil', 'Canada', 'Chile', \
         'China', 'Colombia', 'Costa Rica', 'Denmark', 'Ecuador', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', \
         'Iceland', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kuwait', 'Latvia', \
         'Malaysia', 'Mexico', 'Netherlands', 'Nigeria', 'Norway', 'Pakistan', 'Panama', 'Peru', \
         'Philippines','Poland', 'Portugal', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', \
         'Spain', 'Sri Lanka', 'Sweden', 'Switzerland', 'Turkey', 'United Arab Emirates', 'United Kingdom', 'Venezuela')

state = ttk.Combobox(mainframe, textvariable=States, width=1, state = 'readonly')
state.grid(column=2, row=4, sticky=(W,E))
state['values'] = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', \
         'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', \
         'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', \
         'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', \
         'Oklahoma','Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', \
         'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
#states of the US

rmessage = Text(mainframe,wrap=WORD, width = 17,height=7)
#text widget that gives message to receiver. wrap makes sure that a word doesn't strech onto more than one line
rmessage.grid(column = 2, row = 8, sticky =W) #graph on diff line else "no index" error
rmessage.insert(END, "") #adds text into text widget

#exportselection=0 makes so if more than 1 listbox, you can select from all of them
ships = Listbox(mainframe, height=3, listvariable=shipping, exportselection=0) #shipping days
ships.grid(column = 6, row = 2, sticky = (N,W,E,S))
#creates listbox which has shipping days. listvariable acceses the shipping days and adds to listbox

gift = Listbox(mainframe, height=7,width=37,listvariable=giftItem, exportselection=0) #shipping days
gift.grid(column=4, row = 8, columnspan=2,sticky=(E,W))
gift.bind('<<ListboxSelect>>',gift_pic)
s = ttk.Scrollbar(mainframe, orient=VERTICAL, command=gift.yview) #creating a scroll bar for the listbox(box1)
s.grid(column=4, row=8, columnspan=2,sticky=(N,S,E))
gift['yscrollcommand'] = s.set #makes the scroll moveable

ttk.Button(mainframe, text="Send", width = 8, command=check).grid(column=6, row=5, sticky = (N,W))
ttk.Button(mainframe, text="Clear", width = 8, command=clear).grid(column=6, row=5, sticky = (N,E))

ttk.Label(mainframe, text = "      Your information").grid(column = 2, row = 1, sticky =W)
ttk.Label(mainframe, text = "First Name").grid(column = 1, row = 2, sticky =W)
ttk.Label(mainframe, text = "Last Name").grid(column = 1, row = 3, sticky =W)
ttk.Label(mainframe, text = "State").grid(column = 1, row = 4, sticky =W)
ttk.Label(mainframe, text = "City").grid(column = 1, row = 5, sticky =W)
ttk.Label(mainframe, text = "Street Address").grid(column = 1, row = 6, sticky =W)
ttk.Label(mainframe, text = "Zip Code").grid(column = 1, row = 7, sticky =W)
ttk.Label(mainframe, text = "Message").grid(column = 1, row = 8, sticky =W)
ttk.Label(mainframe, text = "Gift").grid(column = 3, row = 8, sticky =W)
ttk.Label(mainframe, text = "  Receiver's information").grid(column = 4, row = 1, sticky =W)
ttk.Label(mainframe, text = "First Name").grid(column = 3, row = 2, sticky =W)
ttk.Label(mainframe, text = "Last Name").grid(column = 3, row = 3, sticky =W)
ttk.Label(mainframe, text = "Country").grid(column = 3, row = 4, sticky =W)
ttk.Label(mainframe, text = "City").grid(column = 3, row = 5, sticky =W)
ttk.Label(mainframe, text = "Address").grid(column = 3, row = 6, sticky =W)
ttk.Label(mainframe, text = "Zip Code").grid(column = 3, row = 7, sticky =W)
ttk.Label(mainframe, text = "            Ship").grid(column = 6, row = 1, sticky =W)
ttk.Label(mainframe, text = "Shipping").grid(column = 5, row = 2, sticky =W)
ttk.Label(mainframe, text = "Tax: ", textvariable=tax).grid(column = 6, row = 3, sticky =W)
ttk.Label(mainframe, text = "Total: ", textvariable=total).grid(column = 6, row = 4, sticky =W)
tax.set("Tax: $")
total.set("Total: $")
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#continues the loop
root.mainloop()