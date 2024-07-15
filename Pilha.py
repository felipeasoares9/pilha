from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, l: Livro):
        if not self.topo:
            self.topo = l
        else:
            l.proximo = self.topo
            self.topo = l
        self.tamanho += 1

    def remover(self) -> Livro:
        if not self.topo:
            return None
        livro_atual = self.topo
        self.topo = livro_atual.proximo
        if self.topo is None:
            self.topo = None  # garantir que o topo seja nulo se a pilha estiver vazia
        else:
            self.topo.proximo = None  # desvincular o próximo da pilha
        self.tamanho -= 1
        return livro_atual

    def imprimir(self):
        atual = self.topo
        while atual:
            print(f"Título: {atual.titulo}, Autor: {atual.autor}, Páginas: {atual.paginas}")
            atual = atual.proximo