
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


//Ejercicio 1: Calcular estación del año
let mes = 8;
let estacion; // variable vacía
/* 
if(mes == 1 || mes == 2 || mes == 12) {
    estacion = 'Verano';
} else if(mes == 3 || mes == 4 || mes == 5) {
    estacion = 'Otoño';
} else if(mes == 6 || mes == 7 || mes == 8) {
    estacion = 'Invierno';
} else if(mes == 9 || mes == 10 || mes == 11) {
    estacion = 'Primavera';
} else {
    estacion = 'Valor incorrecto';
}

console.log(`El valor corresponde a la estación de: ${estacion}`);
 */
//Ejercicio 2: Hora del día
/* 
de 6 a 11 nos saluda: Good morning
de 12 a 16 nos saluda: Good afternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good night
Trabajaremos con 24 horas
*/

let horaDia = 20;
let mensaje;

if(horaDia >= 6 && horaDia <= 11) {
    mensaje = 'Good morning';
} else if(horaDia >= 12 && horaDia <= 16) {
    mensaje = 'Good afternoom';
} else if(horaDia >= 17 && horaDia <= 19) {
    mensaje = 'Good evening';
} else if(horaDia >= 20 && horaDia <= 23){
    mensaje = 'Good night';
} else {
    mensaje = 'Valor incorrecto';
}

console.log(mensaje);

//Estructura switch => Comparación estricta

switch (mes) {

    case 1: case 2: case 12:
        estacion = 'Verano';
        break;
    
    case 3: case 4: case 5:
        estacion = 'Otoño';
        break;
    
    case 6: case 7: case 8:
        estacion = 'Invierno';
        break;
    
    case 9: case 10: case 11:
        estacion = 'Primavera';
        break;
    
    default:
        estacion = 'Valor incorrecto';
        break;
}

console.log(`El valor corresponde a la estación de: ${estacion}`);