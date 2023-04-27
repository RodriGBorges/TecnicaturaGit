//Ejercicio para encontrar números pares
let parInpar = 10;

if(parInpar % 2 == 0) {
    console.log('Es PAR');
} else {
    console.log('Es IMPAR');
}

//Ejercicio mayor de edad
let edad = 20, adulto = 18;
if(edad >= adulto) {
    console.log('Es mayor de edad');
} else {
    console.log('No es mayor de edad');
}

//Ejercicio: Dentro de un rango
let dentroRango = 5; //Cambiar valor
let valorMin = 0, valorMax = 10;
if(dentroRango >= valorMin && dentroRango <= valorMax) {
    console.log('Está dentro del rango');
} else {
    console.log('No está dentro del rango');
}

//ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = true;
if(vacaciones || diaDescanso) {
    console.log('El padre puede asistir');
} else {
    console.log('El padre no puede asistir');
}

//Operador ternario

let resultado2 = 3 > 2 ? 'Verdadero' : 'Falso';
console.log(resultado2);

let numero = 8;
resultado2 = numero % 2 == 0 ? 'Es PAR' : 'Es IMPAR';
console.log(resultado2);

//Convertir String a Number

let miNumero = '18x'; //Es un string
console.log(typeof miNumero);

let edad2 = Number(miNumero); // Number() es una función
console.log(typeof edad2); // Es un number
console.log(edad2);

//Función isNaN

//isNaN() => no es un número / is not a number (devuelve un resultado booleano)
if(isNaN(edad2)) {
    console.log('La variable no contiene solo números');
} else {
    if(edad2 >= 18) {
        console.log('Puede votar');
    } else {
        console.log('No puede votar');
    }
}

let resultado3 = edad2 >= 18 ? 'Puede votar' : 'No puede votar';
console.log(resultado3);
