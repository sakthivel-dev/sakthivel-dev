a=2
b=100
for i in range(a,b):
    flag=False
    for j in range(2,i):
        if(i%j==0):
             flag=True
             break
    if (not flag):
        print(i,end=" ")