import csv

import text
import view


class Record:
    def __init__(self, id: str, headline: str, annotazione: str, time: str):
        self.id = id
        self.headline = headline
        self.annotazione = annotazione
        self.time = time

    def to_str(self, sep: str = ' '):
        return f'{self.id}{sep}{self.headline}{sep}{self.annotazione}{sep}{self.time}'


class NotesBook:
    def __init__(self, path: str = 'notes.csv', separator: str = ';'):
        self.path = path
        self.separator = separator

    def open_notes(self):
        try:
            with open(self.path, 'r') as file:
                reader = csv.reader(file, delimiter=self.separator)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(text.error_open_notes)
            nb = NotesBook()
            nb.add_column_names()

    def add_new_notes(self, inNewNote=list[str]):
        try:
            if open(self.path):
                with open(self.path, 'a') as file:
                    writer = csv.writer(file, delimiter=self.separator, lineterminator="\r")
                    writer.writerow(inNewNote)
        except FileNotFoundError:
            print(text.error_open_notes)
            nb = NotesBook()
            nb.add_column_names()

    def add_column_names(self):
        with open(self.path, 'x') as file:
            writer = csv.writer(file, delimiter=self.separator, lineterminator="\r")
            writer.writerow(text.column_names)

    def next_id(self) -> int:
        try:
            nb = NotesBook()
            return nb.count_row()
        except FileNotFoundError:
            print(text.error_open_notes)
            nb = NotesBook()
            nb.add_column_names()
            return 1

    def count_row(self):
        with open(self.path) as file:
            return sum(1 for line in file)

    def edit_note(self, id_num: int):
        try:
            note_csv =[]
            with open(self.path, 'r') as file:
                reader = csv.reader(file, delimiter=self.separator)
                for line in reader:
                    note_csv.append(line)
            test = note_csv[id_num]
            id_str = str(id_num)
            edit_note = view.edit_notes(id_str)
            note_csv[id_num] = edit_note
            with open(self.path, 'w') as file:
                writer = csv.writer(file, delimiter=self.separator, lineterminator="\r")
                for i in note_csv:
                    writer.writerow(i)
            view.print_massage(text.edit_and)
        except FileNotFoundError:
            print(text.error_open_notes)
            nb = NotesBook()
            nb.add_column_names()
        except IndexError:
            print(text.error_id_dont)

    def delite_note(self, id_del: int):
        try:
            note_csv =[]
            with open(self.path, 'r') as file:
                reader = csv.reader(file, delimiter=self.separator)
                for line in reader:
                    note_csv.append(line)
            test = note_csv[id_del]
            note_csv.pop(id_del)
            long_note = len(note_csv)
            with open(self.path, 'w') as file:
                writer = csv.writer(file, delimiter=self.separator, lineterminator="\r")
                for i in note_csv:
                    writer.writerow(i)
        except FileNotFoundError:
            print(text.error_open_notes)
            nb = NotesBook()
            nb.add_column_names()