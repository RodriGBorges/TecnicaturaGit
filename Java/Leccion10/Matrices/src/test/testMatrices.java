
package test;

import domain.Persona;

public class testMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        
        edades[0][0] = 5; // Llenado manual
        edades[0][1] = 7; // En una diferente columna
        edades[1][0] = 8; //En una diferente fila
        edades[1][1] = 4;
        edades[2][0] = 2;
        edades[2][1] = 9;
        
        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 2-0 = " + edades[2][0]);
        System.out.println("edades 2-1 = " + edades[2][1]);
        
        System.out.println("Recorremos la matriz a través del ciclo for");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int columna = 0; columna < edades[fila].length; columna++) {
                System.out.println("edades " + fila + "-" + columna + ": " + edades[fila][columna]);
            }
        }
        System.out.println("");
        //Sintaxis clásica 
        //izq => definimos la variable / der => instanciamos
        //String frutas[][] = new String[3][2];
        
        //Sintaxis simplificada
        String frutas[][] = {{"Limon", "Pomelo"}, {"Ciruela", "Kiwi"}, {"Banana", "Manzana"}};
        System.out.println("Matriz de frutas");
        imprimir(frutas);
        /*
        for (int i = 0; i < frutas.length; i++) {
            for (int j = 0; j < frutas[i].length; j++) {
                System.out.println("frutas " + i + "-" + j + ": " + frutas[i][j]);
            }
        }
        */
        
        System.out.println("");
        Persona personas[][] = new Persona[2][3];
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Ciclope");
        personas[0][1] = new Persona("Magneto");
        personas[0][2] = new Persona("Phoenix");
        personas[1][0] = new Persona("ProfesorX");
        personas[1][1] = new Persona("Wolverine");
        personas[1][2] = new Persona("Storm");
        System.out.println("Matriz de personas");
        imprimir(personas);
    }
    
    public static void imprimir(Object matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("matriz " + i + "-" + j + ": " + matriz[i][j]);
            }
        }
    }
}
