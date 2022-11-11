/*
 Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:

* Variables: Evita cambiar el valor que almacena la variable
* Métodos: Evita que se modifique la definición o el comportamiento
    de un método desde una subclase (hija)
* Clases: Evita que se creen clases hijas

Otra característica es que normalmente, cuando trabajamos con variables se
combina con el modificador de acceso estático para convertir una variable
en una constante, es decir que no se puede modificar su valor, el ejemplo 
de esto es la clase Math en la cual todos sus atributos son de tipo static 
y final, es por esto que la variable Pi*(3.14) se conoce como una constante.
 */
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        
        final int miDni = 12345234;
        System.out.println("miDni = " + miDni);
        
        //miDni = 20234234; No se puede modificar esta constante
        
        //Persona.CONSTATNE_AQUI = 9; //No se puede modificar la constante
        System.out.println("Mi atrubuto constante es: " + Persona.CONSTATNE_AQUI);
        
        final Persona persona1 = new Persona(); //El constructor se genera autom. aunque no lo veamos
        //persona1 = new Persona(); 
        //No se puede modificar una nueva referencia
        
        //Pero si se puede modificar el valor de un atributo
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre: = " + persona1.getNombre());
        
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: = " + persona1.getNombre());
    }
}
