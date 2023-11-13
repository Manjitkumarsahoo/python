#Matrix add using list

L1=[[1,2],[3,4]]
L2=[[5,6],[7,8]]
L3=[[0,0],[0,0]]

for i in range(len(L1)):
    for j in range (len(L1[i])):
        L3[i][j]=L1[i][j]+L2[i][j]
print(L3)

