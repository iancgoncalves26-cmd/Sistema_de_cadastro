from connect_sql import Session,User
from pandas import DataFrame


def Buscar():
    email_busca = input('Digite o email da busca:').strip()
    try:
        with Session() as session:
            user_busca = session.query(User).filter_by(email = email_busca).first()
            usuarios={'id':user_busca.id,'nome':user_busca.nome,'idade':user_busca.idade,'email':user_busca.email}
            print(DataFrame([usuarios]))
        if user_busca is None:
            print('Usauario nao encontrado')
    except:
        return False