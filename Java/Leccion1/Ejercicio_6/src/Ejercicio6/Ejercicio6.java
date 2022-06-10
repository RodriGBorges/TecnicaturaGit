
package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float billeteraGuille, billeteraLuis, billeteraJuan, sumaTotal;
        System.out.println ("Digite la cantidad de dinero en dolares que tiene Guillermo: ");
        billeteraGuille = Float.parseFloat(entrada.nextLine());
        
        billeteraLuis = billeteraGuille / 2;
        billeteraJuan = (billeteraGuille + billeteraLuis) / 2;
        
        sumaTotal = billeteraGuille + billeteraLuis + billeteraJuan;
        System.out.println("\nEl dinero de Luis es: " + billeteraLuis);
        System.out.println("\nEl dinero de Juan es: " + billeteraJuan);
        System.out.println("\nLa cantidad de dinero que juntan Guillermo, Luis y Juan es = " + sumaTotal);
    }
}
