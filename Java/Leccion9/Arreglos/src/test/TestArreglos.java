
package test;

public class TestArreglos {
    public static void main(String[] args) {
        //lado izq => declaración de la variable
        //lado der => instanciamos un objeto de tipo object
        int edades[] = new int[3]; // 3 elementos, índices (por default reciben 0)
        
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades pos. 0 = " + edades[0]);
        
        edades[1] = 3;
        System.out.println("edades pos. 1 = " + edades[1]);
        
        edades[2] = 8;
        System.out.println("edades pos. 2 = " + edades[2]);
        
        System.out.println("\nCiclo for: ");
        for(int i = 0; i < edades.length; i++) {
            System.out.println("Indice: " + i + "\n" + "Valor: " + edades[i]);
            System.out.println("");
        }
    }
}
