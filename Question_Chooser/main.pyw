from tkinter import *
from tkinter import ttk
import os
from tkinter.font import BOLD, ITALIC
import mysql.connector as msqlc
from random import randint
from datetime import date

con = msqlc.connect(
    host="localhost",
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS'),
    database="dbase"
)
cursor = con.cursor()


def db():
    # DB queries

    if con.is_connected:
        query = "create table if not exists Question_Chooser (Slno int primary key auto_increment,Date date,questionNo int)"
        cursor.execute(query)
        Q_NO = randint(1, 43)
        query = "select questionNo from Question_Chooser"
        cursor.execute(query)
        li = []
        for i in cursor:
            li.append(i[0])
        if Q_NO not in li:
            query = f"insert into Question_Chooser (Slno,Date,questionNo) values({len(li)+1},'{date.today()}',{Q_NO})"
            cursor.execute(query)
            return f"Your Magic Question No for today ( {date.today()} ) is {Q_NO} on {len(li)+1}"

    else:
        return "Error in connection"


# Tkinter Graphics
root = Tk()
root.iconphoto(False, PhotoImage(file="icon.png"))
root.title("Question Chooser")
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="WELCOME TO QUESTION CHOOSER APP",
          font=("Arial", 25, ITALIC, BOLD)).grid(column=0, row=0)
ttk.Label(frm, text=str(db()), font=(
    "Times New Roman", 20), padding=10).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()


con.commit()
cursor.close()
con.close()
