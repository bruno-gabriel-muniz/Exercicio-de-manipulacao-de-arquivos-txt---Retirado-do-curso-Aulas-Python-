oi = 1
"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser
feita através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""


def le_espaço_usado(usuarios_txt):
    """
    Função que lê o arquivo usuário.txt e devolve o nome e o espaço utilizado
    em disco de cada funcionario separado em uma lista com sublistas dentro
    """
    # abrindo o arquivo que contem os dados
    arquivo_de_origem_dos_dados = open(usuarios_txt, "r")
    # criando a lista que vai conter os dados
    lista_com_os_dados = [["nome"+" "*12, "espaço utilizado", "porcentagem"]]
    # percorrendo toda as linhas do arquivo em um for loop
    for t in arquivo_de_origem_dos_dados:
        # pegando o nome da pessoa
        nome = t[0:16]
        # pegando o espaço ultilizado por ela
        espaço_utilizado = t[16:]
        # adicionando os dois dados na lista dos dados
        lista_com_os_dados.append([nome, espaço_utilizado])
    # retorna a lista com os espaços utilizados
    return lista_com_os_dados


def caucula_espaço_utilizado(lista_com_os_dados):
    """
    Função que converte os bytes de cada funcionario em mega bytes
    """
    # entrando na lista dos dados e passando em cada funcionario
    for funcionario in range(1, len(lista_com_os_dados)):
        # convertendo o valor de bytes para mega em
        # cada lista de cada funcionario
        lista_com_os_dados[funcionario][1] = float(
            lista_com_os_dados[funcionario][1]) / 1048576
    return lista_com_os_dados


def caucula_porcentagem_usada(lista_com_os_dados):
    """
    função que caucula a porcentagem de espaço
    usado em disco e adiciona na listta de usuários"""
    # criando uma variavel para conter o espaço tota usado
    espaco_total_usado = 0
    # passando por todos os espaços usados para somar a variavel total
    for soma in range(1, len(lista_com_os_dados)):
        # somando as variaveis
        espaco_total_usado += float(lista_com_os_dados[soma][1])
    # passando por todas as variaveis para caulcular a porcentagen
    for porcentagem in range(1, len(lista_com_os_dados)):
        # atribuindo ao final da lista de cada
        # usuário a porcentagem e cauculando ela
        lista_com_os_dados[porcentagem].append(
            float(lista_com_os_dados[porcentagem][1])/espaco_total_usado)
    # retornado a lista atualizada
    return lista_com_os_dados


def cria_relatorio(lista_com_os_dados):
    relatorio = open(
        "Relatorio dos espaços utilizado em disco pelos usuários", "w")
    for dados_da_linha in lista_com_os_dados:
        relatorio.write("oi")


lista_com_os_dados = caucula_porcentagem_usada(
    caucula_espaço_utilizado(le_espaço_usado("usuarios.txt")))
for olha in lista_com_os_dados:
    print(olha)
