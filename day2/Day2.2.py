with open("./input2.txt", "r") as f:
    input_data = f.readlines()


def controller():
    horizontal = vertical = aim = 0
    for line in input_data:
        control, value = line.split()
        if control == "forward":
            horizontal += int(value)
            vertical += aim*int(value)
        elif control == "up":
            aim -= int(value)
        elif control == "down":
            aim += int(value)
    print(horizontal * vertical)


controller()
