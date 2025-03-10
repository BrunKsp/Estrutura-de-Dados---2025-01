# 1. Considere listas de valores inteiros e implemente uma função que receba
# como parâmetros uma lista encadeada e um valor inteiro n, retire da lista
# todas as ocorrências de n e retorne a lista resultante. Esta função deve
# obedecer ao protótipo:


class ListaEncadeada:
    def __init__(self, value):
        self.info = value
        self.prox = None

def inserirElementos(primeiro_elemento, valor):
    novo_elemento = ListaEncadeada(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento

def buscarValor(lista, valor):
    atual = lista

    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox

    return None

def removerValor(lista, valor):
    atual = lista
    anterior = None

    while atual is not None:
        if atual.info == valor:
            if anterior == None:
                return atual.prox
            elif atual.prox == None:
                anterior.prox = None
                return lista
            else:
                anterior.prox = atual.prox
                return lista

        anterior = atual
        atual = atual.prox

    return lista

def lista_imprime_recursivo(lista):
    print(lista.info)

    if lista.prox != None:
        lista_imprime_recursivo(lista.prox)


def retira_n(lst, n):

    while buscarValor(lst, n) is not None:
        lst = removerValor(lst, n)
    return lst

def main():
    primeiro_elemento = None 

    while True:
        try:
            valor = int(input("Digite um número (0 para sair): "))
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue

        if valor == 0:
            break 
        
        primeiro_elemento = inserirElementos(primeiro_elemento, valor)

    remover = int(input("Insira um valor para remover da lista:"))

    if (buscarValor(primeiro_elemento, remover) is None): 
            return print("Valor inexistente não pode ser removido!")

    primeiro_elemento = retira_n(primeiro_elemento,remover)
    lista_imprime_recursivo(primeiro_elemento )


if __name__ == "__main__":
    main()
