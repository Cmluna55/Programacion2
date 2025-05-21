#camila milenka luna cruz
# 1. Sea el siguiente diagrama de clases:
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
        return f"Artista: {self.nombre}, CI: {self.ci}, Años de experiencia: {self.anios_experiencia}"

class Pintura(Obra):
    def __init__(self, titulo, material, artista, genero, anuncio=None):
        super().__init__(titulo, material, artista, anuncio)
        self.genero = genero 

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f", Género: {self.genero}"
        return info

#b.Mostrar el nombre del artista con más años de Experiencia de ambas pinturas
def artista_mas_experiencia(pinturas):
    if not pinturas:
        return None
    return max(pinturas, key=lambda p: p.artista.anios_experiencia).artista

#c.Se ha decidido vender la pintura sin anuncio, se pide agregar un anuncio de venta
#y determine el monto total de venta de ambas pinturas.
def total_ventas(pinturas):
    total = 0
    for p in pinturas:
        if p.anuncio:
            total += p.anuncio.precio
    return total

#a.Crear un objeto pintura que tenga un anuncio y otro objeto pintura sin anuncio.
if __name__ == "__main__":
    #Anuncios
    anuncio1 = Anuncio(101, 2200)
    anuncio2 = Anuncio(102, 1800)
    #Artistas
    artista1 = Artista("Pablo Picasso", "66634", 25)
    artista2 = Artista("Van Gogh", "113896", 20)

    #Géneros
    genero1 = "Cubismo"
    genero2 = "Postimpresionismo"

    #Pinturas
    pintura1 = Pintura("Guernica", "Óleo", artista1, genero1, anuncio1)
    pintura2 = Pintura("Orejas cortadas", "Acrilico", artista2, genero2, anuncio2)
    pinturas = [pintura1, pintura2]
    print(f"-----------------------------------------------")
    print(pintura1.mostrar_informacion())
    print(pintura2.mostrar_informacion())
    print(f"-----------------------------------------------")
    artista_lider = artista_mas_experiencia(pinturas)
    print(f"El artista con más años de experiencia es: {artista_lider.mostrar_informacion()}")
    print(f"-----------------------------------------------")
    print(f"El total de ventas de pinturas es: {total_ventas(pinturas)}")

