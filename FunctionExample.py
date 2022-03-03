import socket
from timeit import timeit

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


resolver = Resolver()
print(resolver._cache)
print(timeit(stmt="resolver(\"google.com\")", number = 1))
print(resolver("google.com"))
print(resolver._cache)
print(resolver("google.com"))
