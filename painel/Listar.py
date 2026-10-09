from connect_sql import Session,User
from pandas import DataFrame

def Listar():
    all_user = []
    with Session() as session:
        user = session.query(User).all()
        for users in user:
            usuarios={'id':users.id,'nome':users.nome,'idade':users.idade,'email':users.email}
            all_user.append(usuarios)
                
        print(DataFrame(all_user)) 