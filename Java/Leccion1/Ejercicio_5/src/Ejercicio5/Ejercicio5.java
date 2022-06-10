
package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float nota1, nota2, nota3, sumaTotal;
        System.out.println ("Digite la primer calificacion: ");
        nota1 = Float.parseFloat(entrada.nextLine());

        System.out.println ("Digite la segunda calificacion: ");
        nota2 = Float.parseFloat(entrada.nextLine());
        
        System.out.println ("Digite la tercera calificacion: ");
        nota3 = Float.parseFloat(entrada.nextLine());
        
        sumaTotal = nota1 + nota2 + nota3;
        System.out.println("\nLa suma de las calificaciones es = " + sumaTotal);

    } 
}
