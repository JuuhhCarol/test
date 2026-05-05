def soma (a,i):
    return a+i 

def sub (a,i):
    return a-i

def mult (a,i):
    return a*i

def div (a,i):
    if i == 0:
        raise ValueError("não é possivel dividir por 0!")
    return a/i 