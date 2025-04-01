class Pila:
    def _init_(self, n):
        self.arreglo = [0] * n  
        self.top = -1           
        self.n = n              

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.arreglo[self.top] = e
            print(f'Elemento {e} añadido a la pila.')  
        else:
            raise Exception("Pila llena")

    def pop(self):
        if not self.isEmpty():
            elemento = self.arreglo[self.top]
            self.top -= 1
            print(f'Elemento {elemento} eliminado de la pila.')  
            return elemento
        else:
            raise Exception("Pila vacía")

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.top]
        else:
            raise Exception("Pila vacía")

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

if __name__ == "_main_":
    print("Ejecutando el programa...")
    pila = Pila(5)  
    pila.push(10)
    pila.push(20)
    print(f'Elemento en la cima: {pila.peek()}')  
    print(f'Elemento retirado: {pila.pop()}')      
    print(f'¿Está la pila vacía? {pila.isEmpty()}') 