# Implemente uma função que construa uma nova lista com a intercalação
# dos nós de outras duas listas passadas como parâmetros. Esta função deve
# retornar a lista resultante, conforme ilustrado a seguir:

# Esta função deve obedecer ao protótipo:


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


def merge(l1, l2):
    
    atual = l1
    while atual.prox is not None:
        atual = atual.prox
    
    atual.prox = l2
  
    return l1

def main():
    lista1 = None
    lista2 = None

    while True:
        try:
            valor = int(input("Digite um número (0 para sair): "))
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue

        if valor == 0:
            break 
        
        escolha_lista = int(input("Adicionar à lista 1 ou lista 2? (1/2): "))

        if escolha_lista == 1:
            lista1 = inserirElementos(lista1, valor)
        elif escolha_lista == 2:
            lista2 = inserirElementos(lista2, valor)
        else:
            print("Escolha inválida! Escolha 1 ou 2.")
        
    print("\nLista 1:")
    lista_imprime_recursivo(lista1)

    print("\nLista 2:")
    lista_imprime_recursivo(lista2)
    
    lista_ajuntada = merge(lista1,lista2)
    print("\nLista Ajuntada:")
    lista_imprime_recursivo(lista_ajuntada)

if __name__ == "__main__":
    main()
