# 6. Considere listas que armazenam cadeias de caracteres e implemente uma
# função para criar uma cópia de uma lista encadeada. Essa função deve
# obedecer ao protótipo:
    
def copia(lst):
    nova_lista = ListaEncadeada(lst.info)
    atual_copia = nova_lista
    
    while lst is not None:
        lista_nova = ListaEncadeada(lst.info)
        atual_copia.prox = lista_nova
        atual_copia = lista_nova
        lst = lst.prox
    
    return nova_lista

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

    print("\nLista Original:")
    lista_imprime_recursivo(primeiro_elemento)
    
    print("\nLista Copiada:")
    lista_copiada = copia(primeiro_elemento)
    lista_imprime_recursivo(lista_copiada)

if __name__ == "__main__":
    main()
