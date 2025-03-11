# Implemente uma função que receba como parâmetro uma lista encadeada
# e inverta o encadeamento de seus nós, retornando a lista resultante. Após a
# execução desta função, cada nó da lista vai estar referenciando (prox) o nó
# que originalmente era seu antecessor, e o último nó da lista passará a ser o
# primeiro nó da lista invertida, conforme ilustrado a seguir:

# Esta função deve obedecer ao protótipo:
def inverte(lst):
    anterior = None
    atual = lst
    
    while atual is not None:
    
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo
    
    return anterior

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
        
    print("\nLista Original")
    lista_imprime_recursivo(primeiro_elemento)

    print("\nLista Invertida:")
    primeiro_elemento = inverte(primeiro_elemento)
    lista_imprime_recursivo(primeiro_elemento)


if __name__ == "__main__":
    main()
