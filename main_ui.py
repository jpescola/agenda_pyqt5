# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(10, 10, 432, 190))
        self.calendario.setObjectName("calendario")
        self.excluir = QtWidgets.QPushButton(self.centralwidget)
        self.excluir.setGeometry(QtCore.QRect(10, 500, 80, 26))
        self.excluir.setObjectName("excluir")
        self.lista = QtWidgets.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(10, 210, 431, 281))
        self.lista.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.lista.setObjectName("lista")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 21))
        self.menubar.setObjectName("menubar")
        self.menuAgenda = QtWidgets.QMenu(self.menubar)
        self.menuAgenda.setObjectName("menuAgenda")
        self.menuSistema = QtWidgets.QMenu(self.menubar)
        self.menuSistema.setObjectName("menuSistema")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionNova = QtWidgets.QAction(MainWindow)
        self.actionNova.setObjectName("actionNova")
        self.menuAgenda.addAction(self.actionNova)
        self.menuSistema.addAction(self.actionSair)
        self.menubar.addAction(self.menuAgenda.menuAction())
        self.menubar.addAction(self.menuSistema.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda"))
        self.excluir.setText(_translate("MainWindow", "&Excluir"))
        self.menuAgenda.setTitle(_translate("MainWindow", "Agenda"))
        self.menuSistema.setTitle(_translate("MainWindow", "Sistema"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionNova.setText(_translate("MainWindow", "Nova"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
