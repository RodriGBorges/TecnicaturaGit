let x = 10; //variable de tipo primitiva
console.log(x.length);

console.log("Tipos primitivos");
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Jay',
    email: 'cjay@gmail.com',
    edad: 38,
    idioma: 'es',
    get lang() {
        return this.idioma.toUpperCase();
    },
    set lang(lang) {
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function() { //Método o función en JavaScript
        return this.apellido + " " + this.nombre;
    },
    get nombreEdad() { //Este es el método get
        return "El nombre es: "+ this.nombre + ", edad: " + this.edad; 
    },
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5491122334455';
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");

console.log(persona['apellido']); //Accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in");

//for in => accedemos al objeto como si fuera un arreglo
for(propiedad in persona) {
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log("Cambiamos y eliminamos un error");
persona.apellida = 'Perez'; //Cambiamos dinámicamente un valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Número 1: La más sencilla, concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre + ', ' + persona.apellido);

//Número 2: A través del ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for (const nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad]);
}

//Número 3: La función Object.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Número 4: Utilizaremos el método JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona)
console.log(personaString);

console.log("Comenzamos a utilizar el método get: ");
console.log(persona.nombreEdad);

console.log('Comenzamos a utilizar el método get para idiomas: ');
persona.lang = 'en'
console.log(persona.lang);

function Persona3(nombre, apellido, email) { //Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + " " + this.apellido;
    }
}

let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';
padre.telefono = '54123456789'; //Propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto());

let madre = new Persona3('Laura', 'Nuñez', 'lnuñez@gmail.com')
console.log(madre);
console.log(madre.telefono); //La propiedad no está definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//caso número 1
let miObjeto = new Object(); //Esta es una opción formal

//caso número 2
let miObjeto2 = {}; //Esta opción es breve y recomendada


//caso String 1
let miCadena = new String('Hola'); //Sintaxis formal

//caso String 2
let miCadena2 = 'Hola'; //Esta es la sintaxis simplificada y recomendada


//caso con números 1
let miNumero = new Number(1); //Es formal no recomendable

//caso con números 2
let miNumero2 = 1; //Sintaxis recomendada


//caso boolean 1
let miBoolean1 = new Boolean(false); //Formal

//caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada


//caso Arreglos 1
let miArreglo1 = new Array(); //Formal

//caso Arreglos2
let miArreglo2 = []; //Sintaxis recomendada


//caso function 1
let miFuncion1 = new function(){}; //Todo después de new es considerado objeto

//caso function 2
let miFuncion2 = function(){}; //Notación simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = '987654321';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '54987654321';
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono) {
        return `${titulo}: ${this.nombre} ${this.apellido} ${telefono}`;
        //return `${this.nombre} ${this.apellido}`;
    }
}

let persona5 = {
    nombre: 'Ramon',
    apellido: 'Rodriguez'
}

console.log(persona4.nombreCompleto2('Lic.', '2323232323'));
//console.log(persona4.nombreCompleto2());
console.log(persona4.nombreCompleto2.call(persona5, 'Ing', '123123123'));

//Método Apply

let arreglo = ['Ing.', '54231255385']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));