for t in range(int(input())):
    numbers = list(input())
    for i in range(len(numbers)):
        if numbers[i].isalpha():
            numbers[i] = ' '
    numbers = ''.join(numbers).split()
    numbers = [int(num) for num in numbers]
    print(max(numbers))
