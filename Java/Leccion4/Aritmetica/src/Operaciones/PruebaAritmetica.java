
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        //objeto = aritmetica1
        Aritmetica aritmetica1 = new Aritmetica();
        //Llamamos a la clase en sí y también al constructor
        
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros(); //Método sumarNumeros
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);
    }
}
    