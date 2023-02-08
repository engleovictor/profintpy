
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def somadosn_nesimos(n):
    if n == 1:
        return 1
    else:
        return n**n + somadosn_nesimos(n-1)

def soma(a,b):
    return a+b

def printar():
    return 'Velame!!'

