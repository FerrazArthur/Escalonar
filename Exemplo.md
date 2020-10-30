# inserção de dados:
## -----exemplo----

    Insira a matriz A:
    4, 23, 12, 32;-43, 2, 53, 3;-4, -2, -1, 2;42, 32,-4,12
    Insira a matriz b:
    42, -03, -45, 32

    linha  1                 4.0                 23.0                 12.0                 32.0 |                42.0
    linha  2               -43.0                  2.0                 53.0                  3.0 |                -3.0
    linha  3                -4.0                 -2.0                 -1.0                  2.0 |               -45.0
    linha  4                42.0                 32.0                 -4.0                 12.0 |                32.0

## ----fim----

# Resolução do sistema:

# Primeiro passo:Transformar primeiro elemento não zero da linha 1 em pivo unitário

## -----exemplo----

    escolha uma opção: 2
    
    linha  1                 4.0                 23.0                 12.0                 32.0 |                42.0
    linha  2               -43.0                  2.0                 53.0                  3.0 |                -3.0
    linha  3                -4.0                 -2.0                 -1.0                  2.0 |               -45.0
    linha  4                42.0                 32.0                 -4.0                 12.0 |                32.0
    
    Selecione a linha: 1 
    
    linha  1                 1.0                 5.75                  3.0                  8.0 |                10.5
    linha  2               -43.0                  2.0                 53.0                  3.0 |                -3.0
    linha  3                -4.0                 -2.0                 -1.0                  2.0 |               -45.0
    linha  4                42.0                 32.0                 -4.0                 12.0 |                32.0
    
    Valor da linha 1 e coluna 1 foi multiplicada pelo seu inverso

## ----fim----

# Segundo passo: Zerar todos os elementos na coluna onde o pivô esta. Para isso utilizaremos a opção 4:

## -----exemplo----

    Selecione a linha que deseja zerar:2
    Selecione a linha do pivô:1

    linha  1                 1.0                 5.75                  3.0                  8.0 |                10.5
    linha  2                 0.0               249.25                182.0                347.0 |               448.5
    linha  3                -4.0                 -2.0                 -1.0                  2.0 |               -45.0
    linha  4                42.0                 32.0                 -4.0                 12.0 |                32.0
    
    Os elementos da linha 2 fram substraidos pelo valor que havia na linha 2 e coluna 1

## ----fim----

# Repita o processo para as demais linhas:

## -----exemplo----

    Selecione a linha que deseja zerar:3
    Selecione a linha do pivô:1
    
    linha  1                 1.0                 5.75                  3.0                  8.0 |                10.5
    linha  2                 0.0               249.25                182.0                347.0 |               448.5
    linha  3                 0.0                 21.0                 11.0                 34.0 |                -3.0
    linha  4                42.0                 32.0                 -4.0                 12.0 |                32.0
    
    Os elementos da linha 3 fram substraidos pelo valor que havia na linha 3 e coluna 1

## ----fim----
## -----exemplo----

    Selecione a linha que deseja zerar:4
    Selecione a linha do pivô:1
    
    linha  1                 1.0                 5.75                  3.0                  8.0 |                10.5
    linha  2                 0.0               249.25                182.0                347.0 |               448.5
    linha  3                 0.0                 21.0                 11.0                 34.0 |                -3.0
    linha  4                 0.0               -209.5               -130.0               -324.0 |              -409.0
    
    Os elementos da linha 4 fram substraidos pelo valor que havia na linha 4 e coluna 1

## ----fim---

# Repetimos o primeiro passo, agora na linha 2 

## -----exemplo----

    escolha uma opção:2
    
    linha  1                 1.0                 5.75                  3.0                  8.0 |                10.5
    linha  2                 0.0               249.25                182.0                347.0 |               448.5
    linha  3                 0.0                 21.0                 11.0                 34.0 |                -3.0
    linha  4                 0.0               -209.5               -130.0               -324.0 |              -409.0
    
    Selecione a linha:2
    
    linha  1                 1.0                 5.75                  3.0                  8.0 |                10.5
    linha  2                 0.0                  1.0   0.7301905717151455   1.3921765295887663 |  1.7993981945837512
    linha  3                 0.0                 21.0                 11.0                 34.0 |                -3.0
    linha  4                 0.0               -209.5               -130.0               -324.0 |              -409.0
    
    Valor da linha 2 e coluna 2 foi multiplicada pelo seu inverso

## ----fim----

# Repetiremos o segundo passo para as demais linhas, desde que não sejam o pivo atual:

