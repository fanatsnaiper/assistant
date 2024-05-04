import configparser
import sys
import os
from os import walk
from PyQt5 import QtWidgets,QtCore
import settings_menu
import notes_menu
import importlib.util
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
            self.notes_button.clicked.connect(self.open_notes)
            self.settings_button.clicked.connect(self.open_settings)
        else:
            #отключение кнопок
            self.boards_button.setEnabled(False)
            self.notes_button.setEnabled(False)
            self.settings_button.setEnabled(False)
        #проверка модулей
        #создавать кнопку для каждого модуля
        filenames = next(walk(f"{os.path.dirname(os.path.abspath(__file__))}/modules"), (None, None, []))[2]
        for file in filenames: 
            name = file.split(".")[0]
            self.button = QtWidgets.QPushButton(self.centralwidget)
            self.button.setGeometry(QtCore.QRect(0, 0, 150, 50))
            self.button.setObjectName(f"{file}")
            self.button.setText(f"{name.upper()}")
            self.button.clicked.connect(self.func)
        #привязка функций
        self.exit_button.clicked.connect(self.application_close)
    
    def func(self):
        try:
            file = self.sender().objectName()
            name = file.split(".")[0]
            print(file)
            spec=importlib.util.spec_from_file_location(f"{name}",f"modules/{file}")
            foo = importlib.util.module_from_spec(spec)
            self.close()
            spec.loader.exec_module(foo)
            foo.main()
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