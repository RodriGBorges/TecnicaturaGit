
package test;

import domain.Persona;

public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        
        personas[0] = new Persona("Uriel");
        personas[1] = new Persona("Gabriel");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
        
        System.out.println("");
        for(int i = 0; i < personas.length; i++) {
            System.out.println("personas " + i + " = " +personas[i]);
        }
        
        //Arreglos en la sintaxis resumida
        String frutas[] = {"Banana", "Pera", "Durazno"};
        
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("fruta = " + frutas[i]);
        }
    }
}
