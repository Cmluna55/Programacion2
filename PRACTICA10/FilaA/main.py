# Considerando el medio de transporte Mi Teleférico se define la siguiente clase: 

from Teleferico import LineaTeleferico
# a)
linea1 = LineaTeleferico("Rojo", "Estacion Central, Estacion Cementerio, Estacion 16 de Julio", 20)
linea2 = LineaTeleferico("Verde", "Estacion Luna, Estacion 16 de Julio", 15)

empleados = [
    ("Pedro", 35, 3250),
    ("Rojas", 43, 3250),
    ("Lucy", 43, 3250),
    ("Ana", 26, 2700),
    ("Sosa", 26, 2700),
    ("Saul", 29, 2500),
    ("Arce", 29, 2500),
    ("Calle", 29, 2500)
]
for nombre, edad, sueldo in empleados:
    linea1.agregar_empleado(nombre, edad, sueldo)
# b)
linea1.eliminar_empleado("Rojas")
# c)
linea1.transferir_empleado(linea2, "Pedro")
# d)
print(linea1.mostrar_mayor_edad())
print(linea1.mostrar_mayor_sueldo())
print(linea2.mostrar_mayor_edad())
print(linea2.mostrar_mayor_sueldo())