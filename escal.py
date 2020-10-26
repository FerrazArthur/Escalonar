import math
import numpy as np
def menu():
    print("1-Multiplicar linha por constante\n2-Transformar linha em pivo unitário\n3-Somar linha à multiplo de outra linha\n4-Utilizar pivo unitário em uma linha\n5-Trocar linhas\n6-Trocar colunas\n7-Printar sistema\n8-Printar registro de alteração de colunas\n9-Alterar valor\n10-Sair\n")
    x = int(input("escolha uma opção:"))
    return x
def confirmar():
    x = input("\nDeseja desfazer ultima alteração?(s/n)")
    if x == "s":
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
def printar(A, b):
    print()
    for i in range(len(A)):
        print("linha {0:2}".format(i+1), end = '')
        for j in range(len(A)):
            print("{0:15}".format(A[i][j]), end = ' ')
        print("|{:15}".format(b[i]))
    print()
def main():
    A = input("## use virgula para separar os elementos em uma mesma linha, ';' para separar uma linha de outra\nInsira a matriz A:\n")
    b = input("Insira a matriz b:\n")
    A = toMat(A)
    b = toVet(b)
    if EQuadrada(A):
        if len(b) != len(A):
            print("Sistema incompatível")
            return
    else:
        print("Sistema não é quadrado")
        return
    printar(A, b)
    regis=""
    print("#Dica de uso: escolha opção 2 pra primeira linha, em seguida a opção 4 usando todas as outras linhas\n#Escolha novamente a opção 2 e agora a segunda linha, depois use a opção 4 novamente pra todas as linhas\n#Repita esse processo até o fim do sistema e ele estará triagularizado\n")
    while 1:
        op = menu()
        redo = 0
        Abkp = np.copy(A).tolist()
        bbkp = np.copy(b).tolist()
        if op == 1:
            printar(A, b)
            i = selectLine(A)
            n=float(input("Selecione a constante:"))
            for j in range(len(A)):
                A[i][j] *= n
            b[i] *= n
            printar(A, b)
            redo = confirmar()
        if op == 2:
            printar(A, b)
            i = selectLine(A)
            x = 0
            while A[i][x] == 0 and x < len(A):
                x+=1
            if x == len(A):
                print("linha nula nao pode ser pivo\n")
                break
            n =  1/A[i][x]
            for j in range(len(A)):
                A[i][j] *= n
            b[i] *= n
            printar(A, b)
            print("Valor da linha "+str(i+1)+" e coluna "+str(x)+" foi multiplicada pelo seu inverso")
            redo = confirmar()
        if op == 3:
            printar(A, b)
            i=selectLine(A,"Selecione a linha a operar:")
            x=selectLine(A,"Selecione a linha auxiliar:")
            n=float(input("Insira a constante:"))
            for j in range(len(A)):
                A[i][j] += A[x][j]*n
            b[i] += b[x]*n
            printar(A, b)
            redo = confirmar()
        if op == 4:
            printar(A, b)
            i=selectLine(A,"Selecione a linha a zerar:")
            x=selectLine(A,"Selecione a linha do pivô:")
            z = 0
            while A[x][z] != 1 and z < len(A):
                z += 1
            if z == len(A):
                print("Não há pivô(precisa ser 1)")
                break
            n = A[i][z]
            for j in range(len(A)):
                A[i][j] -= A[x][j]*n
            b[i] -= b[x]*n
            printar(A, b)
            print("À linha "+str(i+1)+" foi substraido o valor que havia na linha "+str(i+1)+" e coluna "+str(z+1))
            redo = confirmar()
        if op == 5:
            printar(A, b)
            i=selectLine(A)
            j=selectLine(A, "Selecione outra linha:")
            aux = np.copy(A[i]).tolist()
            A[i] = A[j]
            A[j] = aux
            aux = b[i]
            b[i] = b[j]
            b[j] = aux
            print("As linhas selecionadas foram trocadas")
            printar(A, b)
            redo = confirmar()
        if op == 6:
            print("## atenção! após utilizar essa opção, verifique o registro de troca de colunas pois a ordem dos coeficientes é alterada")
            printar(A, b)
            i=selectLine(A,"Selecione uma coluna: ")
            j=selectLine(A,"Selecione outra coluna: ")
            aux = []
            for x in range(len(A)):
                aux.append(A[x][i])
                A[x][i] = A[x][j]
            for x in range(len(A)):
                A[x][j] = aux[x]
            print("As colunas selecionadas foram trocadas")
            printar(A, b)
            redo = confirmar()
            if redo == 0:
                regis += "as colunas "+str(i+1)+" e "+str(j+1)+" foram trocadas\n"
        if redo == 1:
            A = Abkp
            b = bbkp
        if op == 7:
            printar(A, b)
            print(regis)
        if op == 8:
            print(regis)
        if op == 9:
            i = selectLine(A,"Selecione a linha:")
            j = selectLine(A,"Selecione a coluna")
            x = float(input("novo valor:"))
            A[i][j] = x
        if op == 10:
            return
        if op < 1 or op > 10:
            print("opção invalida")
main()
