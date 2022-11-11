
package domain;

public class Empleado extends Persona {
    @Override //Sobreescribimos el método de la clase padre
    public void imprimir() {
        System.out.println("Método imprimir desde clase hija");
    }
}
