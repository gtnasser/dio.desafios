Fundamentos Aritméticos em JavaScript

### 1 / 5 - Quantidade de Números Positivos
- Básico
- Princípios Básicos

#### Desafio
Crie um programa que leia 6 valores, os quais poderão ser negativos e/ou positivos. Em seguida, apresente a quantidade de valores positivos digitados.

#### Entrada
Você receberá seis valores, negativos e/ou positivos.

#### Saída
Exiba uma mensagem dizendo quantos valores positivos foram lidos. assim como é exibido abaixo no exemplo de saída. Não se esqueça de incluir na mensagem de saída o sufixo " valores positivos", conforme o exemplo abaixo:

Exemplo de Entrada | Exemplo de Saída
---|---
7<br>-5<br>6<br>-3.4<br>4.6<br>12|4 valores positivos

```js
let quantidadePositivos = 0;

for (let i = 0; i < 6; i++) {
  const valorInformadoPeloUsuario = gets();

  if (valorInformadoPeloUsuario>0) {
    quantidadePositivos++
  };
}

print(`${quantidadePositivos} valores positivos`);
```

---

### 2 / 5 - Exibindo Números Pares
- Básico
- Princípios Básicos

#### Desafios
Crie um programa que leia um número e mostre os números pares até esse número, inclusive ele mesmo.

#### Entrada
Você receberá 1 valor inteiro N, onde N > 0.

#### Saída
Exiba todos os números pares até o valor de entrada, sendo um em cada linha. 

Exemplo de Entrada|Exemplo de Saída
---|---
6|2<br>4<br>6

```js
// Valor informado pelo usuário "N"
let n = parseInt(gets());

// TODO Inclua a condição de parada adequada. 
// Dica: note que o contador "i" é incrementado de 2 em 2 (sempre indo para o próximo par).
for (let i = 2; i<=n ; i+=2) {
  print(i);
}
```

---

### 3 / 5 - Análise de Números
- Básico
- Princípios Básicos

#### Desafio
Você deve fazer a leitura de 5 valores inteiros. Em seguida mostre quantos valores informados são pares, quantos valores informados são ímpares, quantos valores informados são positivos e quantos valores informados são negativos. Considere que o número zero é positivo, mas não pode ser considerado como positivo ou negativo.

#### Entrada
Você receberá 5 valores inteiros.

#### Saída
Exiba a mensagem conforme o exemplo de saída abaixo, sendo uma mensagem por linha e não esquecendo o final de linha após cada uma.

Exemplo de Entrada | Exemplo de Saída
---|---
-5<br>0<br>-3<br>-4<br>12 | 3 par(es)<br>2 impar(es)<br>1 positivo(s)<br>3 negativo(s)

```js
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
```

---

### 4 / 5 - Contagem de Cédulas
- Intermediário
- Princípios Básicos

#### Desafio
Faça a leitura de um valor inteiro. Em seguida, calcule o menor número de notas possíveis (cédulas) onde o valor pode ser decomposto. As notas que você deve considerar são de 100, 50, 20, 10, 5, 2 e 1. Na sequência mostre o valor lido e a relação de notas necessárias.

#### Entrada
Você receberá um valor inteiro N (0 < N < 1000000).

#### Saída
Exiba o valor lido e a quantidade mínima de notas de cada tipo necessárias, seguindo o exemplo de saída abaixo. Após cada linha deve ser imprimido o fim de linha.
 
Exemplo de Entrada|Exemplo de Saída
---|---
576|576<br>5 nota(s) de R$ 100,00<br>1 nota(s) de R$ 50,00<br>1 nota(s) de R$ 20,00<br>0 nota(s) de R$ 10,00<br>1 nota(s) de R$ 5,00<br>0 nota(s) de R$ 2,00<br>1 nota(s) de R$ 1,00
11257|11257<br>112 nota(s) de R$ 100,00<br>1 nota(s) de R$ 50,00<br>0 nota(s) de R$ 20,00<br>0 nota(s) de R$ 10,00<br>1 nota(s) de R$ 5,00<br>1 nota(s) de R$ 2,00<br>0 nota(s) de R$ 1,00
503|503<br>5 nota(s) de R$ 100,00<br>0 nota(s) de R$ 50,00<br>0 nota(s) de R$ 20,00<br>0 nota(s) de R$ 10,00<br>0 nota(s) de R$ 5,00<br>1 nota(s) de R$ 2,00<br>1 nota(s) de R$ 1,00

```js
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
```

---

### 5 / 5 - Consumo Médio do Automóvel
- Básico
- Princípios Básicos

#### Desafio
Você deve calcular o consumo médio de um automóvel onde será informada a distância total percorrida (em Km) e o total de combustível consumido (em litros).

#### Entrada
Você receberá dois valores: um valor inteiro X com a distância total percorrida (em Km), e um valor real Y que representa o total de combustível consumido, com um dígito após o ponto decimal.

#### Saída
Exiba o valor que representa o consumo médio do automóvel (3 casas após a vírgula), incluindo no final a mensagem "km/l".

Exemplo de Entrada | Exemplo de Saída
---|---
500<br>35.0 | 14.286 km/l
2254<br>124.4 | 18.119 km/l
4554<br>464.6 | 9.802 km/l

```js
let x = parseInt(gets());
let y = parseFloat(gets());

// TODO Realize o cálculo do consumo médio do automóvel.
const consumoMedio = x / y;

print(`${consumoMedio.toFixed(3)} km/l`);
```

