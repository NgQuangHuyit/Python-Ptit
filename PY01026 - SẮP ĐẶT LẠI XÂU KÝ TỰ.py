for t in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()
    if s1 == s2:
        print('Test {}: YES'.format(t+1))
    else:
        print('Test {}: NO'.format(t+1))
