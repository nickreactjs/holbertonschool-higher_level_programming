#!/usr/bin/python3
matrix_divided = __import__("2-matrix_divided").matrix_divided

matrix = [
    [1, 2, 3],
    [4, 4, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
