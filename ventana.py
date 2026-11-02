from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ventana import Ui_MainWindow  # Importa la clase generada desde ventana.py
from insumo import Insumo          # Importa la clase Insumo

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 1. Conectar los botones a sus métodos correspondientes
        self.pushButton_aceptar.clicked.connect(self.agregar_insumo)
        self.pushButton_eliminar.clicked.connect(self.eliminar_insumo)

    def agregar_insumo(self):
        try:
            # Obtener y convertir los valores de la interfaz
            codigo = self.lineEdit_codigo.text()
            descripcion = self.lineEdit_descripcion.text()
            cantidad = int(self.lineEdit_cantidad.text())  # Puede lanzar ValueError si está vacío o no es entero
            precio = float(self.lineEdit_precio.text())      # Puede lanzar ValueError si está vacío o no es número
            
            # Crear el objeto Insumo (validará las reglas dentro de la clase)[cite: 7]
            insumo = Insumo(codigo, descripcion, cantidad, precio)
            
            # Si se crea correctamente, mostrar mensaje de éxito y limpiar campos
            QMessageBox.information(self, "Éxito", f"El insumo {insumo.get_descripcion()} fue ingresado al sistema")
            self.limpiar_campos()
            
        except ValueError as e:
            # Si ocurre un error de conversión o la clase lanza ValueError, se muestra con QMessageBox.warning
            mensaje = str(e) if str(e) else "Error en los datos ingresados. Verifique que la cantidad y el precio sean válidos."
            QMessageBox.warning(self, "Advertencia", mensaje)

    def eliminar_insumo(self):
        codigo = self.lineEdit_codigo.text()
        
        # Verificar si el código no está vacío
        if codigo.strip() != "":
            QMessageBox.information(self, "Eliminado", f"El insumo con código {codigo} fue eliminado del sistema")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Advertencia", "El campo código no puede estar vacío para eliminar.")

    def limpiar_campos(self):
        # Método auxiliar para limpiar los LineEdit
        self.lineEdit_codigo.clear()
        self.lineEdit_descripcion.clear()
        self.lineEdit_cantidad.clear()
        self.lineEdit_precio.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainApp()
    ventana.show()
    sys.exit(app.exec_())