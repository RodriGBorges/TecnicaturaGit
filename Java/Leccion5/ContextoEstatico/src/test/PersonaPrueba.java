
package test;

import domain.Persona;

public class PersonaPrueba {
    
    private int contador;
    
    // public -> modificador de acceso público
    // static -> modificador de acceso estático, el compilador no va a crear
    // un objeto de la clase para ejecutar la prueba
    // void -> no devuelve nada
    public static void main(String[] args) {
        
        Persona persona1 = new Persona("Ariel");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Naty");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        
        // this.contador = 10; // No se puede referenciar desde un contexto estatico
        // Para solucionarlo se crea un método getcontador
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }
    
    public static void imprimir(Persona persona) {
        System.out.println("persona = " + persona);
    }
    
    public int getContador() {
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}
