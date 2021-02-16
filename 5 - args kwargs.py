def soma(a, b):
    return a + b

args = (3,5)
print(soma(*args))

kwargs = {
    'b': 2,
    'a': 3
}

print(soma(**kwargs))

args_1 = (3,)
kwargs_1 = {'b': 10}
print(soma(*args_1, **kwargs_1))
