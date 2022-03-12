def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

def northern_city():
    return 'Troms⍥'

print(northern_city())

@escape_unicode
def northern_city():
    return 'Troms⍥'

print(northern_city())

class CallCount:
    def __init__(self, f):
        self._f = f
        self._count = 0
    
    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}!'.format(name))

hello('Fred')
hello('John')
hello('Betty')
print(hello._count)

class Trace:
    def __init__(self):
        self._enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self._enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

def rotate_list(l):
    return l[1:] + [l[0]]

al = [1, 2, 3] 
print(al)
al = rotate_list(al)
print(al)
al = rotate_list(al)
print(al)
al = rotate_list(al)
print(al)

aTrace = Trace()
@aTrace
def rotate_list(l):
    return l[1:] + [l[0]]

al = [1, 2, 3] 
print(al)
al = rotate_list(al)
print(al)
al = rotate_list(al)
print(al)
al = rotate_list(al)
print(al)

aTrace._enabled = False
print(al)
al = rotate_list(al)
print(al)
al = rotate_list(al)
print(al)
al = rotate_list(al)
print(al)