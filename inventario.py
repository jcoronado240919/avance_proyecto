class Inventario:
    def __init__(self, stock, producto, valor):
        self.stock = stock 
        self.producto = producto
        self.valor = valor
        
    #metodos accesadores
    def get_stock(self):
        return self.stock

    def get_producto(self):
        return self.producto  
    
    def get_valor(self):
        return self.valor
    
   #metodos mutadores
    def set_stock(self, nuevo_stock):
        self.modelo = nuevo_stock 

    def set_producto(self, nuevo_producto):
        self.patente = nuevo_producto

    def set_valor(self, nuevo_valor):
        self.valor = nuevo_valor



