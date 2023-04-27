
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

//Evita repetir tu código
//Dry don't repeat yourself

let days = 'Sábado';
// let days = 1;

switch (days) {
    case 'Lunes':
        console.log(`Hoy es ${days}`);
        break;
    case 'Martes':
        console.log(`Hoy es ${days}`);
        break;
    case 'Miércoles':
        console.log(`Hoy es ${days}`);
        break;
    case 'Jueves':
        console.log(`Hoy es ${days}`);
        break;
    case 'Viernes':
        console.log(`Hoy es ${days}`);
        break;
    case 'Sábado':
        console.log(`Hoy es ${days}`);
        break;
    case 'Domingo':
        console.log(`Hoy es ${days}`);
        break;

    default:
        console.log('Error en el ingreso del día de la semana');
        break;
}

let days2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
function getDay(n) {
    if(n < 1 || n > 7) {
        throw new Error('out of range');
    }
    return days2[n - 1]
}

console.log(getDay(5));


let mes2 = 11;

switch (mes2) {
    case 1:
        console.log('El mes es Enero');
        break;
    case 2:
        console.log('El mes es Febrero');
        break;
    case 3:
        console.log('El mes es Marzo');
        break;
    case 4:
        console.log('El mes es Abril');
        break;
    case 5:
        console.log('El mes es Mayo');
        break;
    case 6:
        console.log('El mes es Junio');
        break;
    case 7:
        console.log('El mes es Julio');
        break;
    case 8:
        console.log('El mes es Agosto');
        break;
    case 9:
        console.log('El mes es Septiembre');
        break;
    case 10:
        console.log('El mes es Octubre');
        break;
    case 11:
        console.log('El mes es Noviembre');
        break;
    case 12:
        console.log('El mes es Diciembre');
        break;

    default:
        console.log('Error => No existe ese mes');
        break;
}

let mes3 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
function getMes(n) {
    if(n < 1 || n > 12) {
        throw new Error('out of range');
    }
    return mes3[n - 1]
}

console.log(getMes(7));
