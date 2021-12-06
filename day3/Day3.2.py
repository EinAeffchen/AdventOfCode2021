with open("./input3.txt", "r") as f:
    input_data = f.readlines()


def to_matrix(): 
    matrix = []
    for row in input_data:
        m_row = []
        for char in row[:-1]:
            m_row.append(char)
        matrix.append(m_row)
    return matrix

def most_common(matrix):
    result = list()
    for row in list(zip(*reversed(matrix))):
        count_0 = row.count("0")
        count_1 = row.count("1")
        if count_1>=count_0:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

def least_common(matrix):
    result = list()
    for row in list(zip(*reversed(matrix))):
        count_0 = row.count("0")
        count_1 = row.count("1")
        if count_1<count_0:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

def filter_down(filter, matrix, switch=False):
    reduced_matrix = matrix
    index = 0
    while len(reduced_matrix)>1 and index <= 12:
        if switch:
            filter = most_common(reduced_matrix)
        else:
            filter = least_common(reduced_matrix)
        reduced_matrix = [m_row for m_row in reduced_matrix if m_row[index] == filter[index]]
        index+=1
    return "".join(reduced_matrix[0])

matrix = to_matrix()
mc = most_common(matrix)
lc = least_common(matrix)
og_r = filter_down(mc, matrix)
cs_r = filter_down(lc, matrix, True)
print(int(og_r, 2)*int(cs_r, 2))

