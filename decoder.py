def decode(password):
    decoded = ''
    for char in password:
        digit = int(char)
        decoded += str(digit - 3 % 10)

    return decoded