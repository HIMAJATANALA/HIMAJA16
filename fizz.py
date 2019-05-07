def list_multiple(n):
    l = []
    for i in range(1,n):
        str = ''
        if i % 3 == 0:
            str += 'FIZZ'
        if i % 5 == 0:
            str += 'BUZZ'
        if i % 7 == 0
             str += "duzz"
        if len(str) != 0:
            l.append(str)
        else:
            l.append(i)
    return l

num = int(input())
print(list_multiple(num))


