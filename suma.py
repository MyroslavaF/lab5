def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return a / b
    

if __name__ == "__main__":
    print(sumar(3, 5));
    print(restar(5, 3));
    print(multiplicar(3, 5));
    print(dividir(-6, 0));
