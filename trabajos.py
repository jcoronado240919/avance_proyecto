class Trabajo_1:
    def __init__(self, modelo, patente, diagnostico,costos):
        self.modeloauto = modelo 
        self.patente = patente
        self.diagnostico = diagnostico
        self.costos = costos


#metodos accesadores
    def get_modelo(self):
        return self.modeloauto

    def get_patente(self):
        return self.patente  
    
    def get_diagnostico(self):
        return self.diagnostico
    
    def get_costos(self):
        return self.costos

    #metodos mutadores
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo 

    def set_patente(self, nuevo_patente):
        self.patente = nuevo_patente 

    def set_diagnostico(self, nuevo_diagnostico):
        self.diagnostico = nuevo_diagnostico

    def set_costos(self, nuevo_costos):
        self.fecha = nuevo_costos


