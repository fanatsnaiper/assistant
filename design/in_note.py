# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'in_note.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.back_button.setObjectName("back_button")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 55, 800, 545))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 798, 543))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.input_title = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.input_title.setGeometry(QtCore.QRect(20, 30, 171, 31))
        self.input_title.setObjectName("input_title")
        self.label_title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 80, 16))
        self.label_title.setObjectName("label_title")
        self.label_body = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_body.setGeometry(QtCore.QRect(20, 70, 90, 16))
        self.label_body.setObjectName("label_body")
        self.input_body = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.input_body.setGeometry(QtCore.QRect(20, 100, 761, 431))
        self.input_body.setObjectName("input_body")
        self.add_image_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add_image_button.setGeometry(QtCore.QRect(750, 70, 25, 25))
        self.add_image_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("design/icons/add_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_image_button.setIcon(icon)
        self.add_image_button.setObjectName("add_image_button")
        self.add_doc_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add_doc_button.setGeometry(QtCore.QRect(720, 70, 25, 25))
        self.add_doc_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("design/icons/add_doc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_doc_button.setIcon(icon1)
        self.add_doc_button.setObjectName("add_doc_button")
        self.atachments_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.atachments_button.setEnabled(False)
        self.atachments_button.setGeometry(QtCore.QRect(600, 70, 93, 28))
        self.atachments_button.setObjectName("atachments_button")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.save_changes_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_changes_button.setEnabled(False)
        self.save_changes_button.setGeometry(QtCore.QRect(650, 0, 150, 50))
        self.save_changes_button.setObjectName("save_changes_button")
        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Заметки"))
        self.back_button.setText(_translate("window", "Назад"))
        self.label_title.setText(_translate("window", "Заголовок:"))
        self.label_body.setText(_translate("window", "Тело заметки:"))
        self.atachments_button.setText(_translate("window", "Вложения"))
        self.save_changes_button.setText(_translate("window", "Сохранить изменения"))