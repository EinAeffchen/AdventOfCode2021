with open("./input4.txt", "r") as f:
    input_data = [line.strip for line in f.readlines()]


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
        result.append(max(set(row), key=row.count))
    return "".join(result)

def least_common(matrix):
    result = list()
    for row in list(zip(*reversed(matrix))):
        result.append(min(set(row), key=row.count))
    return "".join(result)

matrix = to_matrix()
mc = int(most_common(matrix), 2)
lc = int(least_common(matrix), 2)
print(mc*lc)

