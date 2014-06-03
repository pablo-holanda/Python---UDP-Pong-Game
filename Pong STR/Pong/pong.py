# -*- coding: utf-8 -*-
# http://qt-project.org/doc/qt-5/qt.html#Key-enum

from PyQt4 import QtCore, QtGui
import sys
import time
import socket
import thread

HOST = ''  # Endereco IP do Servidor
PORT = 2020 # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
player = ""
placar1 = "0"
placar2 = "0"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Pong(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Pong):
        Pong.setObjectName(_fromUtf8("Pong"))
        Pong.resize(570, 262)
        Pong.setAutoFillBackground(False)
        self.label_5 = QtGui.QLabel(Pong)
        self.label_5.setGeometry(QtCore.QRect(230, 10, 121, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Pong)
        self.label_6.setGeometry(QtCore.QRect(110, 210, 351, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.layoutWidget = QtGui.QWidget(Pong)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 60, 201, 87))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.layoutWidget1 = QtGui.QWidget(Pong)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 170, 541, 35))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter = QtGui.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.splitter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)

        self.retranslateUi(Pong)
        QtCore.QMetaObject.connectSlotsByName(Pong)

    def retranslateUi(self, Pong):
        Pong.setWindowTitle(_translate("Pong", "Pong", None))
        self.label_5.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Placar</span></p></body></html>", None))
        self.label_6.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Preencha os campos acima</span></p></body></html>", None))
        self.label_2.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">0</span></p></body></html>", None))
        self.label_3.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">x</span></p></body></html>", None))
        self.label_4.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">0</span></p></body></html>", None))
        self.label.setText(_translate("Pong", "IP Server:", None))
        self.radioButton.setText(_translate("Pong", "Jogador 1", None))
        self.radioButton.clicked.connect(self.playerSelect1)
        self.radioButton_2.setText(_translate("Pong", "Jogador 2", None))
        self.radioButton_2.clicked.connect(self.playerSelect2)
        self.pushButton.setText(_translate("Pong", "Conectar", None))
        self.pushButton.clicked.connect(self.connectToServer)

    def playerSelect1(self):
        global player
        player = "8"

    def playerSelect2(self):
        global  player
        player = "9"

    def atualizarPlacar(self):
            self.label_2.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">"+ placar1+"</span></p></body></html>", None))
            self.label_4.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">"+ placar2+"</span></p></body></html>", None))

    def connectToServer(self):
        ipServidor = self.lineEdit.text()
        self.label_6.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Conectando ao servidor...</span></p></body></html>", None))
        global HOST
        HOST = ipServidor
        global dest
        dest = (HOST, PORT)
        QtCore.QTimer.singleShot(1000, lambda: self.label_6.setText(_translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Conexão realizada com SUCESSO</span></p></body></html>", None)))
        udp.sendto(player, dest)
        self.setFocus(False)
    
    def receberUDP():
        while True:
            global placar1
            global placar2
            msg = udp.recv(1024)
            mensagem = msg.split()
            print mensagem
            placar1 = mensagem[0]
            placar2 = mensagem[1]

    thread.start_new_thread(receberUDP,())

    def keyPressEvent(self, event):
        self.atualizarPlacar()
        #Posi ++
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Right: 
            if player == "8":
                msg = '1'
                udp.sendto(msg, dest)
            else:
                msg = '3'
                udp.sendto(msg, dest)
        #Posi --
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Left: 
            if player == "8":
                msg = '0'
                udp.sendto(msg, dest)
            else:
                msg = '2'
                udp.sendto(msg, dest)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Pong()
    ex.show()
    sys.exit(app.exec_())
    udp.close()






