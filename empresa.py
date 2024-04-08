class Empresa:
    def __init__(self, nombre, rut, direccion):
        self.nombre = nombre 
        self.rut = rut
        self.direccion = direccion

    
        
 #metodos accesadores
    def get_nombre(self):
        return self.nombre
    
    def get_rut(self):
        return self.rut 
    
    def get_direccion(self):
        return self.direccion
    
    

    
   #metodos mutadores
    def set_nombre(self, nuevo_nombre):
        self.modelo = nuevo_nombre

    def set_rut(self, nuevo_rut):
        self.patente = nuevo_rut

    def set_direccion(self, nuevo_direccion):
        self.valor = nuevo_direccion






