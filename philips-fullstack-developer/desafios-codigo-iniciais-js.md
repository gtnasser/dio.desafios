## Bootcamp Philips Fullstack Developer | You Are You<br>Desafios de Código Iniciais Js - Philips Developer

### 1 / 3 - Quantidade de Números Positivos
- Básico
- Princípios Básicos

#### Desafio
Crie um programa que leia 6 valores, os quais poderão ser negativos e/ou positivos. Em seguida, apresente a quantidade de valores positivos digitados.

#### Entrada
Você receberá seis valores, negativos e/ou positivos.

#### Saída
Exiba uma mensagem dizendo quantos valores positivos foram lidos. assim como é exibido abaixo no exemplo de saída. Não se esqueça de incluir na mensagem de saída o sufixo " valores positivos", conforme o exemplo abaixo:

Exemplo de Entrada|Exemplo de Saída
---|---
7<br>-5<br>6<br>-3.4<br>4.6<br>12<br> | 4 valores positivos

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

### 2 / 3 - Fases da Lua
- Básico
- Ad-Hoc

#### Desafio
Jade ganhou de presente de aniversário um telescópio e ficou muito feliz, pois adora olhar a lua à noite. Ela sempre foi uma estudante muito boa, e só analizando a lua por duas noites seguidas, já consegue identificar as mudanças que ocorreram na iluminação e o percentual aproximado da lua que está iluminada.

Você, que é amigo da Jade e estuda Computação, resolveu fazer um pequeno programa que, baseado nesta avaliação que ela fez nas duas últimas noites, informa a fase na qual a lua se encontra. Se a porção visível da lua no momento estiver entre 0 e 2%, por exemplo, é lua nova, se for entre 3 e 96% é lua crescente, se for entre 97 e 100% é lua cheia e se for entre 96 e 3% (diminuindo) é lua minguante.

#### Entrada
A entrada é composta por uma única linha contendo dois valores inteiros. O primeiro valor corresponde ao percentual observado por Jade na noite de dois dias atrás. O segundo valor corresponde ao percentual observado por jade na noite anterior.

#### Saída
Baseado nos dois percentuais observados por Jade, imprima na tela a fase na qual a lua se encontrava na noite anterior, conforme o exemplo abaixo. Não esqueça de imprimir o caractere de fim de linha após a saída :).

Exemplo de Entrada|Exemplo de Saída
---|---
0 2|nova
2 3|crescente
99 97|cheia
97 94|minguante
30 35|crescente

Contest Oficial de Aquecimento da Olimpíada Brasileira de Informática, Fase 2, 2015

```js
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
```

---

### 3 / 3 - Álbum da Copa
- Básico
- Princípios Básicos

#### Desafio
A Copa do Mundo de Futebol é um dos maiores eventos esportivos do Planeta Terra, e o álbum de figurinhas oficial é sempre um grande sucesso entre os amantes dessa competição. O álbum contém espaços numerados de 1 a N para colar as figurinhas; cada figurinha, também numerada de 1 a N, é uma pequena foto de um jogador de uma das seleções que jogará a Copa do Mundo. O objetivo é colar todas as figurinhas nos respectivos espaços no álbum, de modo a completar o álbum, ou seja, não deixar nenhum espaço sem a correspondente figurinha.

As figurinhas são vendidas em envelopes fechados, de forma que o comprador não sabe quais figurinhas está comprando, e pode ocorrer de comprar uma figurinha que ele já tenha colado no álbum.

Para ajudar os usuários, a empresa responsável pela venda do álbum e das figurinhas quer criar um aplicativo que permita gerenciar facilmente as figurinhas que faltam para completar o álbum e está solicitando a sua ajuda.

Dados o número total de espaços e figurinhas do álbum, e uma lista das figurinhas já compradas (que pode conter figurinhas repetidas), o seu desafio é determinar quantas figurinhas faltam para completar o álbum.

#### Entrada
A primeira linha contém um inteiro N (1 ≤ N ≤ 100) indicando o número total de figurinhas e espaços no álbum. A segunda linha contém um inteiro M (1 ≤ M ≤ 300) indicando o número de figurinhas já compradas. Cada uma das M linhas seguintes contém um número inteiro X (1 ≤ X ≤ N) indicando uma figurinha já comprada.

#### Saída
Seu programa deve produzir uma única linha contendo um inteiro representando o número de figurinhas que falta para completar o álbum.

Exemplos de Entrada|Exemplos de Saída
---|---
10<br>3<br>5<br>8<br>3 | 7
3<br>4<br>2<br>1<br>3<br>3 | 0

```js
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
```
