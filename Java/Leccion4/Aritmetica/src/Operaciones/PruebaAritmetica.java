
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        
        var a = 10; //Variables locales
        int b = 7; // Memoria stack - Solo para variables locales                //
        miMetodo(); //Llamamos el método nuevo
        
        //objeto = aritmetica1
        Aritmetica aritmetica1 = new Aritmetica();
        //Llamamos a la clase en sí y también al constructor
        
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros(); //Método sumarNumeros
        // Para almacenar un objeto o los atributos se utiliza la memoria heap   //
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);
        
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
        // no es necesario la limpieza de datos, Java lo hace automáticamente
        // aritmetica1 = null otra forma 
        //System.gc() una forma de limpiar residuos pero NO SE UTILIZA, NO ES NECESARIO
        // gc = garbage collector
    }
    
    public static void miMetodo(){
        //a = 10; // Una variable es limitada - los atributos, métodos, constructores transcienden
        int a = 10;
        System.out.println("Aquí hay otro método");
    }
}
    