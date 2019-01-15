class UnicodeDemo:
    s = 'café'
    len(s)
    b = s.encode('utf8')
    len(b)
    bd = b.decode('utf8')
    print('-' * 100)

    cafe = bytes('café', encoding='utf_8')
    cafe_arr = bytearray(cafe)
    c0 = cafe[0]
    c1 = cafe[:1]
    c2 = cafe_arr[-1:]


if __name__ == '__main__':
    ud = UnicodeDemo()
    params = dir(ud)
    for i in params:
        if not i.startswith('__'):
            print('{:<15}: {}'.format(i, ud.__getattribute__(i)))
