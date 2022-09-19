
package Ciclos06;

import javax.swing.JOptionPane;

public class Ejercicio06 {
    public static void main(String[] args) {
         /*
        Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar la suma de
        todos los números en pantalla
        */
        
        int numero, suma = 0;
        
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            suma += numero;
            
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "El número 0 finaliza el programa");
        JOptionPane.showMessageDialog(null, "\nLa suma de todos los números es: " + suma);

    }
}
