import tkinter as tk
from tkinter import Label, PhotoImage

root = tk.Tk()
root.title('Компания обоев')
root.geometry('600x600')
root.resizable(False, False)
root.configure(bg= '#FFFFFF')

shapka = Label(root, bg= '#405C73', width= 40, height= 2, text= 'Окно первое' ,
               fg = '#FFFFFF' , font=('Constantia', 20))
shapka.place(x=0, y=0)

logo = PhotoImage(file='logo.png')
logo = logo.subsample(20)
logo_label = Label(shapka, image = logo , bg= '#405C73')
logo_label.place(x=5, y=5)

root.mainloop()

