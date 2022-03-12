scientists = ['Rosaline Franklin', 'William Gosset', 'Florence Nightingale',
                'Marie Curie', 'Rachel Carson', 'John Snow', 'Alan Turing', 'Johann Gauss']

print(sorted(scientists, key = lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]
print(last_name)
print(last_name('Thomas Edison'))

class NameSplitter:
    pass

class NameSplitterAdv:
    def __call__(self, name):
        return name.split()[-1]

ns = NameSplitter()
nsa = NameSplitterAdv()
print(nsa('Thomas Edison'))

print("Is sorted() callable: ", callable(sorted))
print("Is a \'lambda\' function callable: ", callable(last_name))
print("Is \'list\' callable: ", callable(list))
print("Is a classname callable: ", callable(NameSplitter))
print("Is a class instance callable: ", callable(ns))
print("Is a class instance callable: ", callable(nsa))