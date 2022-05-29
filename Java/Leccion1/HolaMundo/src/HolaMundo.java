
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
        
        // Clase 4 //
        // TIPOS NÚMERICOS ENTEROS
        
        /*
        
        //byte numEnteroByte = 10;
        byte numEnteroByte = 127; // Max
        // byte numEnteroByte = (byte)129; Lo obligamos a convertir el valor númerico entero en byte
        //El compilador nos avisa que se han ocupado los 127 números positivos, al pasar el rango se pierde información por lo tanto nos da -127
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor mínimo del byte:" + Byte.MIN_VALUE);
        System.out.println("Valor máximo del byte:" + Byte.MAX_VALUE);
        System.out.println("");
        
        //short numEnteroShort = 10;
        short numEnteroShort = 32767; // Max
        //short numEnteroShort = (short)32768; // Pasa el mismo problema, pérdida de bits al momento de hacer la conversión
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor mínimo del short:" + Short.MIN_VALUE);
        System.out.println("Valor máximo del short:" + Short.MAX_VALUE);
        System.out.println("");
        
        //int numEnteroInt = 10;
        int numEnteroInt = 2147483647; // Max
        //int numEnteroInt = (int)2147483648L; por más que se le fuerze no se arregla el error, debemos ponerle una L,
        //al poner la letra L pasa a ser un dato de tipo long, pero sin embargo seguimos teniendo pérdida de información
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor mínimo del int:" + Integer.MIN_VALUE);
        System.out.println("Valor máximo del int:" + Integer.MAX_VALUE);
        System.out.println("");
        
        //long numEnteroLong = 10;
        long numEnteroLong = 9223372036854775807L; // Max, Java toma los números siempre por tipo Int, se debe poner la L al final.
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor mínimo del long:" + Long.MIN_VALUE);
        System.out.println("Valor máximo del long:" + Long.MAX_VALUE);
        System.out.println("");
        
        
        //float numFloat = 10.0F; La F para indicarle que es un número tipo Flotante ya que por default Java lo toma como un tipo de dato Double
        // o tambíen se puede poner (float)10.0
        float numFloat = 3.4028235E38F;
        //float numFloat = (float)3.4028236E38; Si superamos el máximo vamos a generar una pérdida de información
        // Si superamos el número máximo nos marca como Infinity = Inválido
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor mínimo de float: " + Float.MIN_VALUE);
        // valor mínimo 1.4E-45 (E de Exponencial // Exponencial 45 posiciones a la izquierda)
        System.out.println("El valor máximo de float: " + Float.MAX_VALUE);
        // valor máximo 3.4028235E38 (Exponencial 38 posiciones a la derecha)
        System.out.println("");
        
        //double numDouble = 10;
        double numDouble = 1.7976931348623157E308; //No hace falta poner la D al final
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor mínimo de double: " + Double.MIN_VALUE);
        // El valor mínimo de double: 4.9E-324 (4.9 exponencial 324 posiciones hacia la izquierda -valor negativo-)
        System.out.println("El valor máximo de double: " + Double.MAX_VALUE);
        // El valor máximo de double: 1.7976931348623157E308 (exponencial 308 posiciones a la derecha)
        
        */
        
        // Clase 5 //
        
        //Inferencia de tipos var y tipos primitivos
        // Ejecutar en paso a paso
        /*
        
        var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0; //Automaticamente con el punto se transforma en double
        System.out.println("numDouble = " + numDouble);
        
        //Tipos primitivos char
        
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);        
        char varCaracter = '\u0024'; // Indicamos a Java la asignación con el código unicode
        System.out.println("varCaracter = " + varCaracter);        
        char varCaracterDecimal = 36; // Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);        
        char varCaracterSimbolo = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        
        var varCaracter1 = '\u0024'; // Indicamos a Java la asignación con el código unicode
        System.out.println("varCaracter1 = " + varCaracter1);        
        var varCaracterDecimal1 = (char)36; // Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);        
        var varCaracterSimbolo1 = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);        
        int caracaterChar = 'b';
        System.out.println("caracaterChar = " + caracaterChar);

        */
        
        // Clase 6 
        // Tipos primitivos tipos booleanos
        
        /*
        
        boolean varBool = false;
        System.out.println("varBool = " + varBool);
        
        //if(varBool == true) { }
        // es lo mismo que:
        if(varBool) {
            System.out.println("La bandera es verde");
        } else {
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        
        var edad = 23;
        //var adulto = edad >= 18;
        if(edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }
        
        //Conversión de tipos primitivos
        
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad");
        // si ingresamos un dato tipo string nos da error "NumberFormatException"
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        
        
        
        // Conversión de tipos primitivos en Java Parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar);
        
        var entrada = new Scanner(System.in);
        System.out.println("Digite un caracter");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        */
        
        //Clase 8 
        //Operadores Unarios: Cambio de Signo
        
        /*
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); //El resultado sera un número negativo
        
        //Operador de Negación
        var varC = true; //Esta literal por default en Java es de tipo Boolean
        var varD = !varC; //Aqui esta inviritiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores Unarios de Incremento: Preincremento
        var varE = 9; // Se va a modificar su valor
        var varF = ++varE; //Simbolo antes de la variable
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);
        
        //Postincremento (el simbolo va después de la variable)
        var varG = 3;
        var varH = varG++; //Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores unarios de decremento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI); //La variable ya está con decremento
        System.out.println("varJ = " + varJ);
        
        //Postdecremento
        var varK = 8;
        var varL = varK--; //Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK); //Aqui va a decrementar en 1 
        System.out.println("varL = " + varL);
        
        //Operadores de igualdad y Relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        //se usa equals para las cadenas
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var qVar = aNum >= bNum; //> >= < <= == !=
        System.out.println("qVar = " + qVar);
        
        if (aNum % 2 == 0)
            System.out.println("El número es par");
        else 
            System.out.println("El número es impar");

        
        
        //Operador condicional and
        var valorA = 7;
        var valorMinimo = 0; //Rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;
        
        if (respuesta == true) {
            System.out.println("Está dentro del rango establecido");
        } else {
            System.out.println("Está fuera del rango establecido");
        }
        
        //Operador Or
        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) {
            System.out.println("Usted puede asistir al evento");
        } else {
            System.out.println("Usted no puede asistir al evento");
        }

        
        
        //Operador ternario
        var resultado = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultado = " + resultado);
        
        var numeroT = 7;
        var resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);

        
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        
        var solucionAritmetica = 4 + 5 * 6 / 3; //4 + ((5 * 6) / 3)
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3; // 4 + 5 = 9 * 6 = 54 / 3 = 18;
        System.out.println("solucionAritmetica = " + solucionAritmetica);

        */
        
        
    }
}
