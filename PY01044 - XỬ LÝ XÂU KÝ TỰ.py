set1 = set(input().lower().split())
set2 = set(input().lower().split())
union = list(set1.union(set2))
union.sort()
union = ' '.join(union)
inter = list(set1.intersection(set2))
inter.sort()
inter = ' '.join(inter)
print(union, inter, sep='\n')
'''
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
'''