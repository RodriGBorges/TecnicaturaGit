
/*
    VAR: puede modificarse en cualquier momento este forma parte del ambito global
    Un error es que se sobreescriba  
*/

var nombre = 'Lucifer';
nombre = 'Morningstar';
console.log(nombre);

function saludar(){
var nombre2 = 'Florencia';
console.log(nombre2);
}

// console.log(nombre2); //No alcanza el dato dentro de la función


if(true){
var edad = 34;
console.log(edad);
}
console.log(edad); //En la función alcanza el dato correctamente, en la estructura if fallo

/*
LET: puede ser modificada en cualquier momento
la diferencia es que su ambito es de bloque, solo disponible dentro de un bloque de llaves o dentro de una función
*/

function saludar2(){
let nombre2 = 'Rodrigo';
console.log(nombre2);
}
//console.log(nombre2);

if(true){
let edad2 = 33;
console.log(edad2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser modificados luego de asignarles un valor
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior