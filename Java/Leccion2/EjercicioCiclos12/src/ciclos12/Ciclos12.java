
package ciclos12;

//import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos12 {
    public static void main(String[] args) {
        /*
            Ejercicio 12: Pedir un número y calcular su factorial
            Hacerlo con las dos clases, Scanner y JOptionPane
        */
        //Scanner entrada = new Scanner(System.in);
        
        long factorial = 1;
        //System.out.println("Ingrese un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        //System.out.println("\nEl factorial del número ingresado es: " + factorial);
        JOptionPane.showMessageDialog(null, "El factorial del número ingresado es: " + factorial);
    }
}
