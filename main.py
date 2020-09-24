from tkinter import *
from pprint import pprint
import psycopg2

root = Tk()
textVariable = StringVar()
nameVariable = StringVar()
maxLength = 139

connection = False
try:
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="localhost",
                                  port="5432",
                                  database="ns")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



# root.geometry('200x450')

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


naamLabel = Label(root, text="Naam", font=('Comic Sans MS', 12))
naamLabel.pack()
name = Entry(root, textvariable=nameVariable, relief=RAISED, font=('Comic Sans MS', 12))  # Creates name Input
name.pack()
textLabel = Label(root, text="Bericht", font=('Comic Sans MS', 12))
textLabel.pack()
text = Text(root, relief=RAISED, font=('Comic Sans MS', 12), width=33, height=4)  # Creates Input
text.pack()  # Loads input into window


def character_limit(args):
    print("active")
    textVar = text.get("1.0", "end-1c")
    if len(textVar) > maxLength:
        text.delete(1.0, "end")
        text.insert(1.0, textVar[0:maxLength - len(textVar)])


text.bind('<Key>', character_limit)


def test():
    # post to db
    pprint(text.get("1.0", "end-1c"))


button = Button(root, text="submit", command=test, font=('Comic Sans MS', 12), fg="green", background="pink")
button.pack()

app = Window(root)
root.mainloop()
