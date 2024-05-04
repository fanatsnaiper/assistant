import configparser
import os
from os import walk
import shutil
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QLabel,QFileDialog,QGridLayout
from PyQt5.QtWidgets import *
import settings_menu
import messagebox
from design import add_module_menu

class Add_module(QtWidgets.QMainWindow, add_module_menu.Ui_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #объявление переменных
        self.atachments = []
        #привязка функций
        self.back_button.clicked.connect(self.return_to_main)
        self.browse_file_button.clicked.connect(self.getFileName)
        self.atachments_button.clicked.connect(self.show_atachments)
        self.save_button.clicked.connect(self.save_module)
    
    def return_to_main(self):
        try:
            self.form = settings_menu.Settings()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def getFileName(self):
        file_adress, file_type = QFileDialog.getOpenFileNames(self,
                            "Выбрать файл",
                            "c:/Users/Home/Documents",
                            "Library Files(*.pyd)")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path= dir_path + f"/modules"
        if file_adress:
            file = [file_adress[0],dir_path]
            self.atachments.append(file)
            self.save_button.setEnabled(True)
            self.atachments_button.setEnabled(True)
        else:
            pass

    def show_atachments(self):
        filenames = next(walk(f"{os.path.dirname(os.path.realpath(__file__))}/modules"), (None, None, []))[2]  #массив с именами файлов из указанной папки
        grid = QGridLayout()
        message = QDialog(self)
        message.setWindowFlags(message.windowFlags() & (~QtCore.Qt.WindowContextHelpButtonHint)) #убирает из шапки всплывающего окна кнопку с вопросительным знаком
        message.setWindowTitle("Список вложений")
        saved_label = QLabel(self)
        new_label = QLabel(self)
        saved_label.setText("Добавленные:")
        new_label.setText("Новые:")
        saved_attaches = QTextEdit(self)
        new_attaches = QTextEdit(self)
        new_attaches.resize(300,150)
        saved_attaches.resize(300,150)
        saved_list = ""
        new_list = ""
        #переделать
        '''for i in range (0,len(os.listdir(path=self.notes_dir+f"/{self.file}"))-1):   #заполнение раздела 'Сохраненные' всплывающего меню
            saved_list += f"{filenames[i]}\n"'''
        if self.atachments: # проверка на наличие новых вложений и заполнение раздела 'Новые' всплывающего меню
            for file in self.atachments:
                new_list+= f"{file[0]}\n"
            new_attaches.setText(new_list)
        else:
            pass
        self.new_attaches = new_attaches
        saved_attaches.setText(saved_list)
        grid.addWidget(saved_label,0,0)
        grid.addWidget(new_label,0,150)
        grid.addWidget(saved_attaches,10,0)
        grid.addWidget(new_attaches,10,150)
        message.setLayout(grid)
        message.show()  # отображение всплывающего окна

    def save_module(self):
        for file in self.atachments:
            if os.path.exists(f"{os.path.dirname(os.path.realpath(__file__))}/modules/{os.path.splitext(os.path.basename(file[0]))[0]}"): # проверяет, есть ли уже этот файл в папке
                pass    # предлагать перезаписать файл
            else:
                shutil.copy(file[0], file[1], follow_symlinks=True)
        self.atachments = []    #очистка памяти для опустошения раздела 'Новые' всплывающего меню
        self.save_button.setEnabled(False)