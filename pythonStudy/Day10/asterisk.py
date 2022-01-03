# * : 변수 앞에 붙은 경우 *args, **kwagrs => 언패킹

def astrick_test1(a, *args):
    print(a, args)
    print(type(args))

def astrick_test2(a, *args):
    print(a, *args)
    print(type(args))

astrick_test1(1,2,3,4,5)
astrick_test2(1,2,3,4,5)

a, b, c = ([1,2,3], [3,4,5], [5,6,7])
print(a,b,c)
data = ([1,2,3], [3,4,5], [5,6,7])
print(data,'\n',*data)

def astrick_test3(a, **kwargs):
    print(a, kwargs)
    print(type(kwargs))

astrick_test3(1,b=2, c=3, d=4, e=5)

data2 = {'b': 2, 'c': 3, 'd': 4, 'e': 5}
astrick_test3(1, **data2)