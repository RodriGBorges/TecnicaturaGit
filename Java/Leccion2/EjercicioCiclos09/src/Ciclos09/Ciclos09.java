
package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        /*
            Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si la
            fecha es correcta. Suponiendo que todos los meses son de 30 días.
        */
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese el día: ");
        int dia = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Ingrese el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Ingrese el año: ");
        int anio = Integer.parseInt(entrada.nextLine());
        
        if((dia > 0) && (dia <= 30)) {
            if((mes > 0) && (mes <= 12)) {
                if((anio > 0) && (anio <= 2022)) {
                    System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    System.out.println("Fecha incorrecta --> Año incorrecto");
                }
            } else {
                    System.out.println("Fecha incorrecta --> Mes incorrecto");
            }
        } else {
                    System.out.println("Fecha incorrecta --> Día incorrecto");
        }
    }
}
