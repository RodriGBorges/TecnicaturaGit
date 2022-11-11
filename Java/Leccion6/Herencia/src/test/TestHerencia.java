
package test;

import domain.Cliente;
import domain.Empleado;
import domain.Persona;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Liliana", 87000.0);
        System.out.println("empleado1 = " + empleado1);
        
        //        Date fecha1 = new Date();
        //        
        //        Cliente cliente1 = new Cliente(fecha1, true, "Lili", 'F', 37, "24 de octubre 321");
        //        System.out.println("cliente1 = " + cliente1);
        //        
        //        Persona persona1 = new Persona();
    }
}
