def sum_even_columns(matrix):
    return [sum(row[i] for row in matrix) for i in range(len(matrix[0])) if i % 2 == 0]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    print("Суммы элементов столбцов с четными номерами:")
    print(sum_even_columns(matrix))