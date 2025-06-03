# Considerando os algoritmos de inserção e remoção em uma árvore binária de busca, mostre como fica
# a composição da árvore após cada uma das operações a seguir:
# a = abb_insere(a, 5)
# a = abb_insere(a, 1)
# a = abb_insere(a, 3)
# a = abb_insere(a, 4)
# a = abb_insere(a, 7)
# a = abb_insere(a, 2)
# a = abb_insere(a, 8)
# a = abb_retira(a, 8)
# a = abb_retira(a, 1)
# a = abb_retira(a, 5)
# a = abb_retira(a, 4)

class No:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

def inserir(root, key):
    if root is None:
        return No(key)
    if key < root.chave:
        root.esquerda = inserir(root.esquerda, key)
    else:
        root.direita = inserir(root.direita, key)
    return root

def remover(root, key):
    # O número não existe ou árvore vazia
    if root is None:
        return None
    
    if key < root.chave:
        root.esquerda = remover(root.esquerda, key)
    else:
        root.direita = remover(root.direita, key)
        
    # Toda lógica de remoção
    if root.chave == key:
        if root.esquerda is None and root.direita is None:
          
            root = None
        elif root.esquerda is None:
            root = root.direita
        elif root.direita is None:
            root = root.esquerda
        else:
            aux = root.esquerda
            
            # Chega ao final da direita
            while aux.direita is not None:
                aux = aux.direita
            
            aux.chave, root.chave = root.chave, aux.chave
            
            root.esquerda = remover(root.esquerda, key)
    
    return root

def buscar(root, key):
    if root is None:
        return None  

    if key == root.chave:
        return root 

    if key < root.chave:
        return buscar(root.esquerda, key)
    else:
        return buscar(root.direita, key)



def pre_ordem(no):
    if no:
        print(no.chave, end=' ')
        pre_ordem(no.esquerda)
        pre_ordem(no.direita)

def em_ordem(no):
    if no:
        em_ordem(no.esquerda)
        print(no.chave, end=' ')
        em_ordem(no.direita)

def pos_ordem(no):
    if no:
        pos_ordem(no.esquerda)
        pos_ordem(no.direita)
        print(no.chave, end=' ')



arvore = ArvoreBinaria()

arvore.raiz = No(5)
inserir(arvore.raiz, 1)
inserir(arvore.raiz, 3)
inserir(arvore.raiz, 4)
inserir(arvore.raiz, 7)
inserir(arvore.raiz, 2)
inserir(arvore.raiz, 8)

print("Pré-ordem:")
pre_ordem(arvore.raiz)



remover(arvore.raiz, 8)
remover(arvore.raiz, 1)
remover(arvore.raiz, 5)
remover(arvore.raiz, 4)
print("\n Pós Remoção")
pre_ordem(arvore.raiz)

