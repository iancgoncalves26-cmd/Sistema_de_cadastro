from connect_sql import Session,User
from dd_filter import filter_add

def cadastro():
    nome_user = input('Digite o nome inteiro:').strip()
    idade_user=int(input('Digite a idade:'))
    email_user = input('Digite o email:').strip()
    validador=filter_add(nome=nome_user,idade=idade_user,email=email_user)
    if not validador:
        print('Dados digitados de maneira incorreta')
        return False
    with Session() as session:
                    
        novo_user = User(
            nome = nome_user,
            idade = idade_user,
            email = email_user
        )
        session.add(novo_user)
        session.commit()
    return True