def func(argument):
    lista = []
    if type(argument) == list: 
        for c in argument:
            if len(c) > 5:
                lista.append(c)
    return lista

def getchar(palavra):
    l = []
    for i in palavra:
        if 'h' in i:
            l.append(i)
    return l