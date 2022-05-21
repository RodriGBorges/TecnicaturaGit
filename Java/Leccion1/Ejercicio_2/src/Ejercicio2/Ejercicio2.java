
package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        //Ejercicio 2:
        //Hacer un programa que calcule e imprima el salario de un empleado, a partir de sus horas
        //semanales trabajadas y de su salario por hora
        
        //horas semanales
        //salario por hora
        
        /**/
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese los siguientes datos para calcular su salario");
        System.out.println("");
        
        System.out.println("Ingrese las horas semanales trabajadas.");
        var horasSemanales = entrada.nextLine();
        
        System.out.println("Ingrese su paga $ por hora.");
        var salarioHora = entrada.nextLine();
        
        int resultado = Integer.parseInt(horasSemanales) * Integer.parseInt(salarioHora);
        
        System.out.println("Su salario es: $" + resultado);
        
        System.out.println("");
        System.out.println("Parte 2");
        System.out.println("");
        
        
        // Solución profe
        
        int horasSemanales2;
        float salarioHora2, salarioTotal;
        
        System.out.println("Ingrese las horas semanales trabajadas 2");
        horasSemanales2 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el salario que cobra por hora.");
        salarioHora2 = Float.parseFloat(entrada.nextLine());
        salarioTotal = horasSemanales2 * salarioHora2;
        System.out.println("\nEl salario semanal es: US$" + salarioTotal);
        
        
    }
}
