num = input()
while len(num) > 1:
    num1 = int(num[:int(len(num)/2)])
    num2 = int(num[int(len(num)/2):])
    num = str(num1 + num2)
    print(num)
