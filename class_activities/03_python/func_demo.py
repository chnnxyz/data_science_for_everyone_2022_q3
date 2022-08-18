from ast import Raise


def freefall(t, y_start = 0):
    G = 9.81
    if not isinstance(t,list):
        raise TypeError('t no es una lista y debe serlo')
    y_start = float(y_start)

    y = [y_start - G * (t_i ** 2)/2 for t_i in t]
    
    output = dict()
    output['t'] = t
    output['y'] = y
    return output
