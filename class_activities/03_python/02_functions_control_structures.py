# Definir una función que genere la media aritmetico-geometrica
def arithmetic_mean(x:float, y:float) -> float:
    '''
    Calcula la media aritmetica
    :param x: primer numero
    :param y: segundo numero

    :returns: media aritmetica
    '''
    return (x+y)/2

def geometric_mean(x:float, y:float) -> float:
    '''
    Calcula la media geometrica
    :param x: primer numero
    :param y: segundo numero

    :returns: media geometrica
    '''
    return (x * y) ** (1/2)

def agm(a:float, b:float) -> float:
    '''
    Calcula la media aritmético geométrica de dos funciones
    :param a: primer numero
    :param b: segundo numero

    :returns: media aritmetico geometrica
    '''
    # Obtener el valor grande y chico
    smaller = min([a,b])
    larger = max([a,b])
    # Obtener la diferencia entre 
    difference = abs(smaller-larger)

    while difference > 0.000000000001:
        #nuevo numero grande es la media aritmetica
        larger = arithmetic_mean(smaller, larger)
        #nuevo numero chico es la media geometrica
        smaller = geometric_mean(smaller, larger)
        #obtener la diferencia 
        difference = abs(smaller-larger)
    
    #elegir cualquiera de ambos valores como valor de retorno

    return smaller