
package enumeraciones;

public enum Continentes {
    AFRICA(54, "1.3 millones"),
    EUROPA(44, "741 millones"),
    ASIA(50, "4.670 millones"),
    AMERICA(35, "1.080 millones"),
    OCEANIA(14, "42 millones");
    
    private final int paises;
    private final String habitantes;
    
    Continentes(int paises, String habitantes) {
        this.paises = paises;
        this.habitantes = habitantes;
    }
    
    //Método Get
    public int getPaises() {
        return this.paises;
    }
    
    public String getHabitantes() {
        return this.habitantes;
    }
}
