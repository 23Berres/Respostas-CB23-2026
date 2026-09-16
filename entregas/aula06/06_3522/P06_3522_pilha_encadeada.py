class _No():
    """Guarda o valor e o próximo a esse item.
    Isso cria os atributos necessários pras manipulações em PilhaEncadeada."""

    def __init__(self,vale,prox):
        self.valor = vale
        self.proximo = prox

class PilhaEncadeada():
    """Classe que define a pilha.
    Define os atributos do topo e da quantia total de itens"""

    def __init__(self):
        self.topinho = None
        self.quantia = 0

    def push(self,item):
        """Adiciona um ao valor de itens e redefine o topo como o item a ser adicionado,
        atribuindo a esse item a classe _No e o anteriomente item do topo como atributo proximo.
        
        Complexidade: O(1)
    
        Justificativa: A inserção ocorre diretamente no início da estrutura. 
        O método apenas cria um novo nó e reatribui a referência do ponteiro do topo, sem precisar percorrer os elementos existentes."""

        self.quantia += 1
        self.topinho = _No(item,self.topinho)

    def pop(self):
        """Confere se há algo no topo.
        Caso não, levanta IndexError.
        
        Caso haja, diminui a quantia total de itens em 1, guarda o topo atual, 
        atualiza o topo para o item abaixo e retorna a informação guardada.
        
        Complexidade: O(1) 
        
        Justificativa: A remoção lida apenas com o nó do topo. 
        O método acessa o valor, atualiza a referência do topo para 
        o próximo nó e decrementa o contador, tudo de forma direta e sem iterações."""

        if self.topinho == None:
            raise IndexError("A pilha está vazia.")
        else:
            self.quantia -= 1
            algo = self.topinho.valor
            self.topinho = self.topinho.proximo
            return algo

    def topo(self):
        """Se o topo não tem nenhum prato, levanta IndexError.
        Do contrário, retorna o atual topo.
        
        Complexidade: O(1)
        
        Justificativa: Acessa diretamente a variável que guarda a referência do topo da pilha, 
        retornando seu valor instantaneamente."""

        if self.topinho == None:
            raise IndexError("A pilha está vazia.")
        else:
            return self.topinho.valor

    def esta_vazia(self):
        """Retorna True ao caso de estar vazia e False ao caso de não estar.
        
        Complexidade: O(1)
        Justificativa: Realiza apenas uma avaliação booleana simples em cima do atributo interno de quantidade, 
        que já está armazenado e atualizado na memória."""

        return self.quantia == 0
        
    def __len__(self):
        """Retorna a quantia de itens na pilha, como ela começa vazia, retorna 0 neste caso.
        
        Complexidade: O(1)
        
        Justificativa: Como o contador self.quantia é atualizado a cada inserção e remoção (mantido incrementalmente), 
        o método precisa apenas retornar esse número armazenado, em vez de percorrer a lista contando os nós um a um."""

        return self.quantia
    
    def __repr__(self):
        """Se não há topo, retorna "* *" como string.
        Caso haja topo, confere se há próximo item. Caso não haja, retorna apenas o item único entre asteriscos.
        Caso haja próximo, retorna concatenado(s) o item inicial e os próximos separados por espaço, finalizando e começando em asterisco.
        
        Complexidade: O(N)
        
        Justificativa: Para montar a representação visual completa, o laço while precisa obrigatoriamente percorrer todos os N elementos 
        presentes na pilha, concatenando seus valores um a um até chegar ao fundo."""
        
        if self.topinho == None:
            return "* *"
        
        else:
            n = self.quantia -1
            string = "* " + str(self.topinho.valor)+" "

            if self.topinho.proximo == None:
                return string + " *"
            
            else:
                adiante = self.topinho.proximo

            while n !=0:
                string += str(adiante.valor)+" "
                adiante = adiante.proximo
                n-=1
            return string + " *"