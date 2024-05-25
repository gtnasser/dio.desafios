/*
* Bootcamp Potência Tech Angular Developer - Powered by iFood
*/

// @ts-nocheck

// ----------------------------------------
// Exercite sua Lógica com Desafios de Código em Javascript

//
// Tempo Estimado de Entrega
//

const nomeRestaurante = gets();
const tempoEstimadoEntrega = parseInt(gets());

const mensagem = `O restaurante ${nomeRestaurante} entrega em ${tempoEstimadoEntrega} minutos.`

print(mensagem)


//
//Calcular o Preço Final de um Pedido
//

const valorHamburguer = parseFloat(gets());
const quantidadeHamburguer = parseInt(gets());
const valorBebida = parseFloat(gets());
const quantidadeBebida = parseInt(gets());
const valorPago = parseFloat(gets());

let precoFinal = valorHamburguer * quantidadeHamburguer + valorBebida * quantidadeBebida
let troco = valorPago - precoFinal

print(`O preço final do pedido é R$ ${precoFinal.toFixed(2)}. Seu troco é R$ ${troco.toFixed(2)}.`)


//
// Ganhe uma Sobremesa Especial!
//

const valorPedido = parseInt(gets());

let mensagem = ''
if (valorPedido >= 50.00) {
  mensagem = 'Parabens, você ganhou uma sobremesa gratis!'
} else {
  mensagem = 'Que pena, você nao ganhou nenhum brinde especial.'
}

print(`${mensagem}`)


//
// Gerenciamento de Pedidos de Comida Online
//

function calcularValorTotal(n, pedidos, cupom) {
  let total = 0;
  for (let i = 0; i < n; i++) {
    let [nome, valor] = pedidos[i].split(' ');
    valor = parseFloat(valor);
    total += valor;
  }

  if (cupom === '10%') {
    total *= 0.9
  } else if (cupom === '20%') {
    total *= 0.8
  }

  return total.toFixed(2);
}

//Recupera os valores de entrada, criando um array para os pedidos:
const n = parseInt(gets());
const pedidos = [];
for (let i = 0; i < n; i++) {
  pedidos.push(gets());
}
const cupom = gets();

const valorTotal = calcularValorTotal(n, pedidos, cupom)

print(`Valor total: ${valorTotal}`)


//
// Identificando Pedidos Veganos
//

const numPedidos = parseInt(gets());

for (let i = 1; i <= numPedidos; i++) {
  const prato = gets();
  const calorias = parseInt(gets());
  const ehVegano = gets().toLowerCase() === 's';

  ehVeganoTexto = ''
  if (ehVegano) {
    ehVeganoTexto = 'Vegano'
  } else {
    ehVeganoTexto = 'Nao-vegano'
  }

  print(`Pedido ${i}: ${prato} (${ehVeganoTexto}) - ${calorias} calorias`)
}
