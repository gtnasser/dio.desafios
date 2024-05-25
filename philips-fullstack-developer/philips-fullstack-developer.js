/*
* Bootcamp Philips Fullstack Developer You Are You
*/

// ----------------------------------------
// Desafios de Código Iniciais Js - Philips Developer

//
// 1 / 3 - Quantidade de Números Positivos
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
// ### 2 / 3 - Fases da Lua
//

let lines = gets().split('\n');

let line = lines.shift().split(" ");
let inicio = parseInt(line[0]);
let final = parseInt(line[1]);

if (final >= 0 && final <= 2) {
    print('nova');
} else if (final > inicio && final <= 96 ) {
    print('crescente');
} else if (final < inicio && final <= 96 ) {
    print('minguante');
} else {
    print('cheia');
}


//
// 3 / 3 - Álbum da Copa
//

// a função gets é implementada dentro do sistema para ler as entradas(inputs) dos dados
// Abaixo segue um exemplo de código que você pode ou não utilizar

const numTotal = parseInt(gets())
const numFigCompradas = parseInt(gets())
const setFig = new Set()

for (i=0; i<numFigCompradas; i++) {
  const fig = parseInt(gets())
  setFig.add(fig)
}

print(numTotal - setFig.size)


// ----------------------------------------
// Desafios de Código Intermediários Js - Philips Developer

//
// 1 / 3 - Idade em dias
//

let totalDeDias = parseInt(gets());

// Calcular a quantidade de anos inteiros em qtdAnos e o resto dos dias em total de dias
const qtdAnos = Math.trunc(totalDeDias / 365);
totalDeDias = totalDeDias % 365;

// Calcular a quantidade de meses inteiros em qtdAnos e o resto dos dias em total de dias
const qtdMeses = Math.trunc(totalDeDias / 30);
totalDeDias = totalDeDias % 30;

// Impressão do resultado usando interpolação de strings.
// Referência: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Template_literals
print(`${qtdAnos} ano(s)
       ${qtdMeses} mes(es)
       ${totalDeDias} dia(s)`);


//
// 2 / 3 - Ordenando Números Pares e Ímpares
//

let totalItems = parseInt(gets())
let pares = []
let impares = []

// carrega os valores separando em pares e impares

for (let i = 0; i < totalItems; i++) {
  let number = gets()
  if (number % 2 === 0){
    pares.push(number)
  }
  else {
    impares.push(number)
  }
}

// ordena o sitens do array utilizando sort()

pares.sort((a, b) => a-b)
impares.sort((a, b) => b-a)

// imprime os valores de cada array, um valor por linha
pares.map(m => print(m))
impares.map(m => print(m))


//
// 3 / 3 - Votação para Bobo da Corte
//

// carrega todos os votos

const numVotos = parseInt(gets());
var votos = new Array(numVotos);
for (let i = 0; i < numVotos; i++){
  votos[i] = parseInt(gets());
}

// cria um indicador assumindo que o primeiro inscrito tem a maior quantidade de votos

let primeiroInscrito = true;

// indentifica quantidade de votos do primeiro inscrito (Rafael)
// e tira esse voto da lista de votos

const votosPrimeiroInscrito = Number(votos.shift());

// filtra quantidade de votos maiores que o do primeiro inscrito

votos = votos.filter(votosOutroBobo =>
  votosOutroBobo > votosPrimeiroInscrito
)

// atualiza o indicador se existir quantidade de votos maior que o do primeiro

if (votos.length>0) {
  primeiroInscrito = false
}

// retorna se o primeiro inscrito tem a maior quantidade de votos

print(primeiroInscrito ? "S" : "N");