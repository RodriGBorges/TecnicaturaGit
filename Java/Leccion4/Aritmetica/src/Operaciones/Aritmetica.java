
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //El constructor es un método especial
    public Aritmetica() { // Constructor 1 vacío
        System.out.println("Se está ejecutando este constructor número uno");
    }
    
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando el constructor número 2");
    }
    
    //Metodo
    // void = no retorna / regresa nada
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    // NO ES RECOMENDABLE CREAR EL MAIN LUEGO DE ESTO
    
    // Tipo de retorno entero (int) / retorna int
    public int sumarConRetorno(){
        // int resultado = a + b;
        // o return resultado;
        
        //return a + b;
        return this.a + this.b;
    }
    
    //el argumento es la información que va a recibir el metodo
    public int sumarConArgumentos(int arg1, int arg2){
        //a = arg1;
        //b = arg2;
        //return a + b
                
        a = arg1;
        b = arg2;
        
        //Llamamos a un método que comparten la misma clase
        return sumarConRetorno();
    }
    
    public int sumarConArgumentos2(int a, int b){
        //java sabe distinguir entre los argumentos y las variables
        // el this.a es la variable y "a" el argumento
        
        // El uso de this es opcional
        
        this.a = a; // El argumento "a" se asigna al atributo this.a
        this.b = b;
        
        //Llamamos a un método que comparten la misma clase
        return this.sumarConRetorno();
    }
}
