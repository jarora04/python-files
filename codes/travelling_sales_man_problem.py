import random
ran=random.getrandbits(128)
mat = [[ran,15,10,25], [15,ran,20,10],[10,20,ran,15],[25,10,15,ran]]
src = 0
print(src, end=", ")

for i in range(len(mat)):
    nxt_vertex = mat[src].index(min(mat[src]))
    mat[nxt_vertex][src] = ran
    src = nxt_vertex
    print(src, end=", ")  
    