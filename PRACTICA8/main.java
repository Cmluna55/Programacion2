package PRACTICA8;
//Practica 8
public class main {
    public static void main(String[] args) {

        ClaseD d = new ClaseD(1, 2, 3);
        
        System.out.println("Valores iniciales:");
        System.out.println("A.x: " + d.getAX());
        System.out.println("A.z: " + d.getAZ());
        System.out.println("B.y: " + d.getBY());
        System.out.println("B.z: " + d.getBZ());

        d.incrementaXZ();
        System.out.println("--------------------------------");
        System.out.println("Valores después de incrementaXZ:");
        System.out.println("A.x: " + d.getAX());
        System.out.println("A.z: " + d.getAZ());
        System.out.println("B.y: " + d.getBY());
        System.out.println("B.z: " + d.getBZ());
    }
}