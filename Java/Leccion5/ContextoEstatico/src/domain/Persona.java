
package domain;

public class Persona {
    
    // Cargamos los atributos
    private int idPersona;
    // Al no ser estático cada vez que creamos un objeto vuelve a 0, se reinicia a 0
    private static int contadorPersona;
    private String nombre;
    
    // Constructor
    public Persona(String nombre) {
        this.nombre = nombre;
        
        // Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona ++; // No utilizar el operador this
        // Vamos a asignar un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersona;
    }
    
    // click derecho -> insert code -> Getters and Setters... -> 
    // Encapsulate fields -> generate
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    // click derecho -> insert code -> toString().. -> generate
    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
}
