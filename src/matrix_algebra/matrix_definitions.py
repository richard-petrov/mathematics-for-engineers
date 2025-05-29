a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

def matrix_addiition(
        matrix_a: list,
        matrix_b: list):
    """
    Adds two matrices together if they have the same dimensions.

    Parameters:
    - matrix_a (list): The first matrix.
    - matrix_b (list): The second matrix.
    """
    len_rows_a = len(matrix_a[0])
    len_rows_b = len(matrix_b[0])

    len_columns_a = len(matrix_a)
    len_columns_b = len(matrix_b)

    return len_rows_a == len_rows_b and len_columns_a == len_columns_b

print(matrix_addiition(a, b))