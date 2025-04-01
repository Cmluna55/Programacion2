public class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        arreglo = new long[n]; 
        top = -1;              
    }

    public void push(long e) throws Exception {
        if (!isFull()) {
            top++;
            arreglo[top] = e;
        } else {
            throw new Exception("Pila llena");
        }
    }

    public long pop() throws Exception {
        if (!isEmpty()) {
            long elemento = arreglo[top];
            top--;
            return elemento;
        } else {
            throw new Exception("Pila vacía");
        }
    }

    public long peek() throws Exception {
        if (!isEmpty()) {
            return arreglo[top];
        } else {
            throw new Exception("Pila vacía");
        }
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args) {
        try {
            Pila pila = new Pila(5);
            pila.push(10);
            pila.push(20);
            System.out.println("-----------------");
            System.out.println(pila.peek()); 
            System.out.println(pila.pop());   
            System.out.println(pila.isEmpty()); 
        } catch (Exception e) {
            System.out.println("-----------------");
            System.out.println(e.getMessage());
        }
    }
}