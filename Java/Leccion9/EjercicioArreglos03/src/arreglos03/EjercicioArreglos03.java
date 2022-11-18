
package arreglos03;

import java.util.Scanner;

public class EjercicioArreglos03 {
    public static void main(String[] args) {
        /*
        Ejercicio 3: Leer 5 números por tecladom, guardarlos en un arreglo.
        Realizar la media de los números positivos, negativos y contar el
        número de ceros.
        */
        
        Scanner entrada = new Scanner(System.in);
        
        float numeros[] = new float[5];
        float negativos = 0, positivos = 0, mediaNegativos, mediaPositivos;
        int contadorCeros = 0, contadorNegativos = 0, contadorPositivos = 0;
        
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Ingrese un número: ");
            numeros[i] = entrada.nextFloat();
            
            if (numeros[i] > 0) {
                positivos += numeros[i];
                contadorPositivos++;
            } else if (numeros[i] < 0) {
                negativos += numeros[i];
                contadorNegativos++;
            } else {
                contadorCeros++;
            }
        }
        
        if(contadorPositivos == 0) {
            System.out.println("\n ERROR -> No se ingresaron números positivos para calcular la media.");
        } else {
            mediaPositivos = positivos / contadorPositivos;
            System.out.println("\n La media de los números positivos es = " + mediaPositivos);
        }
        
        if(contadorNegativos == 0) {
            System.out.println("\n ERROR -> No se ingresaron números negativos para calcular la media.");
        } else {
            mediaNegativos = negativos / contadorNegativos;
            System.out.println("\n La media de los números positivos es = " + mediaNegativos);
        }
        
        System.out.println("\nLa cantidad de ceros es: " + contadorCeros);
    }
}
