# 2. Sea el siguiente diagrama de clases:
# Implementar las clases y los métodos necesarios para resolver los siguientes problemas:
class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def mostrar_informacion(self):
        return f"Anuncio N°: {self.numero}, Precio: {self.precio}"

class Obra:
    def __init__(self, titulo, material, artista, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artista = artista  
        self.anuncio = anuncio  

    def mostrar_informacion(self):
        info = f"Título: {self.titulo}, Material: {self.material}, Artista: {self.artista.nombre}"
        if self.anuncio:
            info += f", {self.anuncio.mostrar_informacion()}"
        return info

class Artista:
    def __init__(self, nombre, ci, anios_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.anios_experiencia = anios_experiencia

    def mostrar_informacion(self):
        return f"Artista: {self.nombre}, CI: {self.ci}, Años: {self.anios_experiencia}"

class Pintura(Obra):
    def __init__(self, titulo, material, artista, genero, anuncio=None):
        super().__init__(titulo, material, artista, anuncio)
        self.genero = genero

    def incrementar_precio(self, incremento):
        self.anuncio.precio += incremento

#a.Crear dos objetos pintura que tengan anuncios de venta
artista1 = Artista("Pablo Picasso", "114456", 24)
anuncio1 = Anuncio(103, 2500)
pintura1 = Pintura("Guernica", "Óleo", artista1, "Cubismo", anuncio1)
print(pintura1.mostrar_informacion())
# 2. Calcular el promedio de años de experiencia de los artistas de ambas pinturas
artista2 = Artista("Van Gogh", "1134222", 15)
anuncio2 = Anuncio(104, 2450)
pintura2 = Pintura("La noche estrellada", "Óleo", artista2, "Realismo", anuncio2)
pinturas = [pintura1, pintura2]
#b.Calcular el promedio de años Experiencia de los artistas de ambas pinturas
def promedio_años_experiencia(pinturas):
    total_años = sum(p.artista.anios_experiencia for p in pinturas)
    return total_años / len(pinturas)
print("Promedio de años de experiencia:", promedio_años_experiencia(pinturas))
#c.Incrementar el precio en X a la pintura del artista con nombre X
nombre_buscar = "Pablo Picasso"
incremento = 400
for p in pinturas:
    if p.artista.nombre == nombre_buscar:
        p.incrementar_precio(incremento)
        print(f"Nuevo precio de la pintura '{p.titulo}': {p.anuncio.precio}")
for p in pinturas:
    print(p.mostrar_informacion())


