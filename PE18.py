#data = [[3],[7,4],[2,4,6],[8,5,9,3],[2,10,1,2,3]]

data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

row_list = data.splitlines()
num_rows = len(row_list)

matrix = []
for i in range(0,num_rows):
    matrix.append(row_list[i].split(" "))
    num_ents_rowi = len(matrix[i])
    for j in range(0,num_ents_rowi):
        matrix[i][j] = int(matrix[i][j])

dim = len(matrix[-1])

longest_paths = matrix

for i in range(1,dim):
    longest_paths[i][0] += longest_paths[i-1][0]
    for j in range(1,i):
        longest_paths[i][j] += max(longest_paths[i-1][j-1],longest_paths[i-1][j])
    longest_paths[i][i] += longest_paths[i-1][i-1]

print(matrix)
print(longest_paths)

print(max(longest_paths[-1]))
