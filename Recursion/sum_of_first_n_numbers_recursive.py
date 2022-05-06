def sum_of_n(n_param):

    n=n_param

    if n == 1: #Escenario base.
        return 1
    
    else: #Esecenario recursivo.
        return n + sum_of_n(n - 1)

