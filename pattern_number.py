a=5
b=a
for i in range(1,a+1):
    for k in range(b-1,0,-1):
        print(" ",end=" ")
    b-=1
    for j in range(1,i+1):
        print(j,end=" ")
    count = i
    for n in range(1,i):
        count-=1
        print(count,end=" ")
    print()
