import unittest

from P06_3522_pilha_encadeada import PilhaEncadeada as Pilha
from P06_3522_fila_encadeada import FilaEncadeada as Fila

class TestesPilhaEncadeada(unittest.TestCase):

    def teste_estado_inicial(self):
        """A pilha deve nascer vazia e com tamanho zero."""
        pilha = Pilha()
        self.assertEqual(len(pilha), 0)
        self.assertTrue(pilha.esta_vazia())

    def teste_push_e_topo(self):
        """O método push deve inserir no topo corretamente."""
        pilha = Pilha()
        pilha.push("A")
        pilha.push("B")
        
        self.assertEqual(len(pilha), 2)
        self.assertEqual(pilha.topo(), "B")
        self.assertFalse(pilha.esta_vazia())

    def teste_pop_comportamento_lifo(self):
        """O método pop deve remover os itens na ordem inversa (LIFO)."""
        pilha = Pilha()
        pilha.push(10)
        pilha.push(20)
        pilha.push(30)
        
        self.assertEqual(pilha.pop(), 30)
        self.assertEqual(len(pilha), 2)
        
        self.assertEqual(pilha.pop(), 20)
        self.assertEqual(len(pilha), 1)

    def teste_excecoes_pilha_vazia(self):
        """pop() e topo() devem levantar IndexError se a pilha estiver vazia."""
        pilha = Pilha()
        
        with self.assertRaises(IndexError):
            pilha.pop()
            
        with self.assertRaises(IndexError):
            pilha.topo()


class TestesFilaEncadeada(unittest.TestCase):

    def teste_estado_inicial(self):
        """A fila deve nascer vazia e com tamanho zero."""
        fila = Fila()
        self.assertTrue(fila.esta_vazia())
        self.assertEqual(len(fila), 0)

    def teste_enfileirar_e_tamanho(self):
        """O método enfileirar deve aumentar o tamanho da fila."""
        fila = Fila()
        fila.enfileirar(10)
        fila.enfileirar(20)
        
        self.assertFalse(fila.esta_vazia())
        self.assertEqual(len(fila), 2)

    def teste_desenfileirar_comportamento_fifo(self):
        """O método desenfileirar deve remover os itens na ordem correta (FIFO)."""
        fila = Fila()
        fila.enfileirar("A")
        fila.enfileirar("B")
        fila.enfileirar("C")
        
        self.assertEqual(fila.frente(), "A")
        self.assertEqual(fila.desenfileirar(), "A")
        self.assertEqual(len(fila), 2)
        self.assertEqual(fila.desenfileirar(), "B")
        self.assertEqual(len(fila), 1)

    def teste_fluxo_dinamico_amortizado(self):
        """Testa se a fila suporta intercalar entradas e saídas mantendo a ordem."""
        fila = Fila()
        fila.enfileirar(1)
        fila.enfileirar(2)
        self.assertEqual(fila.desenfileirar(), 1)
        
        fila.enfileirar(3)
        self.assertEqual(fila.desenfileirar(), 2)
        self.assertEqual(fila.desenfileirar(), 3)
        self.assertTrue(fila.esta_vazia())

    def teste_excecoes_fila_vazia(self):
        """frente() e desenfileirar() devem levantar IndexError se a fila estiver vazia."""
        fila = Fila()
        
        with self.assertRaises(IndexError):
            fila.desenfileirar()
            
        with self.assertRaises(IndexError):
            fila.frente()


if __name__ == '__main__':
    unittest.main()