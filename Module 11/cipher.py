def encode():
    message = input("\nEnter a message to encode: ")
    message = message.replace('a','0')
    message = message.replace('b','1')
    message = message.replace('c','2')
    message = message.replace('d','3')
    message = message.replace('e','4')
    message = message.replace('f','5')
    message = message.replace('g','6')
    message = message.replace('h','7')
    message = message.replace('i','8')
    message = message.replace('j','9')
    message = message.replace('k','!')
    message = message.replace('l','@')
    message = message.replace('m','#')
    message = message.replace('n','$')
    message = message.replace('o','%')
    message = message.replace('p','^')
    message = message.replace('q','&')
    message = message.replace('r','*')
    message = message.replace('s','(')
    message = message.replace('t',')')
    message = message.replace('u','-')
    message = message.replace('v','+')
    message = message.replace('w','<')
    message = message.replace('x','>')
    message = message.replace('y','?')
    message = message.replace('z','=')

    print("Encoded message: {}".format(message))

def decode():
    message = input("\nEnter a message to decode: ")
    message = message.replace('0','a')
    message = message.replace('1','b')
    message = message.replace('2','c')
    message = message.replace('3','d')
    message = message.replace('4','e')
    message = message.replace('5','f')
    message = message.replace('6','g')
    message = message.replace('7','h')
    message = message.replace('8','i')
    message = message.replace('9','j')
    message = message.replace('!','k')
    message = message.replace('@','l')
    message = message.replace('#','m')
    message = message.replace('$','n')
    message = message.replace('%','o')
    message = message.replace('^','p')
    message = message.replace('&','q')
    message = message.replace('*','r')
    message = message.replace('(','s')
    message = message.replace(')','t')
    message = message.replace('-','u')
    message = message.replace('+','v')
    message = message.replace('<','w')
    message = message.replace('>','x')
    message = message.replace('?','y')
    message = message.replace('=','z')

    print("Decoded message: {}".format(message))


while True:
    print("\nWelcome to the Secret Message Encoder/Decoder")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")
    while True:
        answer = input("\nWhat would you like to do? ")
        if answer == '1':
            break
        elif answer == '2':
            break
        elif answer == '3':
            break
        elif answer == 'one':
            print("Please enter a number between 1 and 3.")
            continue
        elif answer == 'two':
            print("Please enter a number between 1 and 3.")
            continue
        elif answer == 'three':
            print("Please enter a number between 1 and 3.")
            continue
        else:
            print("{} is not a valid choice.".format(answer))
            continue

    if answer == '1':
        encode()
        continue
    elif answer == '2':
        decode()
        continue
    else:
        exit()
