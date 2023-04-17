//While
let contador = 0;
while (contador < 3) {
    console.log(contador);
    contador++;
}
console.log('Fin del ciclo while');

//Do while
let conteo = 0;
do {
    console.log(conteo);
    conteo++;
} while (conteo < 3);
console.log('Fin del cilo do while');

//For
for (let contado = 0; contado < 3; contado++) {
    console.log(contado);
}
console.log('Fin del ciclo for');

//Palabra reservada break
for (let contando = 0; contando <= 10; contando++) {
    if(contando %2 === 0) {
        console.log(contando);
        break;
    }
}
console.log('Termina el ciclo al encontrar el primer par');

//Palabra continue
for (let contando = 0; contando <= 10; contando++) {
    if(contando %2 !== 0) {
        continue;
    }
    console.log(contando);
}
console.log('Termina el ciclo');

// Etiquetas Labels