// Paso por referencia
package pasoporreferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        //utilizamos la memoria heap
        Persona persona1 = new Persona();
        persona1.nombre = "Ester"; // Hay que establecer a nombre como public para poder utilizarla aquí
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: " + persona1.nombre);
        
        persona1 = cambiarElValor(persona1);
        
        
        // Persona persona2 = null;
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevovalor del objeto es: " + persona2.nombre);
    }
    
    // void viene con return implícito
    public static void cambiarValor(Persona persona){ //parámetro por referencia
        persona.nombre = "María";
    }
    
    public static Persona cambiarElValor(Persona persona){
        if(persona == null) {
            System.out.println("Valor de persona es inválido : Null");
            return null;
        } else {
            persona.nombre = "Monica";
            return persona;
        }
        
    }
}
