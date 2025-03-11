# Implemente funções para inserir e retirar um elemento de uma lista circular
# simplesmente encadeada (obtenha informações adicionais sobre listas
# circulares na bibliografia básica da disciplina).


class ListaEncadeadaCircular:
    def __init__(self, value):
        self.info = value
        self.prox = self

def inserirElementos(primeiro_elemento, valor):
    
    print("Dados", primeiro_elemento, valor)
    novo_elemento = ListaEncadeadaCircular(valor)
    
    if primeiro_elemento is None:
        return novo_elemento
    
    atual = primeiro_elemento
    print("Atual", atual)
    
    while atual.prox != primeiro_elemento:  
        atual = atual.prox
        
    atual.prox = novo_elemento
    novo_elemento.prox = primeiro_elemento
    
    return novo_elemento


def removerValor(lista, valor):
    
    if lista is None:
        print("Lista vazia")
        return lista
    
    if lista.prox == lista and lista.info == valor:
        return None 
    
    atual = lista
    anterior = None

    while True:
        if atual.info == valor:
            if anterior == None:
                ultimo = lista
                while ultimo.prox != lista:
                        ultimo = ultimo.prox
                lista = atual.prox
                ultimo.prox = lista 
            else:
                anterior.prox = atual.prox
            break

        anterior = atual
        atual = atual.prox

    return lista

    
## Sinceridade é tudo, isso aqui o meu amigo que fez(GPT)
def imprimirListaCircular(lista):
    atual = lista
    while True:
        print(atual.info, end=" -> ")
        atual = atual.prox
        if atual == lista: 
            break
    print("... (de volta ao início)")

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
    print("\n Lista Original")
    imprimirListaCircular(primeiro_elemento)
    remover = int(input("Deseja remover um valor ? Digite um número:"))
    primeiro_elemento = removerValor(primeiro_elemento,remover)
    print("\n Lista Atualizada")
    imprimirListaCircular(primeiro_elemento)


if __name__ == "__main__":
    main()
