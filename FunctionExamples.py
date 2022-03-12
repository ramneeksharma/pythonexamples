import socket

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

print(Resolver)

resolve = Resolver()
print(resolve._cache)
print(resolve("google.com"))
print(resolve._cache)
print(resolve("google.com"))

'''
resolveTime = Resolver()
 = """
from FunctionExample import resolve
"""
print(timeit(setup = s, stmt = 'resolve("google.com")', number = 1))
print(timeit(setup = s, stmt = 'resolve("google.com")', number = 1))
'''

print(resolve.has_host("google.com"))
resolve.clear()
print(resolve.has_host("google.com"))

def sequence_class(immutable):
    return tuple if immutable else list

seq = sequence_class(immutable=True)
t = seq("Testing Instance Creation")
print(t)
print(type(t))
