import time 


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, lenght=1, color=222):
    line = ' ' * lenght
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")


def draw_romb():
    size = 15
    center = size // 2
    offset = size // 2

    step = 1
    lenght = 1

    # print(size, center, offset)

    colors = [125,173,227,119,15,21,93]


    while True:
        for color in colors:
            for line in range(size):

                draw_line(offset, lenght, color)

                if line < center:
                    offset -= step
                    lenght += step * 2
                else:
                    offset += step
                    lenght -= step*2
            
            print(f"\x1b[{size+2}A")
            print(f"\x1b[{offset}D")

            lenght = 1
            offset = size // 2

            time.sleep(2)

for i in range(256):
     print(f"{i}--{SET_COLOR}{i}m")

if __name__ ==  "__main__":
    draw_romb()

# for i in range(20):
#     draw_line(lenght=40, color=47, offset=i)
#     print(f"{CLEAR}")
#     time.sleep(0.3)



