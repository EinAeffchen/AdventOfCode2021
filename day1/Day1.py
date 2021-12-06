with open("./input1.txt", "r") as f:
    input_data = f.readlines()
print(sum([True for i, line in enumerate(input_data) if (i>0 and int(line) > int(input_data[i-1]))]))