from .cadastrar import cadastro
from .Listar import Listar
from .Buscar import Buscar
from .Remover import remove


def controle():
    '''
    Sistema de cadastros.
    1-Cadastra o usuario usando nome,idade e email,tambem faz a verificaçao de tais.
    2-Lista todos cadastros.
    3-Busca o usuario pelo email.
    4-Remove o usuario pelo email.
    5-Encerra o programa.
    '''
    while True:
        print(
            ' 1 - Cadastrar usuário\n',
            '2 - Listar usuários\n',
            '3 - Buscar usuário\n',
            '4 - Remover usuário\n',
            '5 - Sair'
        )
        user = int(input('\n:'))
        if user==1:
            if cadastro():
                print('Cadastro concluido!!')
        if user==2:
            Listar()
        if user==3:
            Buscar()
        if user==4:
            remove()
        if user==5:
            break