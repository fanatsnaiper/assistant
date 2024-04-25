import configparser
import os
from os import walk
import shutil
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QLabel,QFileDialog,QGridLayout
from PyQt5.QtWidgets import *
import notes_menu
import messagebox
from design import in_note

class In_note(QtWidgets.QMainWindow, in_note.Ui_window):
    def __init__(self,file,dirs):
        super().__init__()
        self.setupUi(self)
        #распаковка массива
        self.notes_dir = dirs[1]
        #привязка функций
        self.back_button.clicked.connect(self.return_to_main)
        self.save_changes_button.clicked.connect(self.save_changes)
        # обработка открытия заметки
        # переменная file 
        self.file = file    # открытие файла по переменной self.file, открытие соответствующего .ini файла и чтение заголовка, тела и вложени
        ini_file =(self.notes_dir+f"/{file}"+f"/{file}.ini")
        self.ini_file = ini_file
        config = configparser.ConfigParser()
        config.read(ini_file)
        section = file[0].upper()+file[1:]
        title = config[f"{section}"]["title"]   # переменная title принимает значения заголовка заметки
        body = config[f"{section}"]["body"] # переменная body принимает значения тела заметки
        self.input_title.setText(f"{title}")
        self.input_body.setText(f"{body}")
        self.input_title.textChanged.connect(self.button_enable) 
        self.input_body.textChanged.connect(self.button_enable)    
        self.atachments_button.clicked.connect(self.show_atachments) 
        self.add_image_button.clicked.connect(self.getImageName)
        self.add_doc_button.clicked.connect(self.getFileName)  
        self.atachments = []
        try:
            if len(os.listdir(path=self.notes_dir+f"/{file}"))>1 : #проверка (подсчетом количества) на наличие файлов в папке(.ini не учитывается, поэтому кол-во должно быть >1) 
                self.atachments_button.setEnabled(True) # включение кнопки 'Вложения' 
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def show_atachments(self):
        filenames = next(walk(self.notes_dir+f"/{self.file}"), (None, None, []))[2]  #массив с именами файлов из указанной папки
        grid = QGridLayout()
        message = QDialog(self)
        message.setWindowFlags(message.windowFlags() & (~QtCore.Qt.WindowContextHelpButtonHint)) #убирает из шапки всплывающего окна кнопку с вопросительным знаком
        message.setWindowTitle("Список вложений")
        saved_label = QLabel(self)
        new_label = QLabel(self)
        saved_label.setText("Сохранённые:")
        new_label.setText("Новые:")
        saved_attaches = QTextEdit(self)
        new_attaches = QTextEdit(self)
        new_attaches.resize(300,150)
        saved_attaches.resize(300,150)
        saved_list = ""
        new_list = ""
        for i in range (0,len(os.listdir(path=self.notes_dir+f"/{self.file}"))-1):   #заполнение раздела 'Сохраненные' всплывающего меню
            saved_list += f"{filenames[i]}\n"
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

    def getImageName(self):
        file_adress, file_type = QFileDialog.getOpenFileNames(self,
                            "Выбрать файл",
                            "c:/Users/Home/Pictures",
                            "PNG Files(*.png)") #переменная file_type  нужна, чтобы исключить сохранение её текста в переменную file_adress
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path= dir_path + f"/memory/notes/{self.file}"
        if file_adress:
            for adress in file_adress:
                file = [adress,dir_path]
                self.atachments.append(file)
            self.save_changes_button.setEnabled(True)
            self.atachments_button.setEnabled(True)
        else:
            pass
    
    def getFileName(self):
        file_adress, file_type = QFileDialog.getOpenFileNames(self,
                            "Выбрать файл",
                            "c:/Users/Home/Documents",
                            "Text Files(*.txt)")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path= dir_path + f"/memory/notes/{self.file}"
        if file_adress:
            file = [file_adress[0],dir_path]
            self.atachments.append(file)
            self.save_changes_button.setEnabled(True)
            self.atachments_button.setEnabled(True)
        else:
            pass

    def button_enable(self):
        self.save_changes_button.setEnabled(True)

    def return_to_main(self):
        try:
            self.form = notes_menu.Notes()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)
    def save_changes(self,file):
        title = self.input_title.toPlainText()
        body = self.input_body.toPlainText()
        config = configparser.ConfigParser()
        config.read(self.ini_file)
        section = self.file[0].upper()+self.file[1:]
        config.set(f"{section}","title", f"{title}")
        config.set(f"{section}","body", f"{body}")
        with open(self.ini_file, "w") as config_file:
            config.write(config_file)
        for file in self.atachments:
            if os.path.exists(f"{self.file[1]}/{os.path.splitext(os.path.basename(file[0]))[0]}"): # проверяет, есть ли уже этот файл в папке заметки
                pass    # предлагать перезаписать файл
            else:
                shutil.copy(file[0], file[1], follow_symlinks=True)
        self.atachments = []    #очистка памяти для опустошения раздела 'Новые' всплывающего меню
        self.save_changes_button.setEnabled(False)