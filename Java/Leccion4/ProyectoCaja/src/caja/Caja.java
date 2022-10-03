
package caja;

public class Caja {

    int ancho;
    int alto;
    int profundidad;
    
    public Caja() {
        
    }
    // Si necesitamos un constructor para recibir argumentos es necesario tener
    // otro vacío
    public Caja(int ancho, int alto, int profundidad){
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    public int calcularVolumen() {
        return ancho * alto * profundidad;
    }
    
}
