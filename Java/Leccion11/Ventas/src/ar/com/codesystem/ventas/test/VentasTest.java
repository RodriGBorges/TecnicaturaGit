
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Remera", 7900.00);
        Producto producto4 = new Producto("Short", 4900.00);
        Producto producto5 = new Producto("Gorro", 3900.00);
        Producto producto6 = new Producto("Musculosa", 4900.00);
        Producto producto7 = new Producto("Buzo", 19900.00);
        Producto producto8 = new Producto("Boxer", 2900.00);
        Producto producto9 = new Producto("Medias", 1900.00);
        Producto producto10 = new Producto("Calza", 2900.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        System.out.println("");
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto7);
        orden2.mostrarOrden();
        
        System.out.println("");
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto1);
        orden3.agregarProducto(producto2);
        orden3.agregarProducto(producto3);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.mostrarOrden();
    }
}
