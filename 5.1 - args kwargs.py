arr1 = [1,2]
arr2 = [3,4]

arr3 = [*arr1, *arr2, 5, 6]
print(arr3)

dict1 = {
    'a': 1,
    'd': 4
}
dict2 = {
    'a': 3,
    'b': 2
}

print({**dict1, **dict2})