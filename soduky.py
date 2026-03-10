soduku  = [5, 3, 4, 6, 7, 8, 9, 1, 2]
soduku1 = [6, 7, 2, 1, 9, 5, 3, 4, 8]
soduku2 = [1, 9, 8, 3, 4, 2, 5, 6, 7]
soduku3 = [8, 5, 9, 7, 6, 1, 4, 2, 3]
soduku4 = [4, 2, 6, 8, 5, 3, 7, 9, 1]
soduku5 = [7, 1, 3, 9, 2, 4, 8, 5, 6]
soduku6 = [9, 6, 1, 5, 3, 7, 2, 8, 4]
soduku7 = [2, 8, 7, 4, 1, 9, 6, 3, 5]
soduku8 = [3, 4, 5, 2, 8, 6, 1, 7, 9]

rows = [soduku, soduku1, soduku2, soduku3, soduku4, soduku5, soduku6, soduku7, soduku8]


def check_row(row, index):
    seen = []
    for num in row:
        if num in seen:
            print(f"Row {index}: duplicate number {num}")
            return False
        else:
            seen.append(num)
    print(f"Row {index} is valid: {row}")
    return True


def check_column(col_index):
    seen = []
    for row_index, row in enumerate(rows):
        num = row[col_index]
        if num in seen:
            print(f"Column {col_index}: duplicate number {num} (found in row {row_index})")
            return False
        else:
            seen.append(num)
    print(f"Column {col_index} is valid")
    return True


def solve():
    print("--- Checking Rows ---")
    for i, row in enumerate(rows):
        check_row(row, i)

    print("\n--- Checking Columns ---")
    for col in range(9):
        check_column(col)


solve()