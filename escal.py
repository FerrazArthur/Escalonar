import math
import numpy as np
from tabulate import tabulate as tab
def menu():
    print("\n1-Multiplicar linha por constante\n2-Transformar primeiro elemento não zero da linha em pivo unitário\n3-Somar linha à multiplo de outra linha\n4-Utilizar pivo unitário em uma linha\n5-Trocar linhas\n6-Trocar colunas\n7-Printar sistema\n8-Printar registro de alteração de colunas\n9-Alterar sistema\n10-Sair\n")
    x = int(input("escolha uma opção:"))
    return x
def confirmar():
    x = input("\nCaso deseje desfazer a ultima operação, insera 'r', caso contrário, insira qualquer outra letra:")
    if x == 'r' or x == 'R':
        return 1
    else:
        return 0
def toMat(A):
    aux = A.replace(' ', '')
    aux = [index for index in A.split(';')]
    for i in range(len(aux)):
        aux[i] = aux[i].replace(' ', '')
        aux[i] = [float(index) for index in aux[i].split(',')]
    return aux
def toVet(b):
    aux = b.replace(' ', '')
    aux = [float(index) for index in aux.split(',')]
    return aux
def selectLine(A, phrase = "Selecione a linha:"):
    i=int(input(phrase))
    while i > len(A) or i <= 0:
        print("Opção inválida, tente novamente:")
        i=int(input(phrase))
    return i-1
def EQuadrada(A):
    for i in range(len(A)):
        if len(A[i]) != len(A):
            return False
    return True

def printar(A, b, X):
    #preparando a tabela
    linhas=[]
    for i in range(1,np.size(A, 0)+1):
        linhas.append('Linha '+'{0:2}'.format(i))
    #adicionando nome das linhas à tabela
    table=np.append(np.transpose(np.column_stack(linhas)), A, axis=1)
    #adicionando matriz de coeficientes à tabela
    table=np.append(table, np.transpose(np.column_stack(b)), axis=1)

    print('\n'+tab(table,headers=X, tablefmt='heavy_grid'))
    print()

def getSys():
    A = input("## use virgula para separar os elementos em uma mesma linha, ';' para separar uma linha de outra\nInsira a matriz A:\n")
    b = input("Insira a matriz b:\n")
    A = toMat(A)
    b = toVet(b)
    if EQuadrada(A):
        if len(b) != len(A):
            print("Sistema incompatível")
            return None, None
    else:
        print("Sistema não é quadrado")
        return None, None
    return A, b
def MultiplyLine(A, b, n = '', i = ''):#multiplica linha por constante N
    if n == '':
        i = selectLine(A)
        n=float(input("Selecione a constante:"))
    for j in range(len(A)):
        A[i][j] *= n
    b[i] *= n
    return A
def SumLines(A, b, n = '', i = '', x = ''):
    if n == '':
        i=selectLine(A,"Selecione a linha a operar:")
        x=selectLine(A,"Selecione a linha auxiliar:")
        n=float(input("Insira a constante:"))
    for j in range(len(A)):
        A[i][j] += A[x][j]*n
    b[i] += b[x]*n
    return A
def main():
    A, b = getSys()
    X = []
    if A is None or b is None:
        return
    for i in range(1, np.size(A, 0)+1):
        X.append('X{0:02}'.format(i))
    X.append('Constantes')
    printar(A, b, X)
    regis=""
    print("#Dica de uso: escolha opção 2 pra primeira linha, em seguida a opção 4 usando todas as outras linhas\n#Escolha novamente a opção 2 e agora a segunda linha, depois use a opção 4 novamente pra todas as linhas\n#Repita esse processo até o fim do sistema e ele estará triagularizado\n")
    while 1:
        if A is None or b is None:
            return
        op = menu()
        redo = 0
        Abkp = np.copy(A).tolist()
        bbkp = np.copy(b).tolist()
        xbkp = np.copy(X).tolist()
        if op == 1:
            printar(A, b, X)
            A = MultiplyLine(A, b)
            printar(A, b, X)
            redo = confirmar()
        if op == 2:
            printar(A, b, X)
            x = 0
            i = selectLine(A)
            while A[i][x] == 0 and x < len(A):#procurando o primeiro elemento não nulo da linha
                x+=1
            if x == len(A):
                print("linha nula nao pode ser pivo\n")
                break
            n =  1/A[i][x]
            A = MultiplyLine(A, b, n, i)
            printar(A, b, X)
            print("Valores da linha "+str(i+1)+" foram multiplicados pelo inverso do  valor na coluna "+str(x+1))
            redo = confirmar()
        if op == 3:
            printar(A, b, X)
            A = SumLines(A, b)
            printar(A, b, X)
            redo = confirmar()
        if op == 4:
            printar(A, b, X)
            z = 0
            i=selectLine(A,"Selecione a linha que deseja zerar:")
            x=selectLine(A,"Selecione a linha do pivô:")
            while z < len(A) and abs(A[x][z]-1) > 0.0001:#procurando por posição do pivô
                z += 1
            if z == len(A):
                print("Não há pivô(precisa ser 1)")
                break
            n = -1*A[i][z]
            A = SumLines(A, b, n, i, x)
            printar(A, b, X)
            print("Os elementos da linha "+str(i+1)+" foram substraidos pelo valor que havia na linha "+str(i+1)+" e coluna "+str(z+1))
            redo = confirmar()
        if op == 5:
            printar(A, b, X)
            i=selectLine(A)
            j=selectLine(A, "Selecione outra linha:")
            aux = np.copy(A[i]).tolist()#trocando linhas
            A[i] = A[j]
            A[j] = aux
            aux = b[i]
            b[i] = b[j]
            b[j] = aux#fim
            print("\nAs linhas selecionadas foram trocadas")
            printar(A, b, X)
            redo = confirmar()
        if op == 6:
            #print("## atenção! após utilizar essa opção, verifique o registro de troca de colunas pois a ordem dos coeficientes é alterada")
            printar(A, b, X)
            i=selectLine(A,"Selecione uma coluna: ")
            j=selectLine(A,"Selecione outra coluna: ")
            aux = []
            #atualizando a ordem do vetor das variáveis
            auxx = X[j]
            X[j] = X[i]
            X[i] = auxx
            for x in range(len(A)):#trocando colunas
                aux.append(A[x][i])
                A[x][i] = A[x][j]
            for x in range(len(A)):#fim
                A[x][j] = aux[x]
            print("\nAs colunas selecionadas foram trocadas")
            printar(A, b, X)
            redo = confirmar()
            if redo == 0:
                regis += "as colunas "+str(i+1)+" e "+str(j+1)+" foram trocadas\n"
        if redo == 1:
            A = Abkp
            b = bbkp
            x = xbkp
        if op == 7:
            printar(A, b, X)
            print(regis)
        if op == 8:
            print(regis)
        if op == 9:
            op = int(input("\n1-Inserir novo sistema \n2-Alterar apenas um valor\nescolha uma opção:"))
            if op == 1:
                A, b = getSys()
            elif op == 2:
                i = selectLine(A,"Selecione a linha:")
                j = selectLine(A,"Selecione a coluna")
                x = float(input("\nnovo valor:"))
                A[i][j] = x
            else:
                print("Opção não reconhecida")
        if op == 10:
            return
        if op < 1 or op > 10:
            print("opção invalida")
main()
