import tkinter as tk
from tkinter import Label, PhotoImage
from connect import App

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

def mat():
    material = App.select()
    return material

Oboi = mat()

y_position = 80

for i in Oboi:
    zone = Label(root, bg = '#BFD5F6', width= 80, height= 7)
    zone.place(x=15, y= y_position)

    type = Label(zone, bg= '#BFD5F6',
                 text= f'{i.type} | {i.name}', font=('Constantia', 12))
    type.place(x=15, y=5)

    article = Label(zone, bg= '#BFD5F6',
                    text= f'Артикул: {i.article}', font=('Constantia', 10))
    article.place(x=15, y= 30)

    min_price = Label(zone, bg= '#BFD5F6' ,
                      text= f'Минимальная стоимость для партнера: {i.min_price} руб.', font=('Constantia', 10))
    min_price.place(x=15, y= 50)

    width = Label(zone, bg= '#BFD5F6',
                    text= f'Ширина: {i.width} м', font=('Constantia', 10))
    width.place(x=15, y= 70)

    price = Label(zone, bg= '#BFD5F6',
                    text= f'Стоимость: {i.price} руб.', font=('Constantia', 12))
    price.place(x=360, y= 5)
                  
    y_position += 130



root.mainloop()
