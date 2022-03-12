def double(n):
       return n*n

kval = {'foo': {'a': 4, 'b': 3}, 
        'bar': {'c': 5, 'd': 8},
        'baz': {'e': 8, 'f': 7}}

# Square of each value
#{'foo': {'a': 16, 'b': 9},
# 'bar': {'c': 25, 'd': 64},
# 'baz': {'e': 64, 'f': 49}}

k = {}
for k1, k2 in kval.items():
    l = {}
    for k3, k4 in k2.items(): 
        l[k3] = double(k4)
    k[k1] = l

print({k1: {k2: double(v2) for k2, v2 in v1.items()} for k1, v1 in kval.items()})

def func(num):
    res = '*'
    for _ in range(num):
        print(_)
        res += res
    return res
 
print(func(2))
 
for x in func(2):
    print(x, end='')