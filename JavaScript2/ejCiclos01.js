const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numero = 0;
let cuadrado = 0;

console.log("Ingrese un número: ");
rl.on('line', function(line){
    numero = parseInt(line.trim());
    if(numero >= 0) {
        cuadrado = Math.pow(numero, 2);
        console.log("El número " + numero + " elevado al cuadrado es: " + cuadrado);
        console.log("Ingrese otro número: ");
    } else {
        console.log("El programa ha finalizado por número negativo");
        rl.close();
    }
});
