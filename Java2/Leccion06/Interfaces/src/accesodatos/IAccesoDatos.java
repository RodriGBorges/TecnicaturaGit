
package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRO = 10;
    
    //Método insertar es abstractor y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
}
