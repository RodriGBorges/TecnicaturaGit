/*
    Ejercicio 13: Leer 10 enteros en una tabla. Guardar en otra tabla los
    elementos pares de la primera, y a continuación los elementos impares.
 */
package arreglos13;

import java.util.Scanner;

public class EjercicioArreglos13 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        int conteoPares = 0, conteoImpares = 0;
        
        System.out.println("Llenar arreglo: ");
        for(int i = 0; i < 10; i++) {
            System.out.print((i + 1) + ". Digite un número: ");
            arreglo[i] = entrada.nextInt();
            
            if(arreglo[i] % 2 == 0 ) {
                //contamos para crear los arreglos
                conteoPares++;
            } else {
                conteoImpares++;
            }
        }
        
        //Creamos los arreglos pares e impares
        int par[] = new int[conteoPares];
        int impar[] = new int[conteoImpares];
        
        //Los usamos como iteradores
        conteoPares = 0;
        conteoImpares = 0;
        
        for(int i = 0; i < 10; i++) {
            if(arreglo[i] % 2 == 0) {
                par[conteoPares] = arreglo[i];
                conteoPares++;
            } else {
                impar[conteoImpares] = arreglo[i];
                conteoImpares++;
            }
        }
        
        System.out.print("\nArreglo ingresado: ");
        for(int i = 0; i < 10; i++) {
            System.out.print(arreglo[i] + " - ");
        }
        
        System.out.print("\nArreglo pares: ");
        for(int i = 0; i < conteoPares; i++) {
            System.out.print(par[i] + " - ");
        }
        
        System.out.print("\nArreglo impares: ");
        for(int i = 0; i < conteoImpares; i++) {
            System.out.print(impar[i] + " - ");
        }
        System.out.println();
    }
}
