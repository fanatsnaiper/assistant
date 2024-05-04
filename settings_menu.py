import main_menu
from design import settings
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, shutil
import messagebox, add_module

class Settings(QtWidgets.QMainWindow, settings.Ui_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        # объявление переменных
        self.dirs = []
        #привязка функций
        self.back_button.clicked.connect(self.return_to_main)
        self.module_menu_button.clicked.connect(self.open_add_module_menu)

    def return_to_main(self):
        try:
            self.form = main_menu.Main_menu()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)
    
    def open_add_module_menu(self):
        try:
            self.form = add_module.Add_module()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)
