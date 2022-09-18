
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        /*
        Ejercicio 4: Pedir números hasta que se teclee uno negativo,
        y mostrar cuántos números se han introducido.
        Lo haremos primero con la clase Scanner
        Luego lo hacemos con la clase JOptionPane
        */
        
        Scanner entrada = new Scanner(System.in);
        
        int numero, conteo = 0;
        
        System.out.println("Ingrese un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero >= 0) {
            System.out.println("El número " + numero + " es POSITIVO");
            conteo ++;
            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado " + conteo + " números que NO son negativos");
    }
}
