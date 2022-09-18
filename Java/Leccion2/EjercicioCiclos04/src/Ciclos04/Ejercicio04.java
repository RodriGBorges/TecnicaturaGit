
package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        /*
        Ejercicio 4: Pedir números hasta que se teclee uno negativo,
        y mostrar cuántos números se han introducido.
        Lo haremos primero con la clase JOptionPane
        */

        int numero, conteo = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        
        while(numero >= 0) {
            JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            conteo ++;
            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + conteo + " números que NO son negativos");
    }
}

