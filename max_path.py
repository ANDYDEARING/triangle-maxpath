triangle = [[3],[7,4],[2,4,6],[8,5,9,3]]

num_rows = len(triangle)
row_index = num_rows - 2

while row_index >= 0:
    column_index = 0
    for number in triangle[row_index]:
        down_left = number + triangle[row_index+1][column_index]
        down_right = number + triangle[row_index+1][column_index+1]
        if down_left > down_right:
            triangle[row_index][column_index] = down_left
        else:
            triangle[row_index][column_index] = down_right
        column_index += 1
    row_index -= 1

print(triangle[0][0])