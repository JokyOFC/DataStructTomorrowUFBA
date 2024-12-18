class No:
    def __init__(self, chave, dado):
        self.chave = chave
        self.dado = dado
        self.direita = None
        self.esquerda = None
    
    def __str__(self):
        return f"|{self.dado}|"


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    def busca(self, chave):
        atual = self.raiz
        parent = self

        while atual is not None and chave != atual.chave:
            parent = atual
            if chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        return (atual, parent)
    
    def inserir(self, chave, dado):
        no, pai = self.busca(chave)

        if no is not None:
            no.dado = dado
            return
        
        if pai is self:
            self.raiz = No(chave, dado)
        elif chave < pai.chave:
            pai.esquerda = No(chave, dado)
        else:
            pai.direita = No(chave, dado)
    
    def remover(self, chave):
        no, pai = self.busca(chave)

        if no is not None:
            self.__remover(no, pai)

    def __remover(self, no, pai):
        if no.esquerda is not None:

            if no.direita is not None:
                self.__promoverSucessor(no)
                return

            if pai is self:
                self.raiz = no.esquerda
            elif no is pai.esquerda:
                pai.esquerda = no.esquerda
            elif no is pai.direita:
                pai.direita = no.esquerda
        
        elif no.direita is not None:

            if pai is self:
                self.raiz = no.direita
            elif no is pai.esquerda:
                pai.esquerda = no.direita
            elif no is pai.direita:
                pai.direita = no.direita
        
        else:
        
            if pai is self:
                self.raiz = None
            elif no is pai.esquerda:
                pai.esquerda = None
            else:
                pai.direita = None
        
    def __promoverSucessor(self, no):
        pai = no
        sucessor = no.direita

        while sucessor.esquerda is not None:
            pai = sucessor
            sucessor = sucessor.esquerda
        
        no.chave = sucessor.chave
        no.dado = sucessor.dado
        self.__remover(sucessor, pai)
    
    def calcularTotal(self):
        return self.__calcularTotal(self.raiz)
    
    def __calcularTotal(self, no):

        if no is None:
            return 0
        
        esquerda = self.__calcularTotal(no.esquerda)
        direita = self.__calcularTotal(no.direita)

        return esquerda + direita + no.dado





arvore = ArvoreBinariaBusca()

arvore.inserir(55, 10)
arvore.inserir(40, 20)
arvore.inserir(60, 75)
arvore.inserir(65, 10)
arvore.inserir(56, 40)
arvore.inserir(30, 98)

arvore.remover(60)

print(arvore.busca(55)[0])
print(arvore.busca(40)[0])
print(arvore.busca(60)[0])
print(arvore.busca(65)[0])
print(arvore.busca(56)[0])
print(arvore.busca(30)[0])