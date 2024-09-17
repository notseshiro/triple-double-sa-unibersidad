def pascal_triangle(n):
    pascal = [[1]]
    row = 1
    while row < n:
        new_row = [1]
        for i in range(1, row):
            new_row.append(pascal[row - 1][i - 1] + pascal[row - 1][i])
        new_row.append(1)
        pascal.append(new_row)
        row += 1

    for row in pascal:
        print(row)

n = int(input("Enter the number of rows for Pascal's triangle: "))
pascal_triangle(n)