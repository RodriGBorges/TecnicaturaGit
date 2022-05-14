
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    // psvm + tab
    public static void main(String[] args) {
        
        // Ejercicio Tienda de Libros
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro");
        System.out.println("");
        
        System.out.println("Digite el nombre del libro");
        var nombre = entrada.nextLine();
        
        System.out.println("Digite el ID del libro");
        var libroId = entrada.nextLine();
        
        System.out.println("Digite el precio del libro");
        var precio = entrada.nextLine();
        
        System.out.println("Indicar si el envío es gratuito (True/False)");
        var envio = entrada.nextLine();
        
        System.out.println("Nombre: " + nombre);
        System.out.println("ID: " + libroId);
        System.out.println("Precio: $" + precio);
        System.out.println("Envío Gratuito?: " + envio);
        
        
    }
}
