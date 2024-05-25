/*
* Bootcamp HTML Web Developer
*/
// @ts-nocheck comment

// ----------------------------------------
// Introdução a Programação com JavaScript

//
// 1 / 3 - Visita na Feira
//
let line = gets().split(" ");
let A = parseInt(line[0]);
let B = parseInt(line[1]);
let total = A+B; // Altere o valor da variável com o cálculo esperado
print("X = " + total);


//
// 2 / 3 - Multiplicação Simples
//

let valor1 = parseInt(gets());
let valor2 = parseInt(gets());
let total = valor1 * valor2; // Altere o valor da variável com o cálculo esperado
print("PROD = " + total);


//
// 3 / 3 - Folha de Pagamento
//

let valor1 = parseInt(gets());
let valor2 = parseInt(gets());
let valor3 = parseFloat(gets());

let salary = valor2 * valor3;
print("NUMBER = " + valor1);
print("SALARY = U$ " + salary.toFixed(2));

// ----------------------------------------
// Fundamentos Aritméticos em JavaScript

//
// 1 / 5 - Quantidade de Números Positivos
//

let quantidadePositivos = 0;

for (let i = 0; i < 6; i++) {
  const valorInformadoPeloUsuario = gets();

  if (valorInformadoPeloUsuario>0) {
    quantidadePositivos++
  };
}

print(`${quantidadePositivos} valores positivos`);


//
// 2 / 5 - Exibindo Números Pares
//

// Valor informado pelo usuário "N"
let n = parseInt(gets());

// TODO Inclua a condição de parada adequada.
// Dica: note que o contador "i" é incrementado de 2 em 2 (sempre indo para o próximo par).
for (let i = 2; i<=n ; i+=2) {
  print(i);
}


//
// 3 / 5 - Análise de Números
//

let valoresPares = 0;
let valoresImpares = 0;
let valoresPositivos = 0;
let valoresNegativos = 0;

for (var i = 0; i < 5; i++) {
  const valorInformadoPeloUsuario = parseInt(gets());

  // TODO: Complete os espaços em branco com uma solução possível para o problema.
  if ( valorInformadoPeloUsuario % 2 == 0 ) {
    valoresPares++;
  } else {
    valoresImpares++;
  }

  if (valorInformadoPeloUsuario > 0) {
    valoresPositivos++;
  } else if (valorInformadoPeloUsuario < 0) {
    valoresNegativos++;
  }

}

print(`${valoresPares} par(es)`);
print(`${valoresImpares} impar(es)`);
print(`${valoresPositivos} positivo(s)`);
print(`${valoresNegativos} negativo(s)`);


//
// 4 / 5 - Contagem de Cédulas
//

let n = parseInt(gets());
let quantidadeNotas = 0;
let cedulas = [100,50,20,10,5,2,1];

// Função responsável por contar as notas a partir de um valor.
function contaNotas(valor){
  quantidadeNotas = parseInt(n/valor);

  // TODO Subtraia de "n" a "quantidadeNotas" multiplicada por seu respectivo "valor" (parâmetro).
  n -= quantidadeNotas * valor;

  print(`${quantidadeNotas} nota(s) de R$ ${valor},00`);
}

print(n);

for(let cedula in cedulas){
    if (parseInt(cedulas[cedula])>0) contaNotas(cedulas[cedula]);
}


//
// 5 / 5 - Consumo Médio do Automóvel
//

let x = parseInt(gets());
let y = parseFloat(gets());

// TODO Realize o cálculo do consumo médio do automóvel.
const consumoMedio = x / y;

print(`${consumoMedio.toFixed(3)} km/l`);
