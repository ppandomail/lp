function calcularArea(base, altura) {
  let area = (base * altura) / 2;
  return area;
}

let base = parseFloat(prompt("Ingrese la base del triángulo: "));
let altura = parseFloat(prompt("Ingrese la altura del triángulo: "));
let area = calcularArea(base, altura);
alert("El área del triángulo es: " + area);