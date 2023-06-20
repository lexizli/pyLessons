import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Note:
    def __init__(self, num, date, title, content):
        self.num = num
        self.date = date
        self.title = title
        self.content = content


class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Заметки")

        # список заметок
        note_frame = tk.Frame(self.root)
        note_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(note_frame, text="Список заметок:").pack(pady=10)

        self.note_listbox = tk.Listbox(note_frame, width=30, height=20)
        self.note_listbox.pack()

        # загружаем все заметки из csv-файла в список notes
        self.notes = []
        with open("notes.csv") as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                note = Note(*row)
                self.notes.append(note)
                self.note_listbox.insert(tk.END, f"{note.num} - {note.date} - {note.title}")

        self.note_listbox.bind("<Double-Button-1>", self.view_note)

        # кнопки
        button_frame = tk.Frame(self.root)
        # button_frame.pack(side=tk.LEFT, padx=20)

        # tk.Button(button_frame, text="Добавить новую заметку", command=self.add_note).pack(pady=10)
        # tk.Button(button_frame, text="Удалить заметку", command=self.delete_note).pack(pady=10)
        # tk.Button(button_frame, text="Сортировать по заголовку", command=self.sort_by_title).pack(pady=10)
        # tk.Button(button_frame, text="Сортировать по дате", command=self.sort_by_date).pack(pady=10)
        # tk.Button(button_frame, text="Сортировать по номеру", command=self.sort_by_id).pack(pady=10)

        button_frame.pack(side=tk.LEFT, pady=35)

        tk.Button(button_frame, text="Добавить новую заметку", command=self.add_note, width=20,
                  height=3).grid(row=0, column=0, padx=10, pady=6)
        tk.Button(button_frame, text="Удалить заметку", command=self.delete_note, width=20,
                  height=3).grid(row=2, column=0, padx=10, pady=6)
        tk.Button(button_frame, text="Сортировать по заголовку", command=self.sort_by_title, width=20,
                  height=3).grid(row=3, column=0, padx=10, pady=6)
        tk.Button(button_frame, text="Сортировать по дате", command=self.sort_by_date, width=20,
                  height=3).grid(row=4, column=0, padx=10, pady=6)
        tk.Button(button_frame, text="Сортировать по номеру", command=self.sort_by_id, width=20,
                  height=3).grid(row=5, column=0, padx=10, pady=6)

        # правая панель
        detail_frame = tk.Frame(self.root)
        detail_frame.pack(side=tk.LEFT, padx=20)

        # поля для ввода информации о заметке
        # tk.Label(detail_frame, text="Дата/время:").pack(pady=5)
        # self.date_entry = tk.Entry(detail_frame, width=50)
        # self.date_entry.pack()

        tk.Label(detail_frame, text="Дата/время:").pack(pady=5, anchor="w")
        self.date_entry = tk.Entry(detail_frame, width=40)
        self.date_entry.pack()

        tk.Label(detail_frame, text="Заголовок:").pack(pady=5, anchor="w")
        self.title_entry = tk.Entry(detail_frame, width=40)
        self.title_entry.pack()

        tk.Label(detail_frame, text="Содержимое:").pack(pady=5, anchor="w")
        self.content_text = tk.Text(detail_frame, height=10, width=51)
        self.content_text.pack()

        # кнопки сохранения и отмены изменений
        button_frame2 = tk.Frame(detail_frame)
        button_frame2.pack(pady=23)

        tk.Button(button_frame2, text="Сохранить", command=self.save_note, width=10,
                  height=2).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame2, text="Отменить", command=self.cancel, width=10,
                  height=2).pack(side=tk.LEFT, padx=10)

        # отображение первой заметки в списке при запуске приложения
        if len(self.notes) > 0:
            self.current_note = self.notes[0]
            self.display_note()

    def display_note(self):
        self.date_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

        self.date_entry.insert(0, self.current_note.date)
        self.title_entry.insert(0, self.current_note.title)
        self.content_text.insert("1.0", self.current_note.content)

    def view_note(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.current_note = self.notes[index]
            self.display_note()

    def add_note(self):
        # добавляем новую заметку в список и в listbox
        num = len(self.notes) + 1
        date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")  # текущая дата и время
        title = "Новая заметка"
        content = ""
        note = Note(num, date, title, content)
        self.notes.append(note)
        self.note_listbox.insert(tk.END, f"{note.num} - {note.date} - {note.title}")

        # выбираем новую заметку и отображаем ее содержимое
        self.note_listbox.selection_clear(0, tk.END)
        self.note_listbox.selection_set(tk.END)
        self.note_listbox.activate(tk.END)
        self.current_note = note
        self.display_note()

    def delete_note(self):
        # удаляем выбранную заметку из списка и из listbox
        selection = self.note_listbox.curselection()
        if selection:
            index = selection[0]
            self.notes.pop(index)
            self.note_listbox.delete(index)

            # выбираем новую заметку и отображаем ее содержимое
            if len(self.notes) > 0:
                if index == len(self.notes):
                    index -= 1
                self.note_listbox.selection_clear(0, tk.END)
                self.note_listbox.selection_set(index)
                self.note_listbox.activate(index)
                self.current_note = self.notes[index]
                self.display_note()
            else:
                self.current_note = None

    def sort_by_title(self):
        # сортируем заметки по заголовку
        self.notes.sort(key=lambda note: note.title.lower())
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, f"{note.num} - {note.date} - {note.title}")

    def sort_by_id(self):
        # сортируем заметки по номеру
        self.notes.sort(key=lambda note: note.num)
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, f"{note.num} - {note.date} - {note.title}")

    def sort_by_date(self):
        # сортируем заметки по дате
        self.notes.sort(key=lambda note: note.date.lower())
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, f"{note.num} - {note.date} - {note.title}")

    def save_note_to_csv(self):
        # сохраняем список заметок в csv-файл
        with open("notes.csv", mode="w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            for note in self.notes:
                writer.writerow([note.num, note.date, note.title, note.content])

    def save_note(self):
        # сохраняем изменения текущей заметки
        self.current_note.date = self.date_entry.get()
        self.current_note.title = self.title_entry.get()
        self.current_note.content = self.content_text.get("1.0", tk.END)

        # обновляем отображение списка заметок и содержимого текущей заметки
        if self.note_listbox.curselection():
            index = self.note_listbox.curselection()[0]
            self.note_listbox.delete(index)
            self.note_listbox.insert(index,
                                     f"{self.current_note.num} - {self.current_note.date} - {self.current_note.title}")
        self.display_note()

        # сохраняем изменения в csv-файл
        self.save_note_to_csv()

    def cancel(self):
        # отменяем изменения текущей заметки и перезагружаем ее содержимое
        self.display_note()

    def quit(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти из приложения?"):
            self.root.destroy()


root = tk.Tk()
app = NoteApp(root)
root.protocol("WM_DELETE_WINDOW", app.quit)
root.mainloop()