def list_multiple(n):
    l = []
    for i in range(1,n):
        str = ''
        if i % 3 == 0:
            str += 'FIZZ'
        if i % 5 == 0:
            str += ' BUZZ'
        if len(str) != 0:
            l.append(str)
        else:
            l.append(i)
    return l

a = int(input())
print(list_multiple(a))


