from connect_sql import Session,User
from pandas import DataFrame


def remove():
    remov_user = input('Digite o email do user que deseja excluir:')
    try:
        with Session() as session:
            session.delete(remov_user)
            session.commit()
    except:
        return False