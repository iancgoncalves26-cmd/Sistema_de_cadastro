


def filter_add(nome:str,idade:int,email:str) -> bool:
    if not all(letra for letra in nome if letra.isalpha()) and len(nome)<3:
        return False
    if idade<0 and idade>125:
        return False
    fatiamento = email.split('@')
    if len(fatiamento)!=2:
        return False
    if len(fatiamento[0])<4 or not any(letra for letra in fatiamento[0] if letra.isalpha()):
        return False
    if not 1!=len(fatiamento[1].split('.'))<=3:
        return False
    if not fatiamento[1].count('com')==1:
        return False
    return True
