
import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        
        // Clase 1 //
        /*
        System.out.println("Hola mundo desde Java");
        */
        
        // Clase 2 //
        
        /*
        //Variable tipo int
        int miVariable = 10;
        System.out.println(miVariable);
        
        //renombrar variable
        miVariable = 25;
        System.out.println(miVariable);
        
        //Variable tipo string
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        //Apretando control + click izq sobre la variable impresa nos envía a donde fue definida la variable
        */
        
        // Clase 3 //
        
        /*
        
        //Var - inferencia de tipos en Java
        // Ejecutar Shift + F6
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //acceso directo = soutv + tab ===> línea de arriba
        
        //Regla para definir una variable en Java: 
        
        //Se recomienda utilizar métoo de escritura camelCase
        //No se pueden utilizar números como primer carácter de la variable
        //Sí puede tener guión bajo
        //Se puede utilizar el signo del Dólar $
        //No se recomienda utilizar acentos
        // Carácter ILEGAL " # " 
        
        // Dar formato / ordenar código = Alt + Shift + F
        
        var usuario = "Osvaldo";
        var titular = "Ingeniero";
        var union = titular + "" + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        
        //Contexto de las variables: Prioridad de izquierda a derecha
        //Primero se lee la primer variable: Si la primera es tipo string va a concatenar, si es tipo int va a sumar
        
        System.out.println(a + b);  //Suma
        System.out.println(usuario + a + b); // concatena
        System.out.println(usuario + (a + b)); // con paréntesis podemos modificar la prioridad
        
        
        //Ejercicio: Carácteres especiales con Java
        
        var nombre = "Natalia";
        System.out.println("\nNueva Linea: \n" + nombre); //SALTO DE LINEA CON " \n "
        System.out.println("Tabulador: \t" + nombre);  // Tabulador con " \t " un espacio para centrar
        System.out.println("\t\t.:MENÚ:.");
        System.out.println("Retroseso: \b\b" + nombre);  //Carácter de Retroseso = Quita los espacios y/o carácteres 
        System.out.println("Comillas simples: \'" + nombre + "\'");  // Comillas simples
        System.out.println("Comillas dobles: \"" + nombre + "\"");  // Comillas dobles
        
        
        
        // Clase Scanner
        
        //Si sale en rojo importamos con click derecho en el foco de las líneas
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba profesión: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " + titulo2 + " " + usuario2);

        */
    }
}
