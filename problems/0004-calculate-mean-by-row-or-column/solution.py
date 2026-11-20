def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n_columns = len(matrix[0])
    means = []
    if mode == 'row':
        for row in matrix:
            mean = sum(row) / len(row)
            means.append(mean)
    else:
        for i in range(n_columns):
            column = [row[i] for row in matrix]
            mean = sum(column) / len(column)
            means.append(mean)
    return means