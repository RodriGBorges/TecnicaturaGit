
package arreglos01;

import java.util.Scanner;

public class EjercicioArreglos01 {
    public static void main(String[] args) {
        
        /*
        Ejercicio 1: Leer 5 números, guardarlos en un arreglo y mostrarlos
        en el mismo orden introducidos.
        */
        
        Scanner entrada = new Scanner(System.in);
        
        float[] arreglos = new float[5];
        
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Ingrese un número: ");
            arreglos[i] = entrada.nextFloat();
        }
        
        System.out.println("\n Imprimir los elementos del arreglo");
        for(float i : arreglos) {
            System.out.println(i + " ");
        }
        
        System.out.println("\n");
    }
}
