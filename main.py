import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

# Importa tu archivo generado (reemplaza 'ventana2' por el nombre real de tu archivo .py)
from ventana2 import Ui_MainWindow 

class MiVentana(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        
        self.pushButton.clicked.connect(self.accion_aceptar)
        
        # Conectamos el botón Eliminar con otro método personalizado
        self.pushButton_2.clicked.connect(self.accion_eliminar)

    def accion_aceptar(self):
        # Código que se ejecuta al hacer clic en "Aceptar"
        codigo = self.lineEdit.text() # Cambia 'lineEdit' por el nombre real de tu campo de código
        QMessageBox.information(self, "Aceptar", f"Botón Aceptar presionado. Código ingresado: {codigo}")

    def accion_eliminar(self):
        # Código que se ejecuta al hacer clic en "Eliminar"
        QMessageBox.warning(self, "Eliminar", "Botón Eliminar presionado.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())