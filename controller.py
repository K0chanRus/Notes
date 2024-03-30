import csv

import model
import text
import view


def start_app():
    nb = model.NotesBook()
    while True:
        choice = view.choice_menu()
        match choice:
            case 1:
                nb.open_notes()
            case 2:
                view.add_new_notes()
                view.print_massage(text.add_new_contact)
            case 3:
                nb.edit_note(int(input(text.edit_id_note)))
            case 4:
                nb.delite_note(int(input(text.delite_id_note)))
                view.print_massage(text.delite_and)
            case 5: break
    return None