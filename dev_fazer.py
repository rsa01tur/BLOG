# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import db as conexao

class Ui_MainWindow(object):
    def registrar(self):
        nome = self.lnNome.text()
        telefone = self.lnTel.text()
        oi = "s"
        cpf = self.lnCPF.text()
        qual = "músico"
        if (nome !="" and telefone != "" and cpf != "" ):
            conexao.connectar(cpf, nome, oi, qual, telefone)
        else:
            print("tem erro")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 20, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(420, 120, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(410, 270, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lnNome = QtWidgets.QLineEdit(self.frame)
        self.lnNome.setGeometry(QtCore.QRect(420, 190, 341, 41))
        self.lnNome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lnNome.setObjectName("lnNome")
        self.lnTel = QtWidgets.QLineEdit(self.frame)
        self.lnTel.setGeometry(QtCore.QRect(420, 340, 341, 41))
        self.lnTel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lnTel.setObjectName("lnTel")
        self.pushbuttonRegistrar = QtWidgets.QPushButton(self.frame)
        self.pushbuttonRegistrar.setGeometry(QtCore.QRect(190, 460, 91, 81))
        ##botao clicked metodo registrar
        self.pushbuttonRegistrar.clicked.connect(self.registrar)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.pushbuttonRegistrar.setFont(font)
        self.pushbuttonRegistrar.setObjectName("pushbuttonRegistrar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 231, 251))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("projeto.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(410, 420, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lnCPF = QtWidgets.QLineEdit(self.frame)
        self.lnCPF.setGeometry(QtCore.QRect(420, 480, 341, 41))
        self.lnCPF.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lnCPF.setObjectName("lnCPF")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionX_Close = QtWidgets.QAction(MainWindow)
        self.actionX_Close.setObjectName("actionX_Close")
        self.menuArquivo.addAction(self.actionX_Close)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastro"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label_3.setText(_translate("MainWindow", "Telefone"))
        self.pushbuttonRegistrar.setText(_translate("MainWindow", "Registrar"))
        self.label_5.setText(_translate("MainWindow", "CPF"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionX_Close.setText(_translate("MainWindow", "X Close"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

