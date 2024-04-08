class Vehiculo:
    def __init__(self, modelo, patente, diagnostico,fecha):
        self.modelo = modelo 
        self.patente = patente
        self.diagnostico = diagnostico
        self.fecha = fecha

    #metodos accesadores
    def get_modelo(self):
        return self.modelo

    def get_patente(self):
        return self.patente  
    
    def get_diagnostico(self):
        return self.diagnostico
    
    def get_fecha(self):
        return self.fecha

    #metodos mutadores
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo 

    def set_patente(self, nuevo_patente):
        self.patente = nuevo_patente 

    def set_diagnostico(self, nuevo_diagnostico):
        self.diagnostico = nuevo_diagnostico

    def set_fecha(self, nuevo_fecha):
        self.fecha = nuevo_fecha


