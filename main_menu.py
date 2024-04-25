import configparser
import sys
import os
from PyQt5 import QtWidgets
import settings_menu
import notes_menu
import boards
import messagebox
from design import main_menu_design

class Main_menu(QtWidgets.QMainWindow, main_menu_design.Ui_main_menu):  
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #предварительная проверка
        config = configparser.ConfigParser()  # опостылевший конфигпарсер.конфигпарсер.конфигпарсер.конфигпарсер
        config.read('config.ini')
        program_dir = os.path.dirname(os.path.abspath(__file__))
        memory_dir = f'{program_dir}/{config["Default_Dir"]["memory"]}' #адрес папки memory
        if os.path.exists(memory_dir):  # проверка существования папки памяти приложения
            #привязка функций
            self.boards_button.clicked.connect(self.open_boards)
            self.notes_button.clicked.connect(self.open_notes)
            self.settings_button.clicked.connect(self.open_settings)
        else:
            #отключение кнопок
            self.boards_button.setEnabled(False)
            self.notes_button.setEnabled(False)
            self.settings_button.setEnabled(False)
        #привязка функций
        self.exit_button.clicked.connect(self.application_close)

    def open_boards(self):
        try:
            self.form = boards.Connection_menu()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)


    def open_notes(self):
        try:
            self.form = notes_menu.Notes()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def open_settings(self):
        try:
            self.form = settings_menu.Settings()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def application_close(self):
        sys.exit()
    
def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = Main_menu()
        window.show()
        app.exec_()
    except Exception as e:
        messagebox.show_warning_messagebox(e)