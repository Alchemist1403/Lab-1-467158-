BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
RED = '\u001b[41m' 
LIGHT_GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'


for i in range(8):
    if i <= 3:
        print(f"{LIGHT_GREEN}{' '*12}{YELLOW}{' '*18}{END}")
    else:
        print(f"{LIGHT_GREEN}{' '*12}{RED}{' '*18}{END}")


