package PRACTICA6;

import java.util.Scanner;

public class AlgebraVectorial {
    private double x;
    private double y;
    private double z;

    // Constructores
    public AlgebraVectorial(double x, double y) {
        this(x, y, 0); // Vector 2D (z=0)
    }
    
    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // Operaciones básicas
    public double productoEscalar(AlgebraVectorial otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }
    
    public AlgebraVectorial productoVectorial(AlgebraVectorial otro) {
        return new AlgebraVectorial(
            this.y * otro.z - this.z * otro.y,
            this.z * otro.x - this.x * otro.z,
            this.x * otro.y - this.y * otro.x
        );
    }
    
    public AlgebraVectorial proyeccion(AlgebraVectorial otro) {
        double denominador = otro.x*otro.x + otro.y*otro.y + otro.z*otro.z;
        if (denominador == 0) return null;
        double factor = this.productoEscalar(otro) / denominador;
        return new AlgebraVectorial(
            factor * otro.x,
            factor * otro.y,
            factor * otro.z
        );
    }
    
    // Getters
    public double getX() { return x; }
    public double getY() { return y; }
    public double getZ() { return z; }
    
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }

    public static void main(String[] args) {
        // Ejemplo 1: a(1,2,3) y b(-2,1,0)
        AlgebraVectorial a1 = new AlgebraVectorial(1, 2, 3);
        AlgebraVectorial b1 = new AlgebraVectorial(-2, 1, 0);
        
        System.out.println("EJEMPLO 1:");
        System.out.println("a = " + a1);
        System.out.println("b = " + b1);
        System.out.println("Producto escalar = " + a1.productoEscalar(b1));
        System.out.println("Producto vectorial = " + a1.productoVectorial(b1));
        System.out.println("Proyección de a sobre b = " + a1.proyeccion(b1));
        
        // Ejemplo 2: a(2,5) y b(4,10)
        AlgebraVectorial a2 = new AlgebraVectorial(2, 5);
        AlgebraVectorial b2 = new AlgebraVectorial(4, 10);
        
        System.out.println("\nEJEMPLO 2:");
        System.out.println("a = " + a2);
        System.out.println("b = " + b2);
        System.out.println("Producto escalar = " + a2.productoEscalar(b2));
        System.out.println("Producto vectorial = " + a2.productoVectorial(b2));
        System.out.println("Proyección de a sobre b = " + a2.proyeccion(b2));
        
        // Interactivo
        Scanner sc = new Scanner(System.in);
        System.out.println("\nINGRESE SUS PROPIOS VECTORES:");
        System.out.println("Vector 1 (x y [z]):");
        AlgebraVectorial v1 = leerVector(sc);
        System.out.println("Vector 2 (x y [z]):");
        AlgebraVectorial v2 = leerVector(sc);
        
        System.out.println("\nRESULTADOS:");
        System.out.println("Producto escalar = " + v1.productoEscalar(v2));
        System.out.println("Producto vectorial = " + v1.productoVectorial(v2));
        System.out.println("Proyección de v1 sobre v2 = " + v1.proyeccion(v2));
        
        sc.close();
    }
    
    private static AlgebraVectorial leerVector(Scanner sc) {
        String[] componentes = sc.nextLine().split(" ");
        if (componentes.length == 2) {
            return new AlgebraVectorial(
                Double.parseDouble(componentes[0]),
                Double.parseDouble(componentes[1])
            );
        } else if (componentes.length == 3) {
            return new AlgebraVectorial(
                Double.parseDouble(componentes[0]),
                Double.parseDouble(componentes[1]),
                Double.parseDouble(componentes[2])
            );
        }
        return new AlgebraVectorial(0, 0, 0);
    }
}
