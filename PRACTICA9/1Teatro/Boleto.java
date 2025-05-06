public abstract class Boleto {
    protected int numero;
    protected double precio;

    public Boleto(int numero, double precio) {
        this.numero = numero;
        this.precio = precio;
    }

    public int getNumero() {
        return numero;
    }

    public double getPrecio() {
        return precio;
    }

    public abstract String mostrarInfo();
}