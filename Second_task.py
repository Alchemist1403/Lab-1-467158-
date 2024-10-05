import os
import time

BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
RED = '\u001b[41m' 
LIGHT_GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'

Colors = [RED,YELLOW,LIGHT_GREEN]


while True:
    for color in Colors:
        g = 2
        d = 8
        for i in range(13): 

            if i < 4:
                print(f"{" "*(6-i)*2}{color}{" "*(2*(1+2*i))}{END}{" "*(2*(7-2*i))}{color}{" "*(2*(1+2*i))}{END}")
            
            
            elif 4 <= i <= 5:
                print(f"{" "*2*(6-i)}{color}{" "*(2*(9+2*i))}{END}")
            
            
            elif  i == 6:
                print(f"{color}{" "*42}{END}")


            elif 7 <= i <= 8:
                print(f"{" "*2*(i-6)}{color}{" "*(2*(33-2*i))}{END}")
            

            elif 9 <= i <= 12:
                print(f"{" "*(i-6)*2}{color}{" "*(2*(i-g))}{END}{" "*(2*(i-d))}{color}{" "*(2*(i-g))}{END}")
                g += 3
                d -=1
        time.sleep(2)
        os.system("cls")
    time.sleep(2)