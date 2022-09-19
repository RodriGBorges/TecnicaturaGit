
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
    public static void main(String[] args) {
        /*
        Ejercicio 7: Pedir números hasta que se introduzca uno negativo
        y calcular la media
        */
        
        int numero, conteo = 0, sumaTotal = 0;
        float promedio = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            
        while(numero >= 0){
            sumaTotal += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
        }
        if(conteo == 0) {
            JOptionPane.showMessageDialog(null, "\nError --> La división entre cero no existe");
        } else {
            promedio = (float)sumaTotal/conteo;
            JOptionPane.showMessageDialog(null, "El promedio es: " + promedio);
        }
    }
}
