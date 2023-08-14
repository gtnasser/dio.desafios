## Bootcamp Philips Fullstack Developer | You Are You<br>Desafios de Código Intermediários Js - Philips Developer

### 1 / 3 - Idade em dias
- Intermediário
- Princípios Básicos

#### Desafio
Você terá o desafio de ler um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

#### Entrada
O arquivo de entrada contém um valor inteiro.

#### Saída
Imprima a saída conforme exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
--- | ---
400 | 1 ano(s)<br>1 mes(es)<br>5 dia(s)
800 | 2 ano(s)2 mes(es)<br>10 dia(s)
30 | 0 ano(s)<br>1 mes(es)<br>0 dia(s)


```js
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
```

---

### 2 / 3 - Ordenando Números Pares e Ímpares
- Básico
- Estrutura de Dados

#### Desafio
Crie um programa onde você receberá valores inteiros não negativos como entrada.

Ordene estes valores de acordo com o seguinte critério:
* Primeiro os Pares
* Depois os Ímpares
Você deve exibir os pares em ordem crescente e na sequência os ímpares em ordem decrescente.

#### Entrada
A primeira linha de entrada contém um único inteiro positivo **N** (1 < **N** < 10000) Este é o número de linhas de entrada que vem logo a seguir. As próximas **N** linhas terão, cada uma delas, um valor inteiro não negativo.

#### Saída
Exiba todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo de saída abaixo.

Exemplo de Entrada | Exemplo de Saída
--- | ---
10<br>4<br>32<br>34<br>543<br>3456<br>654<br>567<br>87<br>6789<br>98/| 4<br>32<br>34<br>98<br>654<br>3456<br>6789<br>567<br>543<br>87


```js

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
pares.map(m => console.log(m))
impares.map(m => console.log(m))
```

---

### 3 / 3 - Votação para Bobo da Corte
- Intermediário
- Princípios Básicos

#### Desafio
O Império dos Artificialistas é governado por um generoso Monarca. A personalizada do Monarca é conhecida por todo o mundo, principalmente por sua forma como valoriza o bom humor de seu povo, que tem o direito a diversidade cultura. Um dos destaques fica a cargo do bobo da corte, eleito anualmente em um concurso internacional.

O jovem Rafael é um comediante promissor, que sonha em se tornar o bobo da corte nesse grande concurso. Para isso, ele vem se preparando com muita dedicação há vários meses. Chegada a época do concurso do bobo da corte, um total de N candidatos se inscreveram, e como Rafael sabia que ser o primeiro candidato a se inscrever torna-se critério de desempate, foi o primeiro a se inscrever! O concurso dará apenas 5 minutos para cada participante e no final cada cidadão dará seu voto ao futuro bob da corte que achar melhor.

Sendo assim, após a votação, resta apenas apurar os resultados, que será realizado por urna eletrônica com N inteiros, correspondentes ao total de votos em cada candidato, ordenado pela ordem de inscrição. Sua missão é determinar se o jovem Rafael foi eleito ou não.

#### Entrada
A primeira linha da entrada contém um inteiro N (2 ≤ N ≤ 104). As N linhas seguintes conterão N inteiros positivos v 1 , . . . , vN , um em cada linha, correspondentes ao número de votos recebido por cada um dos candidatos, em ordem de inscrição. Sabendo-se que a população total é de 100.000 pessoas, o número total de votos não será superior a este valor.

#### Saída
Seu programa produzirá apenas uma linha contendo o caractere ‘S’ se o jovem Rafael foi o eleito para bobo da corte, ou o caractere ‘N’ caso contrário.

Exemplos de Entrada | Exemplos de Saída
3<br>1000<br>1000<br>1000 | S
5<br>1<br>2<br>3<br>4<br>5 | N


```js
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
```