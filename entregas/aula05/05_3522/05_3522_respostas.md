*Questão 1*
R: Uma possível organização das classes e subclasses trazidas seria:

Pessoa (Classe Base):
    -Funcionário (Subclasse):
        --Chefe de Cozinha (Subclasse_2)
        --Gerente (Subclasse_2)
        --Garçom (Sublcasse_2)

Assim, chefe de cozinha, gerente e garçom herdariam os atributos de funcionário (salario, carga_horaria) e por consequência de Funcionário ser subclasse de Pessoa, herdariam também os seus atributos (nome, idade). Já que as três classes (chefe_de__cozinha, gerente, garçom) são todos funcionários, que por sua vez são pessoas, essa definição faz sentido para melhor definição e implementação pois eles também trazem consigo seus métodos. Depois:

Restaurante (Classe Base):
    -Pizzaria (Subclasse):

Assim, Pizzaria herdaria os atributos de Restaurante (nome, endereço, telefone) ao passo que adicionaria o atributo de ser rodízio ou não. Não faria sentido inicial colocar a classe iguaria (comida), bolo ou pizza aqui, pois elas não necessitam do nome do restaurante, endereço ou telefone e nem adicionam novos métodos/atributos úteis. Por fim:

Iguaria - Comida (Classe Base):
    -Bolo (Subclasse):
    -Pizza (Subclasse):

Assim, pizza e bolo herdariam nome:str e preço, úteis a esses produtos, trazendo por sua vez características importantes dos produtos individualmente (respectivamente, borda_recheada:bool e formato:str).

*Questão 2*
R: Tendo a organização anterior, poderíamos modelar a hierarquia: 

Restaurante (Classe Base):
*Itens (Atributo novo de restaurante): list (lista onde se iteraria vários itens do tipo Iguaria)
    -Pizzaria (Subclasse):

Iguaria - Comida (Classe Base):
    -Bolo (Subclasse):
    -Pizza (Subclasse):

Assim, "Itens" pertenceria ao restaurante e seria responsável por armazenar varios itens da classe Iguaria, sendo possível sempre iterar mais comidas a cada restaurante.

Essa implementação por si só já tem uma capacidade interessante, semelhante a aplicativos de delivery de comida, onde cada produto está obrigatoriamente ligado a algum estabelecimento (que deve possuir nome, endereço e telefone), além dos filhos mais baixos de Iguaria terem atributos específicos de cada produto, contudo, tendo todos "nome do produto" e preço. Assim, poderia se aproveitar o máximo de atributos ao criar a relação entre Restaurante e Iguaria (passando por Itens).
