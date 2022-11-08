''' Daily Coding Problem #158 Path Finding in a matrix '''


def find_paths_in_matrix(n, m):
    matrix = []
    for row in range(m):
        temp_row = []
        for index in range(n):
            temp_row.append(int(input(f"value index {index}: ")))
        matrix.append(temp_row)
    # Print matrix
    for r in matrix:
        print(r)
    # Finding the paths
    i = 1
    return 1


a = int(input('Enter n: '))
b = int(input('Enter m: '))
output = find_paths_in_matrix(a, b)

print(output)