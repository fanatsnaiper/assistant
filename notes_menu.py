import configparser
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
import main_menu, in_note, new_note
from design import notes_design
import messagebox

class Notes(QtWidgets.QMainWindow, notes_design.Ui_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #предварительная проверка
        config = configparser.ConfigParser()  # опостылевший конфигпарсер.конфигпарсер.конфигпарсер.конфигпарсер
        config.read('config.ini')
        program_dir = os.path.dirname(os.path.abspath(__file__))
        notes_dir = f'{program_dir}/{config["Default_Dir"]["notes"]}'
        self.notes_dir = notes_dir
        if os.path.exists(notes_dir):
            pass
        else:
            os.makedirs(notes_dir)
        icons_dir = f'{program_dir}/{config["Default_Dir"]["icons"]}' 
        self.dirs = [program_dir,notes_dir,icons_dir]
        #привязка функций
        self.back_button.clicked.connect(self.return_to_main)
        self.create_note_button.clicked.connect(self.create_note)
        files_list = os.listdir(notes_dir)
        self.coordinates_arr = []    #массив для записи координат кнопок
        lay = QFormLayout()
        self.scrollArea.setLayout(lay)
        try:
            for file in files_list: #заполнение заглавного окна Заметки кнопками по каждой заметке
                ini_file =(notes_dir+f"/{file}"+f"/{file}.ini")
                config = configparser.ConfigParser()
                config.read(ini_file)
                section = file[0].upper()+file[1:]
                title = config[f"{section}"]["title"]   #считывание заголовков из .ini каждой папки заметок
                self.button = QPushButton()
                self.button.setFixedSize(100,40)
                self.button.setObjectName(f"{file}")
                self.button.setText(f"{title}") 
                self.button.clicked.connect(self.open_note)
                lay.addWidget(self.button)
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def contextMenuEvent(self, event):  # доработать функцию. должна определять попадание курсора на кнопку и вызывать контекстное меню
        for set in self.coordinates_arr:
            if (set[0] <= self.scrollArea.mapFromGlobal(QCursor.pos()).x() <= (set[0]+set[2])) and (set[1] <= self.scrollArea.mapFromGlobal(QCursor.pos()).y()<=(set[1]+set[3])):
                contextMenu = QMenu(self)
                deleteAct = contextMenu.addAction("Delete")
                action = contextMenu.exec_(self.mapToGlobal(event.pos()))
                if action == deleteAct:
                    print("Удаление")
                else:
                    print("Другое какое-то что-то")
            else:
                print("Не прошло по условиям")
    
    def return_to_main(self):
        try:
            self.form = main_menu.Main_menu()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)
    
    def create_note(self):
        try:
            self.form = new_note.New_note(self.dirs)
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def open_note(self):
        try:
            file = self.sender().objectName()
            self.form = in_note.In_note(file,self.dirs)
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)