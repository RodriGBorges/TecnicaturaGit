/*
    Proyecto caja:
    Ejercicio 1: Crear un proyecto según las especificaciones mostradas a
    continuación.
    La formula es: volumen = ancho * alto * profundidad
 */
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        // Variables locales
        int medidaAlto = 2;
        int medidaAncho = 3;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacío
        caja1.alto = medidaAlto; // Pasamos valores al objeto
        caja1.ancho = medidaAncho;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen(); // Se llama al método
        
        System.out.println("Resultado volumen de caja 1: " + resultado);
        
        Caja caja2 = new Caja(2, 4, 6); //Se llama al constructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al método para un nuevo cálculo
        System.out.println("Resultado volumen de caja 2: " + caja2.calcularVolumen());
        
    }
}
