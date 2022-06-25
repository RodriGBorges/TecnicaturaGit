
package EjercicioGrupal;

import java.util.Scanner;

public class Ejercicios {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        // Ejercicio 1: Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobará si su promedio de tres
        // calificaciones es mayor o igual a 70 reprueba caso contrario
        
        /*
        float nota1, nota2, nota3, promedio;
        
        System.out.println("Digite las 3 calificaciones: ");
        System.out.print("_ ");
        nota1 = Float.parseFloat(entrada.nextLine());
        System.out.print("_ ");
        nota2 = Float.parseFloat(entrada.nextLine());
        System.out.print("_ ");
        nota3 = Float.parseFloat(entrada.nextLine());
        
        promedio = (nota1 + nota2 + nota3) * 10 / 3;
        
        if (promedio >= 70)
            System.out.println("El alumno está aprobado con: " + promedio);
        else
            System.out.println("El alumno está desaprobado con: " + promedio);
        
        */
        
        // Ejercicio 2: En un almacén se hace un 20 MOD de descuento a los clientes cuya compra supere los $100.
        // ¿Cuál será la cantidad que pagará una persona por su compra?
        
        /*
        float compra, descuento, precioFinal;
        System.out.println("Digite la cantidad a pagar: ");
        System.out.print("_ ");
        compra = Float.parseFloat(entrada.nextLine());
        
        if (compra > 100)
            descuento = compra * 0.2F;
        else
            descuento = 0;
        
        precioFinal = compra - descuento;
        
        System.out.println("El precio a pagar es: " + "$" + precioFinal);
        */
        
        // Ejercicio 3: Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste
        // y si no que los sume
        
        float num1, num2, resultado;
        System.out.println("Digite dos números: ");
        System.out.print("_ ");
        num1 = Float.parseFloat(entrada.nextLine());
        System.out.print("_ ");
        num2 = Float.parseFloat(entrada.nextLine());
        
        if (num1 == num2) {
            System.out.println("Los números son iguales.");
            resultado = num1 * num2;
        } else if (num1 > num2) {
            System.out.println("El número 1 es el mayor");
            resultado = num1 - num2;
        } else {
            System.out.println("El número 2 es el mayor");
            resultado = num1 + num2;
        }
        
        System.out.println("El resultado es: " + resultado);
        
    }
}
