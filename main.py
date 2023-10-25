
def encode (password):
    encodedStr = ""

    for i in password:
        i = int(i)
        i += 3
        i = str(i)
        encodedStr += i

    return encodedStr

def menu():
    print("Menu\n -------------\n 1. Encode\n 2. Decode\n 3. Quit\n")
    userOpt = int(input("Please enter an option: "))
    userPass = input("Please enter your password to encode: ")





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

        #if userOpt == 2:
            #decode(ePass)
            #print("The encoded password is " + ePass + ", and the original password is " + password + ".")
            #print("")

