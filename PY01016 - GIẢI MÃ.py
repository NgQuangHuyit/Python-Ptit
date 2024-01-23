for t in range(int(input())):
    encoded_str = input()
    decoded_str = ''
    for i in range(0, len(encoded_str), 2):
        decoded_str += encoded_str[i] * int(encoded_str[i+1])
    print(decoded_str)
