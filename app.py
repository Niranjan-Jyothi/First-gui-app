import tkinter as tk
from tkinter import filedialog, Text
import os

apps=[]
if os.path.isfile('save.txt'):
    with open('save.txt') as f:
       apps = f.read().split(',')
       apps =[app for app in apps if app!='']
       print(apps)

root = tk.Tk()

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    app = filedialog.askopenfilename(initialdir = '/' , title = "Select App" , filetypes=(("executables","*.exe"),("all files", "*.*")))
    if app!="":
      apps.append(app)
    for app in apps:
        label = tk.Label(frame, text=app , bg='#204051')
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height =700 , width = 700 , bg='#84a9ac')
canvas.pack()

frame = tk.Frame(root , bg='#cae8d5')
frame.place(relwidth=0.8 , relheight=0.8, relx=0.1 , rely=0.1 )

selectApps = tk.Button(root , text = "Select Apps", padx=10,width=8, pady=5,fg='#c2f0fc',bg='#204051', command=addApp)
selectApps.pack()
runApps = tk.Button(root , text = "Run Apps",width=8, padx=10, pady=5,fg='#c2f0fc',bg='#204051',command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app, bg='#204051')
    label.pack()

root.mainloop()

with open('save.txt' , 'w') as f:
    for app in apps:
        f.write(app+',')