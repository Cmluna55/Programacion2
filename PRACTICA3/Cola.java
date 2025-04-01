public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int size;

    public Cola(int n) {
        this.n = n;
        arreglo = new long[n]; 
        inicio = 0;            
        fin = 0;               
        size = 0;              
    }

    public void insert(long e) throws Exception {
        if (!isFull()) {
            arreglo[fin] = e;
            fin = (fin + 1) % n;
            size++;
            System.out.println("Elemento " + e + " añadido a la cola.");
        } else {
            throw new Exception("Cola llena");
        }
    }

    public long remove() throws Exception {
        if (!isEmpty()) {
            long elemento = arreglo[inicio];
            inicio = (inicio + 1) % n;
            size--;
            System.out.println("Elemento " + elemento + " eliminado de la cola.");
            return elemento;
        } else {
            throw new Exception("Cola vacía");
        }
    }

    public long peek() throws Exception {
        if (!isEmpty()) {
            return arreglo[inicio];
        } else {
            throw new Exception("Cola vacía");
        }
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == n;
    }

    public int size() {
        return size;
    }

    public static void main(String[] args) {
        try {
            Cola cola = new Cola(5);
            cola.insert(9);
            cola.insert(11);
            System.out.println("-----------------"); 
            System.out.println("Elemento en la cabeza: " + cola.peek()); 
            System.out.println("Elemento retirado: " + cola.remove());
            System.out.println("-----------------");   
            System.out.println("¿Está la cola vacía? " + cola.isEmpty()); 
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
