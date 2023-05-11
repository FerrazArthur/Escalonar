# Matrix Scaling Tool: Step-by-Step Operations for Precise Control
 

### INTRODUCTION

Have you ever needed to perform or correct matrix scaling by hand, noticed an error in the process, and wished for a program that not only showed the scaled matrix, but also showed each step performed? And what if you had total control over the process? That is the proposal of this project!

With this algorithm, you can swap columns, multiply rows by a scalar, swap rows or columns, and perform any other operations that we usually do by hand, to reduce the number of steps to scale the matrix!

###### ABOUT THE APP

Matrix scaling is a mathematical process that aims to simplify the solution of linear equation systems. Basically, it consists of applying a series of operations (such as swapping rows or columns, multiplying a row by a scalar, etc.) to the matrix that represents the system until it reaches a simplified form, in which the unknowns can be easily solved. The goal of our app is to allow anyone to perform this process quickly and accurately, without relying on manual calculations.

###### WHO CAN BENEFIT FROM IT

This app can be useful for math, physics, engineering, and other students who use linear equation systems in their calculations. For example, imagine a student needs to solve an equation system to determine the forces acting on a mechanical system. The matrix scaling process can be quite laborious, especially if there are many equations involved. With our app, this student can simplify this process and obtain the solution more quickly and accurately.

## Escalonador de Matrizes com Controle de Processo Passo a Passo

### INTRODUÇÃO
Alguma vez ja precisou realizar ou corrigir uma escalonação de matriz na mão, percebeu algum erro no processo e desejou ter um programa que, além de mostrar a matriz escalonada, te mostrasse cada passo realizado? E se você tivesse total poder sobre o processo? Essa é a proposta desse projeto!

Com esse algoritmo você poderá trocar colunas, multiplicar linhas por escalar, trocar linhas ou colunas e mais qualquer outra operação que geralmente fazemos na mão, para reduzir o número de passos para escalonar a matriz!

###### SOBRE O APLICATIVO
O escalonamento de matriz é um processo matemático que visa simplificar a resolução de sistemas de equações lineares. Basicamente, ele consiste em aplicar uma série de operações (como trocar linhas ou colunas, multiplicar uma linha por um escalar, etc.) à matriz que representa o sistema até que ela atinja uma forma simplificada, em que as incógnitas possam ser facilmente resolvidas. O objetivo do nosso aplicativo é permitir que qualquer pessoa possa realizar esse processo de forma rápida e precisa, sem depender de cálculos manuais.

###### QUEM PODE SE BENEFICIAR DELE 
Esse aplicativo pode ser útil para estudantes de matemática, física, engenharia e outras áreas que utilizam sistemas de equações lineares em seus cálculos. Por exemplo, imagine que um estudante precise resolver um sistema de equações para determinar as forças que atuam em um sistema mecânico. O processo de escalonamento de matriz pode ser bastante trabalhoso, principalmente se houver muitas equações envolvidas. Com o nosso aplicativo, esse estudante pode simplificar esse processo e obter a solução de forma mais rápida e precisa.

## ENGLISH MENU:
    1-Multiply line by constant
    2-Transform first element non 0 of line into pivot
    3-Add to a line the multiple of another line
    4-Swap lines
    5-Swap collumns
    6-Show system
    7-Show registry of swap's in collumns
    9-Change system
    10-Exit
##
<p>To insert a matrix, use a ',' to separate elements by collumn and a ';' to separate the lines</p>
<p>Para inserir a matriz, utilize ',' para separar elementos por colunas e ';' para separar as linhas</p>
## Example

    >a, b, c;d, e, f; g,h,i
<p>this will create the following matriz</p>

    a b c
    d e f
    g h i

## (EN)Quick advise in how to use:

- For each line in order, use option '2' to define a pivot then use option '4' in all other lines to reduze the collumns bellow pivot to zero;

- Repeat this processes line by line until you reach the end.

Once done, you'll have a identity matriz 'A' and the other matriz(vector) is going to be the 'x' values to satisfy this system.

Note: when you use 'swap collumns', you must keep in mind that you also swap 'b' and 'x' order. So i wrote a register of collumns change.

Note, THIS CODE IS FOR LINEAR SISTEMS like 'Ax=b' so A MUST be NxN(square matriz) and 'b' must be a single line with N elements.
    
## (PT)Como escalonar a matriz passo a passo:

- Primeiro, escolha a opção '2' para a primeira linha, definindo um pivo e, em seguida, a opção '4' usando todas as outras linhas;

- Repita esse processo a cada linha subsequente.

Ao fim desse processo, você terá uma matriz identidade 'A' e uma matriz com os coeficientes do vetor 'x'( em 'Ax = b') que satisfaça o sistema

Nota: Ao utilizar a opção para trocar colunas, você também estará trocando a ordem dos coeficientes nas matrizes 'b' e 'x'

Nota: Esse algoritmo é para sistemas lineares na forma 'Ax=b', Então é preciso que A seja uma matriz quadrada(NxN) e 'b' precisa ser uma matriz linha com N elementos.


### Fell free to use as you want and to send me your feedback! 

to send your feedback, contact me on

arthursnc@gmail.com

Arthur Ferraz
