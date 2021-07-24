import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='python.png')  # загрузка иконки программы
win.iconphoto(False, photo)  # установка иконки программы
win.title('Тестовое окно')  # заголовок окна
win.geometry("900x600+100+60")  # размеры окна "ШиринахВысота+Лево+Верх"
win.resizable(False, False)  # запрещаем растягивать по ширине и высоте
win.config(bg='blue')  # установка цвета фона окна
win.config(bg='#2DFF00')  # установка цвета фона окна

win.mainloop()
