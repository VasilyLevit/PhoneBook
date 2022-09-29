import ui
import book_save as bs

def button_click():
    if ui.get_comand() == '1':
        bs.log_data(ui.get_data())


