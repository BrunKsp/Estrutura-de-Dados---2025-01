# 1. Implemente uma função que insere um elemento no final da lista simplesmente encadeada circular.
# 2. Implemente uma função que busca um valor específico na lista encadeada circular e retorne True se encontrado ou False caso contrário.
# 3. Implemente uma função que remove um elemento específico da lista encadeada circular.
# 4. Crie uma função que conte quantos elementos estão na lista encadeada circular.


class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert_node(lista, info):
    new_element = Lista(info)

    if lista == None:
        new_element.prox = new_element
        return new_element

    atual = lista

    while atual.prox != lista:
        atual = atual.prox

    atual.prox = new_element
    new_element.prox = lista

    return new_element

def show_elements(lista):
    atual = lista
    count = 0 
    while True:
        print(atual.info)
        atual = atual.prox
        count+=1
        if atual == lista:
            return count

def remove_element(lista, value):
    if lista.prox == lista:
        if lista.info == value:
            print("Esvaziando lista...")
            return None

        print("Item não localizado!")
        return lista

    if lista.info == value:
        ultimo_elemento = lista

        # Ir até o final da lista -> Atual = Último elemento da lista
        while ultimo_elemento.prox != lista:
            ultimo_elemento = ultimo_elemento.prox

        ultimo_elemento.prox = lista.prox

        return lista.prox

    atual = lista
    anterior = None

    while True:
        if atual.info == value:
            anterior.prox = atual.prox
            return lista
        
        anterior = atual
        atual = atual.prox

        if atual == lista:
            print("Item não localizado!")
            break

    return lista

def inserir_final(lista, valor):
    novo_elemento = Lista(valor)
    
    if lista is None: 
        novo_elemento.prox = novo_elemento
        novo_elemento.ant = novo_elemento
        return novo_elemento
    else:
        elemento = lista
        while elemento.prox != lista:  
            elemento = elemento.prox
        
        elemento.prox = novo_elemento  
        novo_elemento.ant = elemento   
        novo_elemento.prox = lista     
        lista.ant = novo_elemento     
        
        return lista


def buscar_elemento(lista, valor):
    elemento = lista
    while elemento != lista:
        if elemento.info == valor:
            return True
        elemento = elemento.prox
        
    return False


lista = None

lista = insert_node(lista, 9)
lista = insert_node(lista, 7)
lista = insert_node(lista, 5)
lista = insert_node(lista, 3)

print("=-=-=-= ANTES =-=-=-=")
show_elements(lista)

print("=-=-=-= DEPOIS =-=-=-=")
lista = inserir_final(lista, 11)
show_elements(lista)

print("=-=-=-= BuscarElemento =-=-=-=")
print(buscar_elemento(lista, 3))

print("=-=-=-= RemoverElemento =-=-=-=")
lista = remove_element(lista, 5) 
show_elements(lista)


print("=-=-=-= Contar Elementos =-=-=-=")
total = show_elements(lista)
print("Total de elementos:", total)