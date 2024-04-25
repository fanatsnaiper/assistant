from PyQt5.QtWidgets import QMessageBox

def show_warning_messagebox(text): 
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Warning) 
        # setting message for Message Box 
        msg.setText(f"{text}") 
        # setting Message box window title 
        msg.setWindowTitle("Warning MessageBox") 
        # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        # start the app 
        retval = msg.exec_() 