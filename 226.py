#Matrix add using list

L1=[[1,2],[3,4]]
L2=[[5,6],[7,8]]
L3=[]
for i in range(len(L1)):
    x=[]
    for j in range(len(L1[i])):
        x.append(L1[i][j]+L2[i][j])
    L3.append(x)
print(L3)
