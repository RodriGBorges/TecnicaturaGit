
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        /*
        Ejercicio 5: Realizar un juego para adivinar un número,
        para ello generar un número aleatorio entre 0-100, y luego ir pidiendo
        números indicando "es mayor" o "es menor" según sea mayor o menos con 
        respecto a N.
        El proceso termina cuando el usuario acierta y mostramos el número
        de intentos hechos
        */
        
        
        int numero, random, intentos = 0;
        
        random = (int)Math.floor(Math.random() * 100); //Genera un número aleatorio de 0 a 100
        
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            if(numero > random) {
                JOptionPane.showMessageDialog(null, "Es MENOR");
            } else if(numero < random){
                JOptionPane.showMessageDialog(null, "Es MAYOR");
            } else {
                JOptionPane.showMessageDialog(null, "¡¡ADIVINASTE!!");
                JOptionPane.showMessageDialog(null, "El número aleatorio era: " + random);
            }
            intentos ++;
        } while(numero != random);
        JOptionPane.showMessageDialog(null, "Número de intentos: " + intentos);
    }
}
