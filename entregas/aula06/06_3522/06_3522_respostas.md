# Respostas - Prática 6

### Por que `desenfileirar` custa $O(N)$ no pior caso, mas tem complexidade amortizada de $O(1)$?

Em uma chamada isolada, o método `desenfileirar` pode custar **$O(N)$**. Isso acontece no cenário específico em que a pilha de saída (`sai`) está vazia e a pilha de entrada (`entra`) possui $N$ elementos. Para garantir que o item mais antigo fique no topo para ser removido, o algoritmo precisa iterar por todos os $N$ elementos da pilha de entrada, transferindo-os um por um para a pilha de saída. Como ele move $N$ itens, o custo dessa execução isolada é linear, $O(N)$.

No entanto, a complexidade é considerada **$O(1)$ amortizada (caso médio)** quando analisamos a jornada (o ciclo de vida) de cada elemento individualmente dentro da estrutura. A argumentação se baseia nas seguintes etapas:

1. **Entrada:** O elemento entra na fila com custo $O(1)$ (`push` na pilha de entrada).
2. **A Única Transferência:** O pulo do gato é que **cada elemento é transferido da pilha de entrada para a pilha de saída exatamente uma única vez** ao longo de toda a sua vida na estrutura. Depois que um elemento vai para a pilha de saída, ele nunca mais faz o caminho inverso. 
3. **Saída:** O elemento é finalmente removido com custo $O(1)$ (`pop` na pilha de saída).

Isso significa que, durante toda a existência de um elemento na Fila, o custo total das operações realizadas sobre ele é constante (1 entrada + 1 transferência + 1 saída). 

A operação pesada de transferência de $N$ elementos só ocorre esporadicamente. O custo alto dessa transferência é "diluído" (amortizado) pelas diversas retiradas consecutivas de custo $O(1)$ que acontecerão logo em seguida diretamente da pilha de saída. Ao dividirmos o esforço total pelo número de operações ao longo do tempo, o custo médio matemático por chamada do `desenfileirar` se consolida como uma constante, justificando o **$O(1)$ amortizado**.
