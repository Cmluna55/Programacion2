class Cola:
    def _init_(self, n):
        self.arreglo = [0] * n  
        self.inicio = 0          
        self.fin = 0             
        self.n = n               
        self.size = 0            

    def insert(self, e):
        if not self.isFull():
            self.arreglo[self.fin] = e
            self.fin = (self.fin + 1) % self.n
            self.size += 1
            print(f'Elemento {e} añadido a la cola.')
        else:
            raise Exception("Cola llena")

    def remove(self):
        if not self.isEmpty():
            elemento = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n
            self.size -= 1
            print(f'Elemento {elemento} eliminado de la cola.')
            return elemento
        else:
            raise Exception("Cola vacía")

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        else:
            raise Exception("Cola vacía")

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.n

    def size(self):
        return self.size

if __name__ == "_main_":
    cola = Cola(3)  
    cola.insert(5)
    cola.insert(6)
    print(f'Elemento en la cabeza: {cola.peek()}')  
    print(f'Elemento retirado: {cola.remove()}')    
    print(f'¿Está la cola vacía? {cola.isEmpty()}')  