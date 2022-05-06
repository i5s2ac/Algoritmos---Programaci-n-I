def factorial(n_param):

    n=n_param

    if n == 0: #Escenario base.
        return 1
    
    else: #Esecenario recursivo.
        return n * factorial(n - 1)

