def func(argument):
    lista = []
    if type(argument) == list: 
        for c in argument:
            if len(c) > 5:
                lista.append(c)
    return lista