## -----exemplo----

    Selecione a linha que deseja zerar:1
    Selecione a linha do pivô:2
    
    linha  1                 1.0                  0.0  -1.1985957873620867 -0.005015045135406737 | 0.15346038114343052
    linha  2                 0.0                  1.0   0.7301905717151455   1.3921765295887663 |  1.7993981945837512
    linha  3                 0.0                 21.0                 11.0                 34.0 |                -3.0
    linha  4                 0.0               -209.5               -130.0               -324.0 |              -409.0
    
    Os elementos da linha 1 fram substraidos pelo valor que havia na linha 1 e coluna 2

## ----fim----

# Ao fim desse processo queremos que o sistema esteja dessa forma: 

## -----exemplo----

    elecione a linha que deseja zerar:4
    Selecione a linha do pivô:2
    
    linha  1                 1.0                  0.0  -1.1985957873620867 -0.005015045135406737 | 0.15346038114343052
    linha  2                 0.0                  1.0   0.7301905717151455   1.3921765295887663 |  1.7993981945837512
    linha  3                 0.0                  0.0   -4.334002006018055     4.76429287863591 | -40.787362086258774
    linha  4                 0.0                  0.0    22.97492477432297   -32.33901705115346 |  -32.02607823470413
    
    Os elementos da linha 4 fram substraidos pelo valor que havia na linha 4 e coluna 2

## ----fim----

# Então voltamos à opção 2 e agora procuramos um pivo na linha 3:

## -----exemplo----

    Selecione a linha:3
    
    linha  1                 1.0                  0.0  -1.1985957873620867 -0.005015045135406737 | 0.15346038114343052
    linha  2                 0.0                  1.0   0.7301905717151455   1.3921765295887663 |  1.7993981945837512
    linha  3                -0.0                 -0.0                  1.0  -1.0992825734783618 |     9.4110159685258
    linha  4                 0.0                  0.0    22.97492477432297   -32.33901705115346 |  -32.02607823470413

    Valor da linha 3 e coluna 3 foi multiplicada pelo seu inverso

## ----fim----

# Repetimos o segundo passo para todas as linhas, agora excluindo a linha 3(reparou que nunca usamos a opção 4 na linha com o pivo?)

## -----exemplo----

    Selecione a linha que deseja zerar:4
    Selecione a linha do pivô:3
    
    linha  1                 1.0                  0.0                  0.0  -1.3226105068271248 |  11.433464475815784
    linha  2                 0.0                  1.0                  0.0   2.1948623003934276 | -5.0724369358944665
    linha  3                -0.0                 -0.0                  1.0  -1.0992825734783618 |     9.4110159685258
    linha  4                 0.0                  0.0                  0.0   -7.083082619763935 | -248.24346216153666

    Os elementos da linha 4 fram substraidos pelo valor que havia na linha 4 e coluna 3

## ----fim----

# Agora uma ultima vez utilizaremos a opção 2 para tornar a linha 4 um pivo

## -----exemplo----

    Selecione a linha:4
    
    linha  1                 1.0                  0.0                  0.0  -1.3226105068271248 |  11.433464475815784
    linha  2                 0.0                  1.0                  0.0   2.1948623003934276 | -5.0724369358944665
    linha  3                -0.0                 -0.0                  1.0  -1.0992825734783618 |     9.4110159685258
    linha  4                -0.0                 -0.0                 -0.0                  1.0 |  35.047376331438315

    Valor da linha 4 e coluna 4 foi multiplicada pelo seu inverso

## ----fim----

# Repita o segundo passo agora usando como pivo a linha 4

## -----exemplo----

    Selecione a linha que deseja zerar:3
    Selecione a linha do pivô:4

    linha  1                 1.0                  0.0                  0.0                  0.0 |   57.78749264850039
    linha  2                 0.0                  1.0                  0.0                  0.0 |  -81.99660197346934
    linha  3                -0.0                 -0.0                  1.0                  0.0 |   47.93798601581394
    linha  4                -0.0                 -0.0                 -0.0                  1.0 |  35.047376331438315
    
    Os elementos da linha 3 fram substraidos pelo valor que havia na linha 3 e coluna 4

## ----fim----
# Conclusão:
    Com o sistema linear nessa forma(1 na diagonal, zero no resto), podemos concluir que os valores após as barras laterais são, respectivamente, os valores de x1, x2, x3, ..., xn que satisfazem o sistema.
    nota: Caso tenha utilizado troca de colunas, não há garantias de que a ordem dos valores esteja correta, é preciso analisar o histórico para saber qual a ordem correta.
