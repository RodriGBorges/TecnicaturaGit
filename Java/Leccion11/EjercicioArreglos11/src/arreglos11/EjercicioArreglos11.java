/*
    Ejercicio 11: Leer 5 elementos numéricos que se introduciran ordenados
    de forma creciente. Éstos los guardaremos en una tabla de tamaño 10.
    Leer un número N, e insertarlo en el lugar adecuado para que la tabla
    continúe ordenada.
 */
package arreglos11;

import java.util.Scanner;

public class EjercicioArreglos11 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        boolean creciente = true;
        int numero, sitioNum = 0, j = 0;
        
        System.out.println("Llenar el arreglo: ");
        do {
            //llenando el arreglo
            for(int i = 0; i < 5; i++) {
                System.out.print((i + 1) + ". Digite un número: ");
                arreglo[i] = entrada.nextInt();
            }
            
            //Comprobar si el arreglo esta ordenado en orden creciente
            for(int i = 0; i < 4; i++) {
                if(arreglo[i] < arreglo[i + 1]) { //Creciente 1, 2, 3...
                    creciente = true;
                }
                if(arreglo[i] > arreglo[i + 1]) {
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false) {
                System.out.println("\nEl arreglo no esta ordenado en forma creciente, vuelva a digitar\n");
            }
        } while(creciente == false);
        
        System.out.println("Digite un número a insertar: ");
        numero = entrada.nextInt();
        
        //Esto es para darnos cuenta en que posición va el número
        while(arreglo[j] < numero && j < 5) {
            sitioNum++;
            j++;
        }
        
        //Por último, trasladamos una posición en el arreglo a los elementos que van detras de número
        for(int i = 4; i >= sitioNum; i--) {
            arreglo[i + 1] = arreglo[i];
        }
        
        //Insertamos el número
        arreglo[sitioNum] = numero;
        
        System.out.println("\nEl arreglo queda: ");
        for(int i = 0; i < 6; i++) {
            System.out.print(arreglo[i] + " - ");
        }
        System.out.println("");
    }
}
