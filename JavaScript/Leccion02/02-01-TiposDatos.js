// Tipos de Datos en JavaScript
/* 
La sintaxis en lo que es comentarios es muy similar 
a la de Java realmente diriamos que es indentica
*/

var nombre = "Ariel"; // Tipo String
console.log(typeof nombre);

nombre = 7;
console.log(typeof nombre);

nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; // Tipo Numerico
console.log(numero);

var objeto = {
    nombre: "Ariel",
    apellido: 'Betancud',
    telefono: '2614567893'
}

console.log(objeto);
console.log(typeof objeto);

// Tipo de dato boolean

var bandera = true;
console.log(bandera);
console.log(typeof bandera);

// Tipo de dato funcion
function miFuncion() {}
console.log(miFuncion);
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);
console.log(typeof simbolo);

// TIpo de dato clase
class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(Persona);
console.log(typeof Persona);

// Tipo de dato undefined
var x;
console.log(x);
console.log(typeof x);
x = undefined;
console.log(x);


// Tipo de dato null => significa ausencia de valor
var y = null;
// null no es un tipo de dato, pero su origen es object
console.log(y);
console.log(typeof y);

// Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z); //Una cadena vacía
console.log(typeof z);