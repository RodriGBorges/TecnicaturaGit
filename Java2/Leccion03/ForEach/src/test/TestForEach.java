
package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9}; //Sintaxis resumida
        
        //ForEach
        //Debe ser una variable del mismo tipo: int edades => int edad
        //No es posible acceder al índice con foreach
        for(int edad: edades) {
            System.out.println("edad = " + edad);
        }
        
        Persona personas[] = {new Persona("Juan"), new Persona("Carla"), new Persona("Pedro")};
        
        //ForEach
        for(Persona persona: personas) {
            System.out.println("persona = " + persona);
        }
    }
}
