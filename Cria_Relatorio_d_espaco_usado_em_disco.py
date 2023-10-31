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
    lista_com_os_dados = [["Nr. ", "nome"+" "*12,
                           "espaço utilizado", "porcentagem"]]
    # criando uma variável contadora para adicionar no relatório
    cont = 0
    # percorrendo toda as linhas do arquivo em um for loop
    for t in arquivo_de_origem_dos_dados:
        cont += 1
        # pegando o nome da pessoa
        nome = t[0:16]
        # pegando o espaço ultilizado por ela
        espaço_utilizado = t[16:]
        # adicionando os 3 dados na lista dos dados
        lista_com_os_dados.append([cont, nome, espaço_utilizado])
    # retorna a lista com os espaços utilizados
    return lista_com_os_dados, cont


def caucula_espaço_utilizado(lista_com_os_dados):
    """
    Função que converte os bytes de cada funcionario em mega bytes
    """
    # entrando na lista dos dados e passando em cada funcionario
    for funcionario in range(1, len(lista_com_os_dados)):
        # convertendo o valor de bytes para mega em
        # cada lista de cada funcionario
        lista_com_os_dados[funcionario][2] = float(
            lista_com_os_dados[funcionario][2]) / 1048576


def caucula_porcentagem_usada(lista_com_os_dados):
    """
    função que caucula a porcentagem de espaço
    usado em disco e adiciona na listta de usuários"""
    # criando uma variavel para conter o espaço tota usado
    espaco_total_usado = 0
    # passando por todos os espaços usados para somar a variavel total
    for soma in range(1, len(lista_com_os_dados)):
        # somando as variaveis
        espaco_total_usado += float(lista_com_os_dados[soma][2])
    # passando por todas as variaveis para caulcular a porcentagen
    for porcentagem in range(1, len(lista_com_os_dados)):
        # atribuindo ao final da lista de cada
        # usuário a porcentagem e cauculando ela
        lista_com_os_dados[porcentagem].append(
            float(lista_com_os_dados[porcentagem][2])/espaco_total_usado)
    # retornando o espaço total usado para fazer a analize
    return espaco_total_usado


def cria_relatorio(lista_com_os_dados):
    """
    Essa função cria o relatório do espaço utilizado em disco pelos usuários
    esta so pernche os dados que serão dados por outras funções
    """
    # criando o arquivo do relatório
    relatorio = open(
        "Espaços utilizado em disco pelos usuários.txt", "w")
    # escrevendo o rítulo do relatório
    relatorio.write(
        "ACME Inc.          Uso do espaço em disco pelos usuários \n" + "-"*35
        + "\n")
    # mostrando o que cada coluna representa
    relatorio.write("\n" +
                    lista_com_os_dados[0][0]
                    + lista_com_os_dados[0][1]+" " + "--" +
                    lista_com_os_dados[0][2] + "--"
                    + lista_com_os_dados[0][3]+"\n"+"\n")
    # passando por todas as listas dos usuários e mostrando os dados
    for dados_da_linha in range(1, len(lista_com_os_dados)):
        # imprimindo o nome o número,o espaço usado e a porcentagem dele
        relatorio.write(
            "%3i %s -- %12.2f GB-- %8.2f %% \n"
            % (lista_com_os_dados[dados_da_linha][0],
               lista_com_os_dados[dados_da_linha][1],
               lista_com_os_dados[dados_da_linha][2],
               lista_com_os_dados[dados_da_linha][3]*100))


def faz_analise(total_do_espaço_usado, n_usuários):
    """
    Função que mostra a média e o total de megabytes usados pelos usuários
    """
    # abrindo o relatório para adicionar a média e o total do espaço usado
    relatorio = open("Espaços utilizado em disco pelos usuários.txt", "a")
    # mostrando o espaço total usado
    relatorio.write("\n"+"Espaço total ocupado: %.2f MB\n"
                    % (total_do_espaço_usado))
    # mostrando o espaço médio usado
    relatorio.write("Espaço médio ocupado: %.2f MB"
                    % (total_do_espaço_usado/n_usuários))


def relatorio_do_espaço_usado():
    # lendo os espaços usados pelos usuário e quantos usuário
    # usaram o disco
    lista_com_os_dados, cont = le_espaço_usado("usuarios.txt")
    # transformando os bytes em mega bytes
    caucula_espaço_utilizado(lista_com_os_dados)
    # cauculando a porcentagem do disco usada
    # pelos usuário e pegando o total usado
    total_do_espaco_usado = caucula_porcentagem_usada(lista_com_os_dados)
    # criando o relatório com os dados gerais
    cria_relatorio(lista_com_os_dados)
    # terminando a parte da análise do relatório
    faz_analise(total_do_espaco_usado, cont)


relatorio_do_espaço_usado()
