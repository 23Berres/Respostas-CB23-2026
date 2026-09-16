# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exactamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs():

        maze[1][1] = room

        pilha = [(0,0)]

        while pilha:
            random.shuffle(directions)
            a,b = pilha[-1]
            for dx, dy in directions:
                nx, ny = a + dx, b + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    pilha.append((nx,ny))
                    maze[2 * a + 1 + dx][2 * b + 1 + dy] = room
                    maze[2*nx+1][2*ny+1] = room
                    break
            else: 
                pilha.pop(-1)

    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs()
    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * n))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break
        
    return maze

    

def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))


def rato_procura(maze, passo, m, n, room=' ', wall='\u25A3', cheese='*'):
    """Função criada pra representar a busca do rato.

    Rcebe como parâmetros um novo símbolo chamado 'passo', a maze criada e os mesmos usados em generate_maze.
    
    Após o rato achar a rota, ele marca o queijo com '@' e e o caminho com 'x'."""
    
    if maze[1][1] == cheese:
        maze[1][1] = "@"
        return maze
    
    maze[1][1] = passo
    pilha = [(0,0)]
    visitados = {(0,0)}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pilha:
        random.shuffle(directions)
        a, b = pilha[-1]
        
        for dx, dy in directions:
            nx, ny = a + dx, b + dy
            
            if 0 <= nx < m and 0 <= ny < n:
                corredor_x, corredor_y = 2 * a + dx + 1, 2 * b + dy + 1
                sala_x, sala_y = 2 * nx + 1, 2 * ny + 1
                
                achou_no_corredor = (maze[corredor_x][corredor_y] == cheese)
                achou_na_sala = (maze[sala_x][sala_y] == cheese and maze[corredor_x][corredor_y] != wall)

                if achou_no_corredor or achou_na_sala:
                    if achou_na_sala:
                        pilha.append((nx, ny))
                        
                    for i in range(len(pilha) - 1):
                        c1, d1 = pilha[i]
                        c2, d2 = pilha[i + 1]
                        maze[2 * c1 + 1][2 * d1 + 1] = passo
                        maze[c1 + c2 + 1][d1 + d2 + 1] = passo
                        
                    ultimo_c, ultimo_d = pilha[-1]
                    
                    if achou_na_sala:
                        maze[2 * ultimo_c + 1][2 * ultimo_d + 1] = '@'
                    else:
                        maze[2 * ultimo_c + 1][2 * ultimo_d + 1] = passo
                        maze[corredor_x][corredor_y] = '@'
                        
                    return maze

                elif maze[sala_x][sala_y] == room and (nx, ny) not in visitados and maze[corredor_x][corredor_y] != wall:
                    pilha.append((nx, ny))
                    visitados.add((nx, ny))
                    break          
        else: 
            pilha.pop(-1)
            
    return maze

# Example usage:
if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)
    maze = generate_maze(m, n)
    print('Maze 1')
    print_maze(maze)

    room = ' '
    wall = '\u25A3'
    cheese = '*'
    passo = 'x'
    maze = generate_maze(m, n, room, wall, cheese)
    maze = rato_procura(maze,passo,m,n,room, wall, cheese)
    print('\nMaze 2')
    print_maze(maze)

