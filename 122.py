a={
    1:'manjit',
    2:'lulu',
    3:'sujit',
    4:'kunu',
    5:'pikul',
    6:'debu'
}
data=dict(filter(lambda x:x[0]%2==0,a.items()))
print(data)
