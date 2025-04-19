package PRACTICA8;

public class ClaseD {
    private ClaseA a;
    private ClaseB b;

    public ClaseD(int x, int z, int y) {
        this.a = new ClaseA(x, z);
        this.b = new ClaseB(y, z);
    }

    public void incrementaXZ() {
        a.incrementaXZ();
        b.incrementaZ(); // Esto afectará a z de B
    }
     // Getters para acceder a los valores de A y B
    public int getAX() {
        return a.getX();
    }

    public int getAZ() {
        return a.getZ();
    }

    public int getBY() {
        return b.getY();
    }

    public int getBZ() {
        return b.getZ();
    }
}
