def fibonacci_sequence(n_param):

    n = n_param

    if n == 0: #Escenario base.
        return 0
    
    if n == 1: #Escenario recursivo.
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n-2)
