
def encode (password):
    encodedStr = ""

    for i in password:
        i = int(i)
        i += 3
        i = str(i)
        encodedStr += i

    return encodedStr


if __name__ == '__main__':

    password = '12345555'
    p = encode(password)
    print(p)

    print("hello test 2")
