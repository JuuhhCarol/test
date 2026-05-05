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

def menor (a,i):
    if (a<i):
        return a
    else:
        return i
    
def par (a):
    return a % 2 == 0 

def quadrado (l,i):
    return l*i 

def triangulo (b,h):
    return b*h/2

def elipse (a,b):
    return 3,14 * a * b 

def metros (a):
    return a/100

def centimetros (a):
    return a*100

def litros (l):
    return l/1000

def mililitros (l):
    return l*1000



