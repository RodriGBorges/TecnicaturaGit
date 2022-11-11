
package domain;

public class Persona {
    
    /* Con final da error
    public final void imprimir() {
        System.out.println("Método para imprimir");
    }
    */
    public void imprimir() {
        System.out.println("Método para imprimir");
    }
    
    // Se recomienda establecer constantes en mayúsculas
    public final static int CONSTATNE_AQUI = 15;
    
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
}
