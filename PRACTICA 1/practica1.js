public class Punto {
    float x, y;

    Punto(float a, float b) {
        x = a;
        y = b;
    }

    float[] coord_cartesianas() {
        return new float[]{x, y};
    }

    double[] coord_polares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan2(y, x);
        return new double[]{r, theta};
    }

    public String toString() {
        return "Punto(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);

        System.out.println("Coordenadas cartesianas: (" + p.coord_cartesianas()[0] + ", " + p.coord_cartesianas()[1] + ")");

        double[] polares = p.coord_polares();
        System.out.println("Coordenadas polares: (r=" + polares[0] + ", θ=" + polares[1] + ")");

        System.out.println("Representación del punto: " + p);
    }
}