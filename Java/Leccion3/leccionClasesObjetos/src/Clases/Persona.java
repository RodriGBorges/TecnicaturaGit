// Se Debe importar un paquete
package Clases;

/*

Introduccion a las clases y objetos en Java

                      Persona(Clase)
Una clase es                              Posee atributos
una plantilla                                y metodos

            Karla(Objeto)        Armando(Objeto)
Posee un                                         Un objeto es una
nombre                                           instancia de una clase

*/

// Una clase es nuestra plantilla
// La clase debe ser pública
// Clase Persona (siempre PascalCase para las clases)
public class Persona {
    //Atributos de la clase(Características)
    String nombre;
    String apellido;
    
    //Métodos de la clase (Acciones)
    public void obtenerInformacion(){
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido: " + apellido);
    }
}
