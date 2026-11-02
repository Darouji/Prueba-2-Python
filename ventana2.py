# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1143, 857)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(80, 30, 831, 661))
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 120, 641, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 160, 631, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 200, 641, 26))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 240, 661, 26))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 280, 81, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 280, 81, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 120, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 160, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 200, 49, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 49, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 90, 131, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # --- CONEXIÓN DE BOTONES ---
        self.pushButton.clicked.connect(self.accion_aceptar)
        self.pushButton_2.clicked.connect(self.accion_eliminar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Aceptar"))
        self.pushButton_2.setText(_translate("Dialog", "Eliminar"))
        self.label.setText(_translate("Dialog", "Codigo"))
        self.label_2.setText(_translate("Dialog", "Descripcion"))
        self.label_3.setText(_translate("Dialog", "Cantidad"))
        self.label_4.setText(_translate("Dialog", "Precio"))
        self.label_5.setText(_translate("Dialog", "Registros de insumos "))

    # --- FUNCIONES DE LOS BOTONES ---
    def accion_aceptar(self):
        codigo = self.lineEdit.text()
        descripcion = self.lineEdit_2.text()
        cantidad = self.lineEdit_3.text()
        precio = self.lineEdit_4.text()
        
        print(f"Código: {codigo} | Descripción: {descripcion} | Cantidad: {cantidad} | Precio: {precio}")
        # Aquí puedes agregar la lógica para guardar en base de datos o mostrar un mensaje
        QtWidgets.QMessageBox.information(None, "Éxito", "Datos registrados correctamente.")

    def accion_eliminar(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())