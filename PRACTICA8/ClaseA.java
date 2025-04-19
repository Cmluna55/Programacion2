package PRACTICA8;
//Practica 8
//Realizar la codificación en Python y en Java del siguiente diagrama de clases:

public class ClaseA {
    public int x;
    public int z;
    
    public ClaseA(int x, int z) {
        this.x = x;
        this.z = z;
    }
    
    public void incrementaXZ() {
        x++;
        z++;
    }
    
    public void incrementaZ() {
        z++;
    } 
     // Getters para x y z
     public int getX() {
        return x;
    }

    public int getZ() {
        return z;
    }             
}
