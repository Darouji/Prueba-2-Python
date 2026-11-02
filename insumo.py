class Insumo:
    def __init__(self, codigo, descripcion, cantidad, precio):
        
        if cantidad < 1:
            raise ValueError("La cantidad debe ser mayor o igual a 1.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
            
        
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__precio = precio

    
    def get_codigo(self):
        return self.__codigo

    def get_descripcion(self):
        return self.__descripcion

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def resumen(self):
        return f"Código: {self.__codigo}, Descripción: {self.__descripcion}, Cantidad: {self.__cantidad}, Precio: {self.__precio}"