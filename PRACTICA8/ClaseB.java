package PRACTICA8;

public class ClaseB {
    public int y;
    public int z;

    public ClaseB(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
    // Getters para y y z
    public int getY() {
        return y;
    }

    public int getZ() {
        return z;
    }
}