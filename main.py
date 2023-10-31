
def encode (password):
    encodedStr = ""

    for i in password:
        i = int(i)
        if i < 7:
            i += 3
            i = str(i)
            encodedStr += i
        elif i >= 7:
            i += 3
            encodedStr += str(i)[-1]

    return encodedStr

def decoder(encodedStr):
    password = ''
    for num in encodedStr:
        num = int(num)
        num -= 3
        num = str(num)
        password += num
    return password


if __name__ == '__main__':
    userOpt = 1

    while userOpt != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        userOpt = int(input("Please enter an option: "))

        if userOpt == 1:
            password = input("Please enter your password to encode: ")
            ePass = encode(password)
            print("Your password has been encoded and stored!")
            print("")

        elif userOpt == 2:
            decoder(ePass)
            print(f'The encoded password is {ePass}, and the original password is {password}.')

