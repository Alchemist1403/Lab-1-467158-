file = open('sequence.txt')
numbers = [float(number) for number in file]
file.close


LIGHT_GREEN = '\u001b[42m'
LIGHT_GREEN_SIGNS = '\u001b[32m'
END = '\u001b[0m'


Zero_to_five = []
Min_five_to_zero = []

for i in numbers:
    if 0 <= i <= 5:
        Zero_to_five.append(i)
    elif -5 <= i <= 0:
        Min_five_to_zero.append(i)


All_100 = len(Zero_to_five) + len(Min_five_to_zero)

Percent1 = round((len(Zero_to_five) / All_100) * 100)
Percent2 = round((len(Min_five_to_zero) / All_100) * 100)


print(f" {'\u001b[32m'}{'_'*100}{END} (100%)")
print(f"|\n|{LIGHT_GREEN}{' '*Percent1}{END} numbers from 0 to 5 ({Percent1}%)")
print(f"|\n|{LIGHT_GREEN}{' '*Percent2}{END} numbers from -5 to 0 ({Percent2}%)\n|")
