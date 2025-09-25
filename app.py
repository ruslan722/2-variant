import tkinter as tk
from tkinter import Label, PhotoImage, messagebox, Entry, Button
from connect import App, Two_widow

root = tk.Tk()
root.title('Компания обоев')
root.geometry('600x600')
root.resizable(False, False)
root.configure(bg='#FFFFFF')

def widow_app(event=None):
    shapka = Label(root, bg='#405C73', width=40, height=2, text='Окно первое',
                fg='#FFFFFF', font=('Constantia', 20))
    shapka.place(x=0, y=0)

    logo = PhotoImage(file='logo.png')
    logo = logo.subsample(20)
    logo_label = Label(shapka, image=logo, bg='#405C73')
    logo_label.image = logo 
    logo_label.place(x=5, y=5)

    def add_window():
        frame_app = tk.Toplevel()
        frame_app.title('Добавление записи')
        frame_app.geometry('300x300')
        frame_app.resizable(False, False)

        type = Label(frame_app, text='Тип', font=('Constantia', 10))
        type.place(x=5, y=5)
        type_entry = Entry(frame_app)
        type_entry.place(x=100, y=5)

        name = Label(frame_app, text='Наименование', font=('Constantia', 10))
        name.place(x=5, y=30)
        name_entry = Entry(frame_app)
        name_entry.place(x=100, y=30)

        article = Label(frame_app, text='Артикул', font=('Constantia', 10))
        article.place(x=5, y=55)
        article_entry = Entry(frame_app)
        article_entry.place(x=100, y=55)

        min_price = Label(frame_app, text='Мин. ст.', font=('Constantia', 10))
        min_price.place(x=5, y=80)
        min_price_entry = Entry(frame_app)
        min_price_entry.place(x=100, y=80)

        width = Label(frame_app, text='Ширина', font=('Constantia', 10))
        width.place(x=5, y=105)
        width_entry = Entry(frame_app)
        width_entry.place(x=100, y=105)

        price = Label(frame_app, text='Стоимость', font=('Constantia', 10))
        price.place(x=5, y=130)
        price_entry = Entry(frame_app)
        price_entry.place(x=100, y=130)

        def add_baza():
            type = type_entry.get()
            name = name_entry.get()
            article = article_entry.get()
            min_price = min_price_entry.get()
            width = width_entry.get()
            price = price_entry.get()

            _ = App.create(
                type=type,
                name=name,
                article=article,
                min_price=min_price,
                width=width,
                price=price
            )
            messagebox.showinfo('Успех', 'Запись добавлена')
            frame_app.destroy()

        save_btn = Button(frame_app, text="Сохранить", bg="#405C73", fg="white",
                          font=("Constantia", 10), command=add_baza, width=15, height=1)
        save_btn.place(x=85, y=180)

    add_btn = Button(root, bg='#405C73', width=15, text='Добавить запись',
                     fg='#FFFFFF', font=('Constantia', 10),
                     command=add_window)
    add_btn.place(x=240, y=550)

def mat():
        material = App.select()
        return material

Oboi = mat()

y_position = 80

for i in Oboi:
        zone = Label(root, bg='#BFD5F6', width=80, height=7)
        zone.place(x=15, y=y_position)

        type = Label(zone, bg='#BFD5F6',
                    text=f'{i.type} | {i.name}', font=('Constantia', 12))
        type.place(x=15, y=5)

        article = Label(zone, bg='#BFD5F6',
                        text=f'Артикул: {i.article}', font=('Constantia', 10))
        article.place(x=15, y=30)

        min_price = Label(zone, bg='#BFD5F6',
                        text=f'Минимальная стоимость для партнера: {i.min_price} руб.', font=('Constantia', 10))
        min_price.place(x=15, y=50)

        width = Label(zone, bg='#BFD5F6',
                    text=f'Ширина: {i.width} м', font=('Constantia', 10))
        width.place(x=15, y=70)

        price = Label(zone, bg='#BFD5F6',
                    text=f'Стоимость: {i.price} руб.', font=('Constantia', 12))
        price.place(x=360, y=5)

        y_position += 130

def two_widow_app(event=None):
    shapka = Label(root, bg='#405C73', width=40, height=2, text='Окно второе',
                fg='#FFFFFF', font=('Constantia', 20))
    shapka.place(x=0, y=0)

    logo = PhotoImage(file='logo.png')
    logo = logo.subsample(20)
    logo_label = Label(shapka, image=logo, bg='#405C73')
    logo_label.image = logo
    logo_label.place(x=5, y=5)

    messagebox.showerror('Внимание', 'Ошибка')
    messagebox.showwarning('Внимание', 'Предупреждение')
    messagebox.showinfo('Внимание', 'Информация об ошибке')

    def mat():
        material = Two_widow.select()
        return material

    Oboi = mat()

    y_position = 80

    for i in Oboi:
        zone2 = Label(root, bg='#BFD5F6', width=80, height=7)
        zone2.place(x=15, y=y_position)

        type = Label(zone2, bg='#BFD5F6',
                    text=f'{i.material}', font=('Constantia', 12))
        type.place(x=15, y=5)

        kolvo = Label(zone2, bg='#BFD5F6',
                      text=f'Количество: {i.kolvo}', font=('Constantia', 10))
        kolvo.place(x=15, y=30)

        y_position += 130


back_btn = Label(root, text=' <', bg='#405C73', fg='white',
                 font=('Constantia', 12), width=8, height=2)
back_btn.place(x=100, y=540)

back_btn.bind('<Button-1>', lambda e: widow_app())
next_btn = Label(root, text=' >', bg='#405C73', fg='white',
                 font=('Constantia', 12), width=8, height=2)
next_btn.place(x=430, y=540)
next_btn.bind('<Button-1>', lambda e: two_widow_app())

widow_app()
root.mainloop()
