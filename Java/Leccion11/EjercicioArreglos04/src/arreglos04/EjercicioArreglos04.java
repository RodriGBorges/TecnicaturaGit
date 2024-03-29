/*
    Ejercicio 4: Leer 10 números enteros, guardarlos en un arreglo.
    Debemos mostrarlos en el siguiente orden: el primero.
    el último, el segundo, el penúltimo, el tercero, etc.
 */
package arreglos04;

import java.util.Scanner;

public class EjercicioArreglos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int[10];
        
        for(int i = 0; i < 10; i++) {
            System.out.print((i + 1) + ". Digite un número: ");
            numeros[i] = entrada.nextInt();
        }
        
        System.out.println("El resultado es: ");
        for(int i = 0; i < 5; i++) {
            System.out.println(numeros[i] + " "); //Primero, segundo
            System.out.println(numeros[9 - i] + " "); //Ultimo, penultimo
        }
        
        System.out.println(); //Salto de linea
        
    }
}