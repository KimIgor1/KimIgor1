def find_min_in_penultimate_column(matrix):
    if len(matrix) == 0 or len(matrix[0]) < 2:
        return None  # Матрица должна иметь хотя бы 2 столбца

    min_value = matrix[0][-2]
    for row in matrix:
        if row[-2] < min_value:
            min_value = row[-2]
    return min_value

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    min_value = find_min_in_penultimate_column(matrix)
    if min_value is not None:
        print("Минимальный элемент в предпоследнем столбце:", min_value)
    else:
        print("Матрица не имеет предпоследнего столбца")