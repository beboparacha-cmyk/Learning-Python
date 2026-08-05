from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("main")

def topwin():
    project = Toplevel()
    project.geometry("180x100")
    project.title("topLevel")

    l2 = Label(project, text="This is toplevel window")
    l2.pack()

    project.mainloop()

l = Label(window, text="This is root window")
btn = Button(window, text="Click here to open another window", command=topwin)

l.pack()
btn.pack()

window.mainloop() 

