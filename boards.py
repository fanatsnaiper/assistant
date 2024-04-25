import sys
from PyQt5 import QtWidgets
from design import boards_connect
from co_work import Board_connect
import find_available_ports 
import messagebox
from threading import *

class Connection_menu(QtWidgets.QMainWindow, boards_connect.Ui_mainWindow):  
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #предварительная настройка окна
        self.box_command_window.hide()
        self.available_ports = 'not_checked'
        #привязка функций
        if find_available_ports.serial_ports(): # поиск юсб портов, к которым что-то подключено
            ports_list = find_available_ports.serial_ports()
            #определенить, какое значение высветится в comboBox (для удобства)
            if len(ports_list) > 0 :
                self.box_usb_ports.setCurrentText(f"{ports_list[0]}")   # для удобства берётся первый порт из полученных
                self.available_ports = 'exist'
            else:
                self.available_ports = 'none'
        #кнопка 'Принять' /возможно не нужна
        self.button_accept_params.clicked.connect(self.accept)
        #кнопка 'Подключить' - запускает многопоточность
        self.button_connect.clicked.connect(self.thread)
        #кнопка 'Выйти' - закрывает приложение (перед использованием отключить многопоточность = отключить работу с ардуино = передать нужную команду)
        self.button_back.clicked.connect(self.return_to_main)
        self.button_send_command.clicked.connect(self.command_send)
        #привязка нажатия энтер при работе со строкой
        self.input_command.returnPressed.connect(lambda: self.command_send())

    def return_to_main(self):
        import main_menu
        self.form = main_menu.Main_menu()
        self.form.show()
        self.close()

    def accept(self):
        try:
            self.connection_params = [f"{self.box_usb_ports.currentText()}",int(f"{self.box_baudrate.currentText()}")]  # берет данные из двух comboBox 
            self.button_connect.setEnabled(True)    # активизирует кнопку 'Подключить'
        except Exception as e:
            messagebox.show_warning_messagebox(e)

    def connect(self):
        self.form = Board_connect.main(self,self.connection_params) # открывает порт и запускает работу с ардуино, передает необходимые для порта параметры
        self.box_command_window.show()  # делает доступным окно команд 

    def application_close(self):
        sys.exit()

    def thread(self): 
        if self.available_ports =='exist':  # проверка на наличие доступных портов
            try:
                t1=Thread(target=self.connect)  # вызывает в поток функцию 'connect'
                t1.start()  # запускает многопоточность для работы с ардуино
            except Exception as e:
                messagebox.show_warning_messagebox(e)
        else:
            messagebox.show_warning_messagebox("No available ports")

    def command_send(self):
        if self.input_command.text():   # если текст не нулевой, отправляет команду на commands_dialogue для отображения истории команд и на доску для выполнения
            command = self.input_command.text() # считывает команду
            self.input_command.clear()  # очищает поле ввода команд
            self.commands_dialogue.insertPlainText(f"{command}\n")  # выводит отправленную команду в окно истории 
            Board_connect.send(self,command)    # отправляет команду на доску

def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = Connection_menu()
        window.show()
        app.exec_()
    except Exception:
        print("Одна ошибка и ты ошибся")

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()