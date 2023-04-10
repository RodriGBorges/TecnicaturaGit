
package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); //Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //Creamos otros objetos de diferente marca
        Monitor monitorGamer = new Monitor("Gamer", 27);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
        Monitor monitorSamsung = new Monitor("Samsung", 19);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);
        
        Monitor monitorNoblex = new Monitor("Noblex", 24);
        Teclado tecladoNoblex = new Teclado("Bluetooth", "Noblex");
        Raton ratonNoblex = new Raton("Bluetooth", "Noblex");
        Computadora computadoraNoblex = new Computadora("Computadora Noblex", monitorNoblex, tecladoNoblex, ratonNoblex);
        
        Monitor monitorGenius = new Monitor("Genius", 24);
        Teclado tecladoGenius = new Teclado("USB", "Genius");
        Raton ratonGenius = new Raton("USB", "Genius");
        Computadora computadoraGenius = new Computadora("Computadora Genius", monitorGenius, tecladoGenius, ratonGenius);
        
        Monitor monitorLogitech = new Monitor("Logitech", 25);
        Teclado tecladoLogitech = new Teclado("USB", "Logitech");
        Raton ratonLogitech = new Raton("USB", "Logitech");
        Computadora computadoraLogitech = new Computadora("Computadora Logitech", monitorLogitech, tecladoLogitech, ratonLogitech);
        
        Monitor monitorLG = new Monitor("LG", 29);
        Teclado tecladoLG = new Teclado("Bluetooth", "LG");
        Raton ratonLG = new Raton("Bluetooth", "LG");
        Computadora computadoraLG = new Computadora("Computadora LG", monitorLG, tecladoLG, ratonLG);
        
        Monitor monitorSony = new Monitor("Sony", 30);
        Teclado tecladoSony = new Teclado("Bluetooth", "Sony");
        Raton ratonSony = new Raton("Bluetooth", "Sony");
        Computadora computadoraSony = new Computadora("Computadora Sony", monitorSony, tecladoSony, ratonSony);
        
        Monitor monitorRedDragon = new Monitor("RedDragon", 26);
        Teclado tecladoRedDragon = new Teclado("USB", "RedDragon");
        Raton ratonRedDragon = new Raton("USB", "RedDragon");
        Computadora computadoraRedDragon = new Computadora("Computadora RedDragon", monitorRedDragon, tecladoRedDragon, ratonRedDragon);
        
        Monitor monitorHyperX = new Monitor("HyperX", 27);
        Teclado tecladoHyperX = new Teclado("Bluetooth", "HyperX");
        Raton ratonHyperX = new Raton("Bluetooth", "HyperX");
        Computadora computadoraHyperX = new Computadora("Computadora HyperX", monitorHyperX, tecladoHyperX, ratonHyperX);
        Orden orden1 = new Orden(); //Inicializamos el arreglo vacío
        Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(computadoraSamsung);
        orden1.agregarComputadora(computadoraNoblex);
        orden1.agregarComputadora(computadoraGenius);
        orden1.agregarComputadora(computadoraLogitech);
        orden1.agregarComputadora(computadoraLG);
        orden1.agregarComputadora(computadoraSony);
        orden1.agregarComputadora(computadoraRedDragon);
        orden1.agregarComputadora(computadoraHyperX);
        
        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonGamer);
        orden2.agregarComputadora(computadorasVarias);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
        //Crear mas objetos de tipo computadora con todos sus elementos
        //Completar una lista en el objeto orden1 que llegue a los 10 elementos
        //probar de esta manera los métodos al máximo rendimiento
    }
}
