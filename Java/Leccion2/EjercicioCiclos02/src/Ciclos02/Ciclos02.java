
package Ciclos02;

import javax.swing.JOptionPane;


public class Ciclos02 {
    public static void main(String[] args) {
        /*
        Ejercicio 2: Leer un número e indicar si es positivo o negativo.
        El proceso se repetira hasta que se ingrese un cero 0. Con JOptionPane
        */
        
        
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        
        while(numero != 0) { // Mientras el número sea distinto de 0
            if(numero > 0 ) {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            } else {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número " + numero + " finaliza el programa");
    }
}
