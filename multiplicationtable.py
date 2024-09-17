def multiplication_table(n):
    row = 1
    while row <= n:
        col = 1
        while col <= n:
            print(f"{row * col:3}", end=" ")
            col += 1
        print()
        row += 1

n = int(input("Enter the size of the multiplication table: "))
multiplication_table(n)