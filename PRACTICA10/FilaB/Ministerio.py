class Ministerio:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.no_empleados = 0
        self.empleados = [["" for _ in range(3)] for _ in range(100)]  # [nombre, edad, sueldo]
        self.sueldos = [0] * 100
    def agregar_empleado(self, nombre: str, edad: int, sueldo: int) -> bool:
        if self.no_empleados < 100:
            self.empleados[self.no_empleados] = [nombre, str(edad), str(sueldo)]
            self.sueldos[self.no_empleados] = sueldo
            self.no_empleados += 1
            return True
        return False
    def eliminar_empleado(self, nombre: str) -> bool:
        for i in range(self.no_empleados):
            if self.empleados[i][0].lower() == nombre.lower():
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
    def transferir_empleado(self, origen: 'Ministerio', nombre: str) -> bool:
        for i in range(origen.no_empleados):
            if origen.empleados[i][0].lower() == nombre.lower():
                if self.agregar_empleado(origen.empleados[i][0], int(origen.empleados[i][1]), int(origen.empleados[i][2])):
                    origen.eliminar_empleado(nombre)
                    return True
                return False
        return False
    def mostrar_menor_edad(self) -> str:
        if self.no_empleados == 0:
            return "No hay empleados"
        min_edad = float('inf')
        nombre_min_edad = ""
        for i in range(self.no_empleados):
            if int(self.empleados[i][1]) < min_edad:
                min_edad = int(self.empleados[i][1])
                nombre_min_edad = self.empleados[i][0]
        return f"Empleado con menor edad: {nombre_min_edad}, Edad: {min_edad}"
    def mostrar_menor_sueldo(self) -> str:
        if self.no_empleados == 0:
            return "No hay empleados"
        min_sueldo = float('inf')
        nombre_min_sueldo = ""
        for i in range(self.no_empleados):
            if self.sueldos[i] < min_sueldo:
                min_sueldo = self.sueldos[i]
                nombre_min_sueldo = self.empleados[i][0]
        return f"Empleado con menor sueldo: {nombre_min_sueldo}, Sueldo: {min_sueldo}"