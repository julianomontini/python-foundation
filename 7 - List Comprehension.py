numeros_pares = [
    (x*3) for x in range(101)
    if (x*3) % 2 == 0 and (x*3) < 100
]
print(numeros_pares)

numeros_pares_tup = (x*3 for x in range(101) if (x*3) % 2 == 0)
print(tuple(numeros_pares_tup))

numeros = {x: x % 2 == 0 for x in range(100)}
print(numeros)