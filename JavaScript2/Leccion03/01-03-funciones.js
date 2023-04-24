miFuncion(8, 2); //Esto se le conoce como hoisting

function miFuncion(a, b) {
    //console.log('Sumamos: ' + (a + b));
    return a + b;
};

//Llamando a la función
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una función de tipo expresión o anónima
let x = function(a, b) {return a + b}; //Necesita cierre con punto y coma
resultado = x(5, 6); //Al llamarla se pone la variable y parentesis
console.log(resultado);

//Funciones de tipo self y invoking
//Se llama a sí misma, no se puede volver a llamar
(function(a, b) {
    console.log('Ejecutando la función: ' + (a + b));
})(9,6);

console.log(typeof miFuncion);
function miFuncion2(a, b) {
    //Arguments se utiliza dentro de la función
    console.log(arguments);
    console.log(arguments.length);
};

miFuncion2(5, 7, 3, 6); //le pasamos los argumentos

//toString
let miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7);
console.log(resultado);

//Función tipo expresión
let sumar = function(a = 4, b = 8) {
    console.log(arguments[0]); //Muestra el parámetro de a
    console.log(arguments[1]); //Muestra el parámetro de b
    return a + b + arguments[2];
};
resultado = sumar(3, 2, 9);
console.log(resultado);

//Sumar todos los argumentos (concepto Hoisting) => llamar la función antes de ser creada
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo() {
    let suma = 0;
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}

//Tipos primitivos
let k = 10;
function cambiarValor(a) { //Paso por valor => la variable no sufre ningún cambio
    a = 20;
}
cambiarValor(k);
console.log(k);

//Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
};
console.log(persona);

function cambiarValorObjeto(p1) {
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
};

cambiarValorObjeto(persona);
console.log(persona);