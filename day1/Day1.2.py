with open("./input1.txt", "r") as f:
    input_data = f.readlines()


def three_stepper():
    dataset = []
    int_data = [int(number) for number in input_data]
    for i, row in enumerate(int_data):
        if i+2<len(int_data):
            dataset.append(sum(int_data[i:i+3]))
    return dataset

data = three_stepper()
print(sum([True for i, line in enumerate(data) if (i>0 and int(line) > int(data[i-1]))]))
