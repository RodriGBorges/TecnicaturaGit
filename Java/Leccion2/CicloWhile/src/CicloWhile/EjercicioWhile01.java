
package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en 1 la variable
        }
        //Diferencia es que el primero entra en la condicion y el doWhile 
        // ejecuta el codigo y despues ve la condicion
        System.out.println("");
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        }while (contador < 7); //es necesario poner ;
        System.out.println("");
        //1er lugar, para declarar o crear la variable, ejem: int i = 0
        //2do, condicion a cumplir
        //3er, incremento o decremento de la variable
        for(var contando = 0;contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
        
        /*
        for(int i=1;i!=0;i++){
            System.out.println("Print eterno");
        }
        */
        //Con Break: apenas encuentre algo que matchee con la condicion se frena
        // Y continue junto a las etiquetas (labels)
        // Etiquetas Labels
        inicio:
        for(var contandoBreak = 0;contandoBreak < 7; contandoBreak++){
            if(contandoBreak % 2==0){
                System.out.println("contandoBreak = " + contandoBreak);
                break inicio;
            }
        }
        //Con Continue: 
        for(var contandoContinue = 0;contandoContinue < 7; contandoContinue++){
            if(contandoContinue % 2!=0){
                continue; //Vamos a la siguiente iteracion
            }
            System.out.println("contandoContinue = " + contandoContinue);
        }
        
    }
}
