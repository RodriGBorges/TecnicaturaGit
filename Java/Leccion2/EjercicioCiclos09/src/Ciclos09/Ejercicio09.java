
package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicio09 {
    public static void main(String[] args) {
        
        /*
            Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si la
            fecha es correcta. Suponiendo que todos los meses son de 30 días.
        */

        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día: "));

        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));

        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));
        
        if((dia > 0) && (dia <= 30)) {
            if((mes > 0) && (mes <= 12)) {
                if((anio > 0) && (anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta > Año " + "'" + anio + "'" + " incorrecto");
                }
            } else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta > Mes " + "'" + mes + "'" + " incorrecto");
            }
        } else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta > Día " + "'" + dia + "'" + " incorrecto");
        }
    }
}
