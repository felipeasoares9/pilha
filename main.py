from Livro import Livro
from Pilha import Pilha

livro1 = Livro("Alice no País das Maravilhas", "Lewis Carroll", 192)
livro2 = Livro("O Conto do Mouro-Coelho", "João Guimarães Rosa", 256)
pilha = Pilha()


pilha.add(livro1)
pilha.add(livro2)
pilha.remover()
pilha.imprimir()