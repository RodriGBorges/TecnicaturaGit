
package test;

import operaciones.Operaciones;

public class TestOperaciones {
    public static void main(String[] args) {
        
        var resultado = Operaciones.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        
        System.out.println("");
        
        var resultado2 = Operaciones.sumar(5.0, 7);
        System.out.println("resultado2 = " + resultado2);
        
        var resultado3 = Operaciones.sumar(8, 6L);
        //Acudiría al método double porque int no soporta tipo long
        System.out.println("resultado3 = " + resultado3);
    }
}
