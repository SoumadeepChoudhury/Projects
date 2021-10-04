import tkinter as tk
from tkinter import Tk
import time
from datetime import datetime
from plyer import notification
from tkinter.font import Font
class AlarmClock(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        root.title("Alarm Clock")
        root.iconbitmap('icon.ico')
        root.config(background='black')
        root.geometry('500x150')
        self.hourstr=tk.StringVar(self,datetime.now().strftime("%H"))
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=4,state="readonly",font=Font(size=36))
        self.minstr=tk.StringVar(self,datetime.now().strftime("%M"))
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=4,state="readonly",font=Font(size=36))
        self.hour.grid()
        self.min.grid(row=0,column=1)
        self.btn = tk.Button(root, text = 'Set !',
                          command = self.alarm,font=Font(size=36))
        self.btn.pack(side = 'bottom')

    def alarm(self):
        root.withdraw()
        while(True):
            if(datetime.now().strftime("%H").lstrip("0")==self.hourstr.get() and datetime.now().strftime("%M").lstrip("0")==self.minstr.get()):
                notification.notify(
                    title="**Hey Dude, Have worked enough.!",
                    message="Get up from your chair and take 5 min halt and restart NEET Preparation.",
                    app_icon="G:\Projects\Alarm Clock\icon.ico",
                    timeout=10
                    )
                break
            time.sleep(1)
        root.destroy()
    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()
root = tk.Tk()
AlarmClock(root).pack()
root.mainloop()
