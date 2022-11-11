
package test;

//import ar.com.codesystem.*; Si hay muchas más clases
//import ar.com.codesystem.Utileria; 1 RECOMENDABLE

//Solo aplica para métodos estáticos
//import static ar.com.codesystem.Utileria.imprimir; 2

 class TestUtileria {
     public static void main(String[] args) {
         //Utileria.imprimir("Saludos a todos los alumnos"); 1 RECOMENDABLE
         
         //imprimir("Terminamos en unos minutos"); 2
         
         //No recomendable 
         ar.com.codesystem.Utileria.imprimir("Ahora si estamos terminando");
     }
}
