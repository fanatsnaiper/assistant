import main_menu
from design import settings
from PyQt5 import QtWidgets
import messagebox

class Settings(QtWidgets.QMainWindow, settings.Ui_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        #привязка функций
        self.back_button.clicked.connect(self.leave_to_main)

    def leave_to_main(self):
        try:
            self.form = main_menu.Main_menu()
            self.form.show()
            self.close()
        except Exception as e:
            messagebox.show_warning_messagebox(e)