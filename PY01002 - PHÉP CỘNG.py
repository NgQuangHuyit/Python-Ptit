arg1, o, arg2, equal, res = input().split()
exec('rres = ' + arg1 + o + arg2)
if int(res) == rres:
    print("YES")
else:
    print('NO')
    