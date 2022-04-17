## Bootcamp Eduzz Fullstack Developer<br>Desafios iniciais em JavaScript

### 1 / 3 - Dividindo X por Y
- Básico
- Princípios Básicos

#### Desafio
Você terá o desafio de escrever um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível, mostre a mensagem “divisao impossivel” para os valores em questão.

#### Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

#### Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Exemplo de Entrada | Exemplo de Saída
--- | ---
3<br>3 -2<br>-8 0<br>0 8<br>|-1.5<br>divisao impossivel<br>0.0

```js
let limit = parseInt(gets());
for (let i = 0; i < limit; i++) {
    let line = gets().split(" ");
    let X = parseInt(line[0]);
    let Y = parseInt(line[1]);
    if (Y == 0) {
        console.log("divisao impossivel");
    } else {
        let divisao = parseFloat(X / Y).toFixed(1); 
        console.log(divisao);
    }
}
```

---

### 2 / 3 - Distância
- Básico
- Princípios Básicos

#### Desafio
Duas motos (X e Y) partem em uma mesma direção. A moto X sai com velocidade constante de 60 Km/h e a moto Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) a moto Y consegue se distanciar 30 quilômetros da moto X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

O seu desafio é ler a distância (em Km) e calcular quanto tempo leva (em minutos) para a moto Y tomar essa distância da outra moto.

#### Entrada
O arquivo de entrada contém um número inteiro K que representa a quantidade de quilômetro que que a moto Y deve estar da moto X.

#### Saída
Imprima o tempo necessário para a moto Y ficar com a quantidade K de quilômetro da moto X, seguido da mensagem " minutos".

Exemplo de Entrada | Exemplo de Saída
--- | ---
30 | 60 minutos
110 | 220 minutos

```js
let quilometros = parseInt(gets());
let minutos = quilometros * 60 / (90-60);
console.log(minutos + " minutos");
```

---

### 3 / 3 - Quanta Mandioca?
- Intermediário
- Princípios Básicos

#### Desafio
Os meses de Junho e Julho são tradicionalmente conhecidos por todo Brasil por suas festas típicas, e para o grupo de amigos da Marlene não é diferente, toda segunda quinzena do mês de Julho ela e seus amigos se reunem para tradicional mandiocada! Na festiva sempre se reúnem na casa da Marlene, o Chico, o Beto, o Bernardo, a Marina e a Iara. E como não poderia ser diferente o prato principal dessa reunião é a mandioca. Cada um deles come de uma a dez porções de mandioca e eles sempre avisam a Marlene com antecedência a respeito de quantas porções irão comer nesse dia. O tamanho da porção de cada um é diferente, mas sempre são os mesmos. As porções são as seguintes (em gramas):

O Chico come 300

O Bento come 1500

O Bernardo come 600

A Marina 1000

A Iara come 150

Marlene por sua vez sempre come 225 gramas de mandioca. Cansada de todo ano ter que calcular quanta mandioca preparar ela te desafiou para escrever um programa que informe quanta mandioca deve ser preparada em gramas.

#### Entrada
A entrada consiste de 5 inteiros cada um representando as porções que os convidados de dona Chica vão consumir. O primeiro inteiro representa as porções do Chico, o segundo do Bento, o terceiro do Bernardo, o quarto da Marina e o quinto a da Iara.

#### Saída
A saída consiste de um único inteiro que representa quanta mandioca Marlene deve preparar em gramas.
 
Exemplos de Entrada | Exemplos de Saída
--- | ---
1<br>1<br>1<br>1<br>1 | 3775
2<br>2<br>2<br>2<br>2 | 7325

```js
let chico = 300 * parseInt(gets());
let bento = 1500 * parseInt(gets());
let bernardo = 600 * parseInt(gets());
let marina = 1000 * parseInt(gets());
let iara = 150 * parseInt(gets());
let marlene = 225;
let total =  chico+bento+bernardo+marina+iara+marlene ; 

print(total);
```
