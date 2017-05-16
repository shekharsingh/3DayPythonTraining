mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print mat[1]
print mat[1][1]
mat[1][1] = 'x'
print mat

mat[-1].append(10)
print mat

for row in mat:
    for col in row:
        print col, "\t",
    print
