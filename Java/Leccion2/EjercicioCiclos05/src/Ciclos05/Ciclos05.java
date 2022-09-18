 
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        /*
        Ejercicio 5: Realizar un juego para adivinar un número,
        para ello generar un número aleatorio entre 0-100, y luego ir pidiendo
        números indicando "es mayor" o "es menor" según sea mayor o menos con 
        respecto a N.
        El proceso termina cuando el usuario acierta y mostramos el número
        de intentos hechos
        */
        
        Scanner entrada = new Scanner(System.in);
        int numero, random, intentos = 0;
        
        random = (int)Math.floor(Math.random() * 100); //Genera un número aleatorio de 0 a 100
        
        do{
            System.out.println("Ingrese un número");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero > random) {
                System.out.println("Es MENOR");
            } else if(numero < random){
                System.out.println("Es MAYOR");
            } else {
                System.out.println("\t¡¡Bien hecho!!");
                System.out.println("\tEl número aleatorio era: " + random);
            }
            intentos ++;
        } while(numero != random);
        System.out.println("\tNúmero de intentos: " + intentos);
        
    }
}
