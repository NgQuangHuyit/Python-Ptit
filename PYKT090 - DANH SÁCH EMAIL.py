file = open('CONTACT.in', mode='r')
emailList = file.read().split(sep='\n')
for i in range(len(emailList)):
    emailList[i] = emailList[i].lower()
emailList = set(emailList)
emailList = list(emailList)
emailList.sort()
print(*emailList, sep='\n')
