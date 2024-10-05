import time

BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
RED = '\u001b[41m' 
LIGHT_GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'

g = 2
d = 8
for i in range(13):

    if i < 4:
        print(f"{" "*(6-i)*2}{LIGHT_GREEN}{" "*(2*(1+2*i))}{END}{" "*(2*(7-2*i))}{LIGHT_GREEN}{" "*(2*(1+2*i))}{END}")
    
    
    elif 4 <= i <= 5:
        print(f"{" "*2*(6-i)}{LIGHT_GREEN}{" "*(2*(9+2*i))}{END}")
    
    
    elif  i == 6:
        print(f"{LIGHT_GREEN}{" "*42}{END}")


    elif 7 <= i <= 8:
        print(f"{" "*2*(i-6)}{LIGHT_GREEN}{" "*(2*(33-2*i))}{END}")
    

    elif 9 <= i <= 12:
        print(f"{" "*(i-6)*2}{LIGHT_GREEN}{" "*(2*(i-g))}{END}{" "*(2*(i-d))}{LIGHT_GREEN}{" "*(2*(i-g))}{END}")
        g += 3
        d -=1