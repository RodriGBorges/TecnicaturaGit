
package ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        /*
        Ejercicio 10: Pedir 10 números y escribir la suma total
        con JOptionPane
        */
        
        int numero, suma = 0;
        for(int i = 1; i <= 10; i++) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            suma += numero;
        }
        
        JOptionPane.showMessageDialog(null, "\nLa suma total es: " + suma);
        
    }
}
