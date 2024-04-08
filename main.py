from auto import Vehiculo
from inventario import Inventario
from empresa import Empresa 
from trabajos import Trabajo_1


auto_1 = Vehiculo("Kia", "FB3040", "Lavado Exterior", "25.10.2024")
auto_2 = Vehiculo("Toyota", "ZD0101", "Lavado Tapiceria", "12.12.2024")

producto_1 = Inventario("10", "Detergente", "15000")

empresa = Empresa("Auto SPA","71.653.545-8", "Santa Julia 675")

Trabajos1 = Trabajo_1 ("Kia","FB3040","Lavado Exterior", "15000")

# Datos Empresas
print("Datos Empresa.......\n")

nombre = empresa.get_nombre()
print("Nombre Empresa:", nombre)

rut = empresa.get_rut()
print("Rut Empresa:", rut)

direccion = empresa.get_direccion()
print("Direccion Empresa:", direccion)




# Datos Auto 1
print ("Auto 1 Ingresado.............\n")

modelo_auto1 = auto_1.get_modelo()
print("Modelo de auto 1:", modelo_auto1)

patente_auto1 = auto_1.get_patente()
print("Patente de auto 1:", patente_auto1)

diagnostico_auto1 = auto_1.get_diagnostico()
print("Diagnóstico de auto 1:", diagnostico_auto1)

fecha_auto1 = auto_1.get_fecha()
print("Fecha de Ingreso 1:", fecha_auto1)


# Datos Auto 2
print ("Auto 2 Ingresado..........\n")

modelo_auto2 = auto_2.get_modelo()
print("Modelo de auto 2:", modelo_auto2)

patente_auto2 = auto_2.get_patente()
print("Patente de auto 2:", patente_auto2)

diagnostico_auto2 = auto_2.get_diagnostico()
print("Diagnóstico de auto 2:", diagnostico_auto2)

fecha_auto2 = auto_2.get_fecha()
print("Fecha de Ingreso 2:", fecha_auto2)


# inventario

print("---------------------------")

print("Inventario de Insumos Operacionales\n")

stock = producto_1.get_stock()
print("Cantidad Stock:", stock)

producto = producto_1.get_producto()
print("Cantidad Stock:", producto)

valor = producto_1.get_valor()
print("Cantidad Stock:", valor)


# Costos

print("--------------------------------")
print("Boleta de Trabajo........")

modelo = Trabajos1.get_modelo()
print("Modelo del Auto:", modelo)

patente = Trabajos1.get_patente()
print("Patente del Auto:", patente)

diagnostico = Trabajos1.get_diagnostico()
print("Diagnistico del Auto",diagnostico)

costos = Trabajos1.get_costos()
print("El costo del Trabajo es", costos)




