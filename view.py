import datetime

import model
import text


def choice_menu() -> int:
    for n, item in enumerate(text.menu_main):
        if n == 0:
            print(item)
        else:
            print(f'\t{n}. {item}')
    while True:
        choise = input(text.choise_menu)
        if choise.isdigit() and 0 < int(choise) < len(text.menu_main):
            return int(choise)
        print(f'{text.error_choise} {len(text.menu_main) - 1}')


def add_new_notes():
    nb = model.NotesBook()
    new_notes = []
    id_note = nb.next_id()
    new_notes.append(id_note)
    in_notes(new_notes)
    nb.add_new_notes(new_notes)


def print_massage(massage: str):
    print('\n' + '=' * len(massage))
    print(massage)
    print('=' * len(massage) + '\n')


def in_notes(in_notes: list[str]):
    headline = input(text.new_contact_headline)
    in_notes.append(headline)
    annotazione = input(text.new_contact_annotazione)
    in_notes.append(annotazione)
    date_now = str(datetime.datetime.now())
    in_notes.append(date_now)


def edit_notes(id_edit: str):
    edit_note = [id_edit]
    in_notes(edit_note)
    return edit_note