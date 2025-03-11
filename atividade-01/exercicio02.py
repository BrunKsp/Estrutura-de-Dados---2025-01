# 2. Considere listas de valores inteiros e implemente uma função que receba
# como parâmetro uma lista encadeada e um valor inteiro n e divida a lista em
# duas, de forma a segunda lista começar no primeiro nó logo após a
# ocorrência de n na lista original. A figura a seguir ilustra esta separação:

# A função deve retornar a referência para a segunda subdivisão da lista
# original, enquanto lst deve continuar apontando para o primeiro elemento da
# primeira subdivisão da lista. Essa função deve obedecer ao protótipo:


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

def separa(lst, n):
    
    atual = lst
    
    while atual is not None:
        if atual.info == n:
            if atual.prox is None:
                return None
            segunda_lista = atual.prox
            print("Ola")
            atual.prox = None 
            return segunda_lista
        
        atual = atual.prox
        print("Ola 2.0", atual.info)    
    return None

def lista_imprime_recursivo(lista):
    print(lista.info)

    if lista.prox != None:
        lista_imprime_recursivo(lista.prox)


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

    remover = int(input("Insira um valor para dividir a lista:"))

    if (buscarValor(primeiro_elemento, remover) is None): 
            return print("Valor inexistente não pode ser usado para a divisão da lista!")

    segunda_lista = separa(primeiro_elemento, remover)

    print("Primeira Subdivisão:")
    lista_imprime_recursivo(primeiro_elemento)

    print("Segunda Subdivisão:")
    lista_imprime_recursivo(segunda_lista)


if __name__ == "__main__":
    main()