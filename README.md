# python_ex02


1- Como organizar modelos em módulos? Resposta: para organizar os modelos em módulos podemos criar uma classe que descreve como o modelo será implementado. Para criar modelos com herança podemos receber como parâmetro o atributo Model de models, por exemplo. Os tipos que models.Model oferecem são por exemplo: - CharField, FileField, FloatField, JSONField, TimeField, etc.

2- O que é, para quê serve e como usar um Proxy no modelo? O Proxy serve por exemplo, para criar, excluir e atualizar instâncias do modelo proxy e ainda assim salvar todos os dados como se estivessemos usando o modelo original (sem proxy [proxy=False]). A diferença é que podemos alterar coisas como a ordem do modelo padrão ou o gerenciador padrão no proxy, sem ter que alterar o original. Os modelos proxy são declarados como modelos normais. Dizemos ao Django que é um modelo proxy atributo da classe Meta para True.

3- O que faz o método str() em uma classe? É um método "mágico" do Python que define o que deve ser retornado se você chamar str() sobre um objeto. O Django usa str(obj) em vários lugares, mais notavelmente como um valor mostrado para renderizar um objeto no site de administração do Django e como valores inseridos em um template quando é mostrado um objeto. Por isso, que você deve sempre retornar uma string, legível para humanos, dos métodos str.

4- Quais são e para que servem as propriedades adicionais dos tipos de relacionamento/mapeamento?

- Relacionamento 1-1 (OneToOneField) Assim como o próprio nome supuõe, o relacionamento 1-1 define que um item de uma entidade só poderá se relacionar com um item de outra entidade. Por exemplo, um departamento só pode ter uma chefia, assim como cada chefe só pode chefiar um departamento.

- Relacionamento 1N (ForeignKey) O relacionamento 1N determina que um item de uma tabela pode se relacionar com vários itens de uma outra tabela. Por exemplo, uma pessoa pode passar por diversos departamentos, porém ela só pode ter um departamento atual.

- Relacionamento NN (ManyToManyField) O relacionam define que um item de uma tabela pode se relacionar com vários itens de uma outra tablea e vice-versa. Por exemplo, uma pessoa pode ser vinculada a diversos departamentos e departamentos podem ter várias pessoas.
