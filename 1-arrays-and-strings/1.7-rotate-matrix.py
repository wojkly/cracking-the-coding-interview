from copy import deepcopy

def rotate_matrix(m):
    res = [[0 for j in range(len(m))] for i in range(len(m[0]))]
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            iRes = j
            jRes = -i - 1
            
            res[iRes][jRes] = m[i][j]
            
    return res

def rotate_matrix_in_place(m_2):  
    m = deepcopy(m_2)  
    for i in range(len(m) // 2 + 1):
        for j in range(len(m[0]) // 2):
            insertValue = m[i][j]
            iNext = i
            jNext = j
            # print(iNext, jNext)
            for k in range(4):
                tmp = iNext
                iNext = jNext
                jNext = len(m) - tmp - 1
                nextInsertValue = m[iNext][jNext]
                m[iNext][jNext] = insertValue
                insertValue = nextInsertValue
                # print(iNext, jNext)
            # return m
    return m

def print_m(m):
    for row in m:
        print(row)
    print()
m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

m2 = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

m3 = [[1,2],
      [3,4],
      [5,6],
      [7,8]]

# r1 = rotate_matrix(m1)
# print_m(r1)
# r2 = rotate_matrix(m2)
# print_m(r2)
# r3 = rotate_matrix(m3)
# print_m(r3)

m4 =[[1,0,2],
     [0,0,0],
     [4,0,3]]


r4 = rotate_matrix_in_place(m4)
print_m(r4)
r5 = rotate_matrix_in_place(m1)
print_m(r5)