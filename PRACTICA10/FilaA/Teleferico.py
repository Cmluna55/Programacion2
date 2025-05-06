# Considerando el medio de transporte Mi Teleférico se define la siguiente clase:
class LineaTeleferico:
    def __init__(self, color: str, tramo: str, no_cabinas: int):
        self.color = color
        self.tramo = tramo
        self.no_cabinas = no_cabinas
        self.no_empleados = 0
        self.empleados = [["" for _ in range(3)] for _ in range(100)]
        self.sueldos = [0] * 100
    def agregar_empleado(self, nombre: str, edad: int, sueldo: int) -> bool:
        if self.no_empleados < 100:
            self.empleados[self.no_empleados] = [nombre, str(edad), str(sueldo)]
            self.sueldos[self.no_empleados] = sueldo
            self.no_empleados += 1
            return True
        return False
    def eliminar_empleado(self, patron: str) -> bool:
        for i in range(self.no_empleados):
            if self.empleados[i][0].lower() == patron.lower():
                self.empleados[i] = ["", "", ""]
                self.sueldos[i] = 0
                self.no_empleados -= 1
                # Reorganizar la lista
                for j in range(i, self.no_empleados):
                    self.empleados[j] = self.empleados[j + 1]
                    self.sueldos[j] = self.sueldos[j + 1]
                self.empleados[self.no_empleados] = ["", "", ""]
                self.sueldos[self.no_empleados] = 0
                return True
        return False
    def transferir_empleado(self, origen: 'LineaTeleferico', nombre: str) -> bool:
        for i in range(origen.no_empleados):
            if origen.empleados[i][0].lower() == nombre.lower():
                if self.agregar_empleado(origen.empleados[i][0], int(origen.empleados[i][1]), int(origen.empleados[i][2])):
                    origen.eliminar_empleado(nombre)
                    return True
                return False
        return False
    def mostrar_mayor_edad(self) -> str:
        if self.no_empleados == 0:
            return "No hay empleados"
        max_edad = 0
        nombre_max_edad = ""
        for i in range(self.no_empleados):
            if int(self.empleados[i][1]) > max_edad:
                max_edad = int(self.empleados[i][1])
                nombre_max_edad = self.empleados[i][0]
        return f"Empleado con mayor edad: {nombre_max_edad}, Edad: {max_edad}"
    def mostrar_mayor_sueldo(self) -> str:
        if self.no_empleados == 0:
            return "No hay empleados"
        max_sueldo = 0
        nombre_max_sueldo = ""
        for i in range(self.no_empleados):
            if self.sueldos[i] > max_sueldo:
                max_sueldo = self.sueldos[i]
                nombre_max_sueldo = self.empleados[i][0]
        return f"Empleado con mayor sueldo: {nombre_max_sueldo}, Sueldo: {max_sueldo}"