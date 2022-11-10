def process_item(x):
    import sympy.ntheory as nt
    try:
        x = int(x)
    except:
        print("Input not valid. Insert a number!")
        return
    x_cpy = x+1
    while not nt.isprime(x_cpy):
        x_cpy += 1
    return x_cpy