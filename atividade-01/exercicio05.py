# 5. Considere listas que armazenam cadeias de caracteres e implemente uma
# função para testar se duas listas passadas como parâmetros são iguais. Essa
# função deve obedecer ao protótipo:

def igual(l1, l2):
    while l1 is not None and l2 is not None:
       if l1.info == l2.info:
           return True
       l1 = l1.prox
       l2 = l2.prox
       
    return False


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

    print("\nLista Igual:")
    print(igual(lista1,lista2))

if __name__ == "__main__":
    main()
