RED_SIGNS = '\u001b[31m'
RED = '\u001b[41m' 
LIGHT_GREEN_SIGNS = '\u001b[32m'
END = '\u001b[0m'


for i in range(10): 

    if i == 0:                            
        print (f"{LIGHT_GREEN_SIGNS}  ^")

    elif i == 9:
        print(f"{LIGHT_GREEN_SIGNS}  |\n{10-i} {RED_SIGNS}*")

    else:
        print(f"{LIGHT_GREEN_SIGNS}  |\n{10-i} *{' '*((10-i-1)*5-1)}{RED_SIGNS}*")

        
print(f"{LIGHT_GREEN_SIGNS}  |\n0 * {"—— * "*9}——>")
print(f"{LIGHT_GREEN_SIGNS} {' '*6}1{' '*4}2{' '*4}3{' '*4}4{' '*4}5{' '*4}6{' '*4}7{' '*4}8{' '*4}9")