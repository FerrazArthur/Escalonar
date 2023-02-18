### Fell free to use as you want and to send me your feedback! 

## INTRODUCTION

<p>Do you ever had to make or correct an matrix scaling process by hand, just to notice some mistake in the process and wished you have a program that, in addition to show you the scaled system, you could also see the step-by-step process? what if you could had total control over the process? That's this project's intention!</p>
<p>With this algorithm, you'll be able to swap collumns, multiply lines by a scalar, swap lines or collumns and some more operations that we usually do by hand to reduce the number of steps it'll take to scale the matrix</p>

## INTRODUÇÃO
<p>Alguma vez ja precisou realizar ou corrigir uma escalonação de matriz na mão, percebeu algum erro no processo e desejou ter um programa que, além de mostrar a matriz escalonada, te mostrasse cada passo realizado? E se você tivesse total poder sobre o processo? Essa é a proposta desse projeto!</p>
<p>Com esse algoritmo você poderá trocar colunas, multiplicar linhas por escalar, trocar linhas ou colunas e mais qualquer outra operação que geralmente fazemos na mão, para reduzir o número de passos para escalonar a matriz!</p>

##

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
<p>For each line in order, use option '2' to define a pivot then use option '4' in all other lines to reduze the collumns bellow pivot to zero;</p>
<p>Repeat this processes line by line until you reach the end</p>
<p>Once done, you'll have a identity matriz 'A' and the other matriz(vector) is going to be the 'x' values to satisfy this system.</p>
<p>Note: when you use 'swap collumns', you must keep in mind that you also swap 'b' and 'x' order. So i wrote a register of collumns change.</p>
<p>Note, THIS CODE IS FOR LINEAR SISTEMS like 'Ax=b' so A MUST be NxN(square matriz) and 'b' must be a single line with N elements.</p>
    
## (PT)Como escalonar a matriz passo a passo:
<p>Para cada linha(começe em ordem), utilize a opção '2' para definir um pivo, então use a opção 4 nas demais linhas para zerar as colunas abaixo do pivo</p>
<p>Repita esse processo a cada linha subsequente</p>
<p>Ao fim desse processo, você terá uma matriz identidade 'A' e uma matriz com os coeficientes do vetor 'x'( em 'Ax = b') que satisfaça o sistema</p>
<p>Nota: Ao utilizar a opção para trocar colunas, você também estará trocando a ordem dos coeficientes nas matrizes 'b' e 'x'</p>
<p>Nota: Esse algoritmo é para sistemas lineares na forma 'Ax=b', Então é preciso que A seja uma matriz quadrada(NxN) e 'b' precisa ser uma matriz linha com N elementos.</p>

##
<p>to send your feedback, contact me on
arthursnc@gmail.com</p>
<p>Arthur Ferraz</p>
