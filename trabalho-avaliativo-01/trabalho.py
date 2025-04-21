class ListaEncadeada:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha():
    def __init__(self, capacidade, topo = None):
        self.topo = topo
        self.capacidade = capacidade
        self.num_elementos = 0


    def pilha_push(self, valor):
        if self.num_elementos >= self.capacidade:
             print("Capacidade máxima alcançada!")
             return ValueError

        if self.topo == None:
            self.num_elementos += 1
            elemento = ListaEncadeada(valor)
            self.topo = elemento

            return self

        self.num_elementos += 1
        elemento = ListaEncadeada(valor)
        elemento.prox = self.topo
        self.topo = elemento

        return self

    def pilha_show(self):
        atual = self.topo

        while atual != None:
            print(atual.info)
            atual = atual.prox

    def pilha_pop(self):
        if self.topo == None:
            print("Pilha vazia!")
        else:
            self.topo = self.topo.prox
            self.num_elementos -= 1

    def pilha_pop_print(self):
        if self.topo == None:
            print("Pilha vazia!")
        else:
            print("Valor removido:",self.topo.info)
            self.topo = self.topo.prox
            self.num_elementos -= 1
    
    def pilha_vazia(self):
        return self.topo == None

    def esvaziar_pilha(sefl):
        while sefl.num_elementos > 0:
            sefl.pilha_pop_print()
        print("Pilha esvaziada")
    
    def remover_item(self, valor):
        
        if self.topo is None:
            print("Pilha vazia!")
            return

        auxiliar = Pilha(self.capacidade)
        encontrado = False
        
        while not self.pilha_vazia():
            
            topo_valor = self.topo.info
            if topo_valor == valor and not encontrado:
                self.pilha_pop() 
                encontrado = True
            else:
                auxiliar.pilha_push(topo_valor)
                self.pilha_pop()
                
        while not auxiliar.pilha_vazia():
            self.pilha_push(auxiliar.topo.info)
            auxiliar.pilha_pop()

        if encontrado:
            print(f"Valor {valor} removido com sucesso.")
        else:
            print(f"Valor {valor} não encontrado.")


def precedencia(op):
    return {'not': 3, 'and': 2, 'or': 1}.get(op, 0)

def aplicar_operador(op, operandos):
    if op == 'not':
        if operandos.pilha_vazia():
            raise ValueError("Faltando operando para 'not'")
        valor = operandos.topo.info
        operandos.pilha_pop()
        operandos.pilha_push(not valor)
    else:
        if operandos.num_elementos < 2:
            raise ValueError(f"Faltando operandos para '{op}'")
        b = operandos.topo.info
        operandos.pilha_pop()
        a = operandos.topo.info
        operandos.pilha_pop()

        if op == 'and':
            operandos.pilha_push(a and b)
        elif op == 'or':
            operandos.pilha_push(a or b)
        else:
            raise ValueError(f"Operador desconhecido: {op}")

def avaliar(expressao):
    operadores = Pilha(100)
    operandos = Pilha(100)
    tokens = expressao.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token in ('True', 'False'):
            operandos.pilha_push(token == 'True')
        elif token in ('and', 'or', 'not'):
            while (not operadores.pilha_vazia() and operadores.topo.info != '(' and
                   precedencia(operadores.topo.info) >= precedencia(token)):
                op = operadores.topo.info
                operadores.pilha_pop()
                aplicar_operador(op, operandos)
            operadores.pilha_push(token)
        elif token == '(':
            operadores.pilha_push(token)
        elif token == ')':
            while not operadores.pilha_vazia() and operadores.topo.info != '(':
                op = operadores.topo.info
                operadores.pilha_pop()
                aplicar_operador(op, operandos)
            if operadores.pilha_vazia():
                raise ValueError("Parênteses desbalanceados")
            operadores.pilha_pop()  # Remove o '('
        else:
            raise ValueError(f"Token inválido: {token}")

    while not operadores.pilha_vazia():
        if operadores.topo.info == '(':
            raise ValueError("Parênteses desbalanceados")
        op = operadores.topo.info
        operadores.pilha_pop()
        aplicar_operador(op, operandos)

    if operandos.num_elementos != 1:
        raise ValueError("Expressão malformada")

    return operandos.topo.info


expressao = "(True or False) not or (False or True)"
resultado = avaliar(expressao)
print("Resultado:", resultado)