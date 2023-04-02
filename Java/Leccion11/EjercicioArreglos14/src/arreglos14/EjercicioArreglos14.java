/*
    Ejercicio 14: Leer dos series de 10 enteros, que estarán ordenados crecientemente.
    Copiar (fusionar) las dostablas en una tercera, de forma que sigan ordenados.
 */
package arreglos14;

import java.util.Scanner;

public class EjercicioArreglos14 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int a[] = new int[10];
        int b[] = new int[10];
        int c[] = new int[20];
        boolean creciente = true;
        
        System.out.println("Llenar el primer arreglo: ");
        do {
            for(int i = 0; i < 10; i++) {
                System.out.print((i + 1) + ". Digite un número: ");
                a[i] = entrada.nextInt();
            }
            
            //Comprobamos si el arreglo esta ordenado
            for(int i = 0; i < 9; i++) {
                if(a[i] < a[i + 1]) {
                    //Creciente 1-2-3
                    creciente = true;
                }
                if(a[i] > a[i + 1]) {
                    //Decreciente 3-2-1
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false) {
                System.out.println("\nEl arreglo está desordenado, vuelva a digitar: ");
            }
            
        } while(creciente == false);
        
        System.out.println("Llenar el segundo arreglo: ");
        do {
            for(int i = 0; i < 10; i++) {
                System.out.print((i + 1) + ". Digite un número: ");
                b[i] = entrada.nextInt();
            }
            
            for(int i = 0; i < 9; i++) {
                if(b[i] < b[i + 1]) {
                    creciente = true;
                }
                
                if(b[i] > b[i + 1]) {
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false) {
                System.out.println("\nEl arreglo está desordenado, vuelva a digitar: ");
            }
        }while(creciente == false);
        
        int i = 0; //Iterador i para el arreglo a
        int j = 0; //Iterador j para el arreglo b
        int k = 0; //Iterador k para el arreglo c
        
        while(i < 10 && j < 10) {
            if(a[i] < b[j]) { //Si el elemento de A es menor que B
                c[k] = a[i]; //Copiamos el elemento de A
                i++; //Avanzamos una posicion en A
            } else {
                c[k] = b[j]; //Copiamos el elemento de B
                j++; //Avanzamos una posicion mas en B
            }
            k++; //Avanzamos una posicion mas en C
        }
        
        //Cuando salimos del while es porque un arreglo (a o b), se ha copiado completamente
        if(i == 10) { //Significa que ya copiamos todo el arreglo A, falta el B
            while(j < 10) { //Mientras el iterador sea menor a 10
                c[k] = b[j]; //Copiamos el elemento de B en C
                j++; //Avanzamos una posicion en B
                k++; //Avanzamos una posicion en C
            }
        } else { //Significa que ya copiamos todo el arreglo B, falta el A
            while(i < 10) {
                c[k] = a[i];
                i++;
                k++;
            }
        }
        
        System.out.println("\nEl arreglo C completo es: ");
        for(k = 0; k < 20; k++) {
            System.out.print(c[k] + " - ");
        }
        System.out.println();
    }
}
