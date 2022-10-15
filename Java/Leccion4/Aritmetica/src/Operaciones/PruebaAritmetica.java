
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
        
        //Persona persona = new Persona(new String("Rodrigo"), "Garayalde"); No es necesario
        Persona persona = new Persona("Rodrigo", "Garayalde");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }
    
    //Modularidad creamos un nuevo método
    public static void miMetodo(){
        //a = 10; // Una variable es limitada - los atributos, métodos, constructores transcienden
        int a = 10;
        System.out.println("Aquí hay otro método");
    }
}

// Solo se puede crear una clase public -linea 4- (modificador de acceso)
// Creamos una nueva clase
class Persona {
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido) { //Constructor
        super(); //LLamada al constructur de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}

class Imprimir {
    public Imprimir() {
        super(); // El constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona) {
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresión del objeto actual (this): " + this);
    }
}
    