
package domain;

// Empleado extends Persona => Empleado hija de Persona
public class Empleado extends Persona {
    
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //Es para incrementar
    
    //Constructores
    
    public Empleado() { //Constructor 1
        this.idEmpleado = ++Empleado.contadorEmpleados;
    }
    
    public Empleado(String nombre, double sueldo) { //Constructor 2
        // o usamos super o this, no se debe utilizar las dos
        //super(nombre);
        this(); //Estamos llamando desde aquí al constructor vacío(llamar a un constructor interno)
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    //Getters and setters
    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    
    //toString con StringBuilder
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
}
