let numero = parseInt(prompt("Ingrese un número: "));
let factorial = 1
for (let i = 1; i <= numero; i++) {
  factorial *= i;
}
alert("El factorial de " + numero + " es: " + factorial);