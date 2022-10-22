
package test;

// Con este asterisco importamos todas las clases dentro del paquete dominio
// import dominio.*;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000.0, false);
        System.out.println("persona1: " + persona1);
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        //Ya no se puede utilizar por el encapsulamiento
        //persona1.nombre = "Juan Ignacio"; 
        //System.out.println("Nombre es: " + persona1.nombre);
        
        //Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        //Crear otro objeto de tipo persona, asignar valores de manera inicial e imprimir
        //luego modificar sus valores y volver a imprimir
        
        //No hace falta llamar al toString(), viene incluido en persona10
        System.out.println("persona1: " + persona1);
    }
}
