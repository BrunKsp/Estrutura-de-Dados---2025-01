	
# Exercícios - Listas Duplamente Encadeadas
# Implemente para listas duplamente encadeadas:
# Inserção ✅
# Impressão ✅
# Busca ✅
# Remoção ✅
# Inserção no fim ✅
# Inserção ordenada (busca pela posição em que deve ser inserido) ✅


class ListaDE:
    
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None


def InserirElemento(lista, valor):
    novo_elemento = ListaDE(valor)
    
    if ( lista is None ) : 
        return novo_elemento
     
    novo_elemento.prox = lista
    lista.ant = novo_elemento

    return novo_elemento

def ExibirElementos(lista):
     
    elemento = lista

    while elemento is not None:
        print(elemento.info)
        elemento = elemento.prox
        

def BuscarElemento(lista, valor):
    elemento = lista
    while elemento is not None:
        if elemento.info == valor:
            return print("Elemento encontrado:", elemento.info)
        elemento = elemento.prox
        
    return print("Elemento não encontrado!")

def RemoverElemento(lista, valor):
    elemento = lista
    anterior = None
    
    while elemento is not None:
        if elemento.info == valor:
            if elemento == lista:
                if elemento.prox is not None:
                    proximo = elemento.prox
                    proximo.ant = None
                return elemento.prox
            
            elif elemento.prox == None:
                anterior.prox = None
                return lista
            
            else:
                anterior.prox = elemento.prox

                if elemento.prox is not None:
                    proximo = elemento.prox
                    proximo.ant = anterior

                return lista
            
        anterior = elemento
        elemento = elemento.prox

def InserirNoFim(lista, valor):
    novo_elemento = ListaDE(valor)
    if lista is None:
        return novo_elemento
    else:
        elemento = lista
        while elemento.prox is not None:
            elemento = elemento.prox
        elemento.prox = novo_elemento
        novo_elemento.ant = elemento
        return lista

def InserirOrdenado(lista, valor):
    elemento = lista
    novo_elemento = ListaDE(valor)
    
    if lista is None or valor < lista.info:
        novo_elemento.prox = lista
        if lista is not None:
            lista.ant = novo_elemento
        return novo_elemento
    
    while elemento is not None:
        proximo = elemento.prox
    
        if valor <= elemento.info and elemento.ant is None:
            novo_elemento.prox = elemento
            elemento.ant = novo_elemento
            return novo_elemento
      
        if elemento.prox is None:
            elemento.prox = novo_elemento
            novo_elemento.ant = elemento
            return lista
        
        if valor >= elemento.info and valor <= proximo.info:
            elemento.prox = novo_elemento
            novo_elemento.ant = elemento
            novo_elemento.prox = proximo
            proximo.anterior = novo_elemento
            
            return lista

        elemento = elemento.prox


def main():
    primeiro_elemento = None 

    valor = int(input("Selecione uma forma de iserção: (1)Ordenado, (2)Aleatorio"))

    if valor == 1:
        while True:
            valor = int(input("Digite um número para inserir ordenado ou (0)SAIR:"))
                   
            if valor == 0:
                break
            primeiro_elemento = InserirOrdenado(primeiro_elemento,valor )
                    
    elif valor == 2:
        while True:
            valor = int(input("Digite um número para inserir aleatorio ou (0)SAIR:"))
            
            if valor == 0:
             break                
            primeiro_elemento = InserirElemento(primeiro_elemento, valor)
    else:
        print("Opção inválida! Escolha 1, 2 ou 0.")
    
       


    print("\n Lista Original")
    ExibirElementos(primeiro_elemento)

    buscar = int(input("Deseja buscar um valor? Digite um número:"))
    BuscarElemento(primeiro_elemento, buscar)
    
    remover = int(input("Deseja remover um valor? Digite um número:"))
    primeiro_elemento=  RemoverElemento(primeiro_elemento, remover)
    
    print("\n Lista Atualizada")
    ExibirElementos(primeiro_elemento)
    
    inserir_fim = int(input("Deseja inserir um valor no final da lista? Digite um número:"))
    primeiro_elemento = InserirNoFim(primeiro_elemento, inserir_fim)
    
    print("\n Lista Atualizada 2.0")
    ExibirElementos(primeiro_elemento) 

if __name__ == "__main__":
    main()