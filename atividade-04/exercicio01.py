#✅ 1. Crie uma pilha com capacidade 10 e empilhe os números de 1 a 5. Depois, desempilhe todos os elementos mostrando na tela um por um.

#✅ 2. Crie uma função esvaziar_pilha(p) que desempilha todos os elementos até que a pilha esteja vazia. Ao final, imprima “Pilha esvaziada”.

#✅ 3. Solicite ao usuário que digite 5 números. Armazene-os numa pilha. Depois, mostre os números na ordem inversa à digitada, desempilhando.

#✅ 4. Simule um editor de texto. Cada caractere digitado é empilhado. Quando o usuário digitar #, o último caractere deve ser removido (como um undo).

#✅ 5. Crie um método para remover um item do meio de uma pilha. Ele deve manter a ordem original apenas removendo o item especificado.


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

def main():
    capacidade = int(input("Digite a capacidade da Pilha: "))
    pilha = Pilha(capacidade)
    while True:
        valor = input("Digite para inserir ou (0)SAIR (#)APAGAR: ")
        if valor == "0":
            break
        if valor == "#":
            pilha.pilha_pop_print()
            continue
        try:
            if(pilha.pilha_push(valor) == ValueError  ): break
            
        except Exception as e:
            print(e)
    
    if(input("Deseja desempilhar tudo? Digite sim ou não:") == "sim"):        
        print("\nDESEMPILHANDO!\n")
        while pilha.num_elementos > 0:
            pilha.pilha_pop_print()
        return  
    
    pilha.remover_item(input("\nDigite algo para remover\n"))
    
    if(input("Remover todos os elementos? Digite sim ou não:") == "sim"):
        print("\n Tua escolha não importa!\n")        
        pilha.esvaziar_pilha()    
    
    
if __name__ == "__main__":
    main()