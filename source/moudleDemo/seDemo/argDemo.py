def say(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
    print('-' * 50)


say(123, 232, 3443, b=3, c=4)
d = {'b': 3, 'c': 4}
say(123, 232, 3443, **d)
e = (1, 2, 3)
say(20, *e, **d)

