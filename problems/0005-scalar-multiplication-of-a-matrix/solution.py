def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    result = []
    for row in matrix:
        new_row = []
        for column in row:
            new_row.append(column*scalar)
        result.append(new_row)
    return result
    pass