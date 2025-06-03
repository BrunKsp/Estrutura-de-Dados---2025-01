# Escreva uma função que percorra uma árvore binária de busca e mostre os valores armazenados em
# ordem decrescente. Tal função deve ter o seguinte protótipo: def abb_imprime(a)

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

def abb_imprime(root):
    if root is not None:
        abb_imprime(root.direita)
        print(root.chave, end=' ')
        abb_imprime(root.esquerda)

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
inserir(arvore.raiz, 9)

print("Pré-ordem:")
pre_ordem(arvore.raiz)



remover(arvore.raiz, 8)
remover(arvore.raiz, 1)
remover(arvore.raiz, 5)
remover(arvore.raiz, 4)
print("\n Pós Remoção")
pre_ordem(arvore.raiz)

print("\n Ordem Descrescente")
abb_imprime(arvore.raiz)
