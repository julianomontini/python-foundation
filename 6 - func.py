from functools import reduce

items = [1,2,3,4,5]

# pares = filter(lambda x: x % 2 == 0, items)
# dicts = map(lambda x: {'numero': x}, pares)

# pares = filter(lambda x: x % 2 == 0, items)
# print(sum(pares))

nomes = ['Juliano', 'Pedro', 'Antonio', 'Jose']
csv_nomes = reduce(lambda x, y: x + ',' + y, nomes)
print(csv_nomes)