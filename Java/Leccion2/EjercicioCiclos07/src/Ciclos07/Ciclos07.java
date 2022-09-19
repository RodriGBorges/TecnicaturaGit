
package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
        /*
        Ejercicio 7: Pedir números hasta que se introduzca uno negativo
        y calcular la media
        */
        
        Scanner entrada = new Scanner(System.in);
        
        int numero, conteo = 0, sumaTotal = 0;
        float promedio = 0;
        
        System.out.println("Ingrese un número: ");
        numero = Integer.parseInt(entrada.nextLine());
            
        while(numero >= 0){
            sumaTotal += numero;
            conteo++;
            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo == 0) {
            System.out.println("\nError --> La división entre cero no existe");
        } else {
            promedio = (float)sumaTotal/conteo;
            System.out.println("El promedio es: " + promedio);
        }
        
    }
}
