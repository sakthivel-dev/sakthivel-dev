a=4
b=a
for i in range(1,a+1):
    for k in range(b-1,-1,-1):
        print(" ",end=" ")
    b-=1
    for j in range(0,i*2-1):
        print("*",end=" ")
        
    print()
b=a
for m in range(0,a+1):
    for n in range(1,m+1):
        print(" ",end=" ")
    for p in range(0,(b+1)*2-1):
        print("*",end=" ")
    b-=1
    print()
