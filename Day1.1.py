with open("./inputs/input2.txt", "r") as f:
    input_data = f.readlines()


def controller():
    horizontal = vertical = 0
    for line in input_data:
        control, value = line.split()
        if control == "forward":
            horizontal += int(value)
        elif control == "up":
            vertical -= int(value)
        elif control == "down":
            vertical += int(value)
    print(horizontal * vertical)


controller()
