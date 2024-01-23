file_name = input()
file_format = file_name[-3:].casefold()
ok = True
for i in range(len(file_name)):
    if (not file_name[i].isalpha()) and (file_name[i] not in ['_', '.']):
        ok = False
        break
if ok and file_format == '.py':
    print('yes')
else:
    print('no')
