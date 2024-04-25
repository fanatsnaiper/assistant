import configparser
import os
from os import walk
import shutil
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QLabel,QFileDialog,QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import notes_menu
import messagebox
from design import new_note

class New_note(QtWidgets.QMainWindow, new_note.Ui_window):
    def __init__(self,dirs):
        super().__init__()
        self.setupUi(self)
        #распаковка массива
        self.dirs = dirs
        self.notes_dir = dirs[1]
        #привязка функций
        self.back_button.clicked.connect(self.return_to_main)
        self.save_note_button.clicked.connect(self.save_note)
        self.input_title.textChanged.connect(self.button_enable) 
        self.input_body.textChanged.connect(self.button_enable) 
        self.atachments_button.clicked.connect(self.show_atachments)
        self.add_image_button.clicked.connect(self.getImageName)
        self.add_doc_button.clicked.connect(self.getFileName)
        label = QLabel(self)
        pixmap = QPixmap('photo.jpg')
        pixmap = pixmap.scaled(400,200)
        label.setPixmap(pixmap)
        label.move(15,10)
        label.resize(180,60)
        self.file = ''
        self.atachments = []
        #расчет индекса и адреса папки
        self.i = len(next(os.walk(self.notes_dir))[1])+1
        self.current_dir = self.notes_dir+f'/note_{self.i}'

    def show_atachments(self):
        if self.file:
            filenames = next(walk(self.file), (None, None, []))[2]  #массив с именами файлов из указанной папки
        else:
            filenames = []
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
        if self.file :
            for i in range (0,len(os.listdir(path=self.file))-1):   #заполнение раздела 'Сохраненные' всплывающего меню
                saved_list += f"{filenames[i]}\n"
        else:
            saved_list ="Сохранённых вложений нет"
        if self.atachments: # проверка на наличие новых вложений и заполнение раздела 'Новые' всплывающего меню
            for file in self.atachments:
                new_list+= f"{file}\n"
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
                            "c:/Users/Home/Documents",
                            "PNG Files(*.png)")
        if file_adress:
            self.atachments.append(file_adress[0])
            self.atachments_button.setEnabled(True)
            self.save_note_button.setEnabled(True)
        else:
            pass
     
    def getFileName(self):
        file_adress, file_type = QFileDialog.getOpenFileNames(self,
                            "Выбрать файл",
                            "c:/Users/Home/Documents",
                            "Text Files(*.txt)")
        if file_adress:
            self.atachments.append(file_adress[0])
            self.atachments_button.setEnabled(True)
            self.save_note_button.setEnabled(True)
        else:
            pass

    def button_enable(self):
        self.save_note_button.setEnabled(True)

    def return_to_main(self):
        try:
            self.form = notes_menu.Notes()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)
    
    def save_note(self):
        #обработать повторное нажатие кнопки 
        i = self.i
        current_dir = self.current_dir
        if os.path.exists(current_dir):
            pass
        else:
            try:
                os.makedirs(current_dir)
            except Exception as e:
                messagebox.show_warning_messagebox(e)
        config_path = current_dir+f'/note_{i}.ini'
        with open(config_path, "w") as config_file: # заносит заголовок и тело заметки в ini файл в папке заметки
            config = configparser.ConfigParser()
            config.add_section(f"Note_{i}")
            config.set(f"Note_{i}","title",f"{self.input_title.toPlainText()}")
            config.set(f"Note_{i}","body",f"{self.input_body.toPlainText()}")
            config.write(config_file)
        for file in self.atachments: 
            if os.path.exists(f"{self.current_dir}/{os.path.splitext(os.path.basename(file))[0]}"): # проверяет, есть ли уже этот файл в папке заметки
                pass    # предлагать перезаписать файл
            else:
                shutil.copy(f"{file}", f"{current_dir}", follow_symlinks=True)  # копирует вложения из их папок в папку заметки
        self.file = current_dir
        self.atachments=[]
        self.save_note_button.setEnabled(False)
