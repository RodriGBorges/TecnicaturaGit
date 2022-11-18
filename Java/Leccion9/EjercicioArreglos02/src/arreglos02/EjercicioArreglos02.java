
package arreglos02;

import java.util.Scanner;

public class EjercicioArreglos02 {
    public static void main(String[] args) {
        
        /*
        Ejercicio 2: Leer 5 números, guardarlos en un arreglo y mostrarlos
        en el orden inverso.
        */
        
        Scanner entrada = new Scanner(System.in);
        
        float numeros[] = new float[5];
        
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Ingrese un número: ");
            numeros[i] = entrada.nextFloat();
        }
        
        System.out.println("\n Elementos del arreglo: ");
        for (int i = 4; i >= 0; i--) {
            System.out.println((i+1) + " " + numeros[i]);
        }
        System.out.println("\n");
    }
}
