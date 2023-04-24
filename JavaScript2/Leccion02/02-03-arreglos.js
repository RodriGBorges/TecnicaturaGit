//Creación de Array o arreglos
// let autos = new Array('Ferrari', 'Renault', 'BMW'); esta es la sintaxis vieja

const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

//recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for (let i = 0; i < autos.length; i++) {
    console.log(`${i}: ${autos[i]}`);
}

//Modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); //Se agrega al final del arreglo
console.log(autos);

//Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

autos[6] = 'Renault'; //cuidado con dejar espacios vacíos en el array
console.log(autos);

//Cómo preguntar si es un array o arreglo
console.log(Array.isArray(autos)); //Devuelve booleano

console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase array