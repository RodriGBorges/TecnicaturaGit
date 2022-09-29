package Ciclos08;

import javax.swing.JOptionPane;


public class Ejercicio08 {
    public static void main(String[] args) {
        /*
            Ejercicio 8: Pedir un número N, y mostrar todos los números del 1 al N
        */

        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        int i = 1;
        
        while(i <= numero) {
            JOptionPane.showMessageDialog(null, "i= " + i);
            i++;
        }
    }
}
