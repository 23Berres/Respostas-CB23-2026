from P06_3522_pilha_encadeada import PilhaEncadeada as Pilha

class FilaEncadeada():

    def __init__(self):
        """Define duas filas com topos, uma de entrada e outra de saída."""

        self.entra = Pilha()
        self.sai = Pilha()

    def enfileirar(self,item):
        """Coloca os itens no topo da entrada. Fim da Fila.

        Complexidade: O(1)

        Justificativa: O método apenas repassa o item diretamente para o método push da pilha de entrada, 
        que possui custo constante."""

        self.entra.push(item)

    def desenfileirar(self):
        """Transfere todos os itens da pilha de entrada pra uma nova pilha invertida de saída.
        
        Complexidade: O(1) amortizada (Pior caso: O(N))

        Justificativa: No pior caso (quando a pilha de saída está vazia), 
        o método precisa transferir todos os N elementos, custando O(N). 
        Contudo, cada elemento da fila sofre essa transferência de uma pilha para a outra apenas 
        uma única vez em toda a sua vida útil. O custo dessa transferência pesada é diluído 
        entre as várias operações imediatas de pop subsequentes, resultando em um custo médio (amortizado) de O(1) por operação."""

        if self.sai.esta_vazia() and self.entra.esta_vazia():
            raise IndexError("Não há nada nem ninguém na fila.")
        
        elif self.sai.esta_vazia():
            while not self.entra.esta_vazia():
                self.sai.push(self.entra.pop())
        
        return self.sai.pop()
        
    def frente(self):
        """Retorna o topo da pilha de Saída se houver. Do contrário, levanta IndexError.
        
        Complexidade: O(1) amortizada (Pior caso: O(N))

        Justificativa: Segue a mesma lógica do desenfileirar. A transferência em lote (O(N)) só 
        ocorre ocasionalmente, tornando a visualização do primeiro da fila 
        uma operação de custo constante na média das execuções."""
    
        if self.sai.esta_vazia() and self.entra.esta_vazia():
            raise IndexError("Não há nada nem ninguém na fila.")
        
        elif self.sai.esta_vazia():
            while not self.entra.esta_vazia():
                self.sai.push(self.entra.pop())

        return self.sai.topo()
            

    def esta_vazia(self):
        """Chama esta_vazia que já foi herdada, retornando True ou False.
        
        Complexidade: O(1)

        Justificativa: Realiza apenas uma avaliação booleana (operador and) conectando 
        dois métodos de verificação instantânea das pilhas."""

        return self.entra.esta_vazia() and self.sai.esta_vazia()

    def __len__(self):
        """Retorna o tamanho da fila de entrada.
        
        Complexidade: O(1)

        Justificativa: Efetua uma soma simples matemática dos tamanhos mantidos 
        incrementalmente por ambas as pilhas, sem iterar por nenhum elemento."""

        return self.entra.__len__() + self.sai.__len__()
    
    def __repr__(self):
        """Retorna a representação da fila de saída

        Complexidade: O(N)

        Justificativa: Independentemente de a pilha de saída já estar pronta ou precisar 
        de uma transferência prévia (ambos processos de custo linear), 
        a montagem da string exige percorrer e concatenar todos os N elementos presentes na estrutura."""
        
        if self.sai.esta_vazia() and self.entra.esta_vazia():
            return "* *"
        
        elif self.sai.esta_vazia():
            while not self.entra.esta_vazia():
                self.sai.push(self.entra.pop())

        return self.sai.__repr__()