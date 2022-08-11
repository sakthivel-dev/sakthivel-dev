a=5
b=a
for i in range(1,a):
    for k in range(b-1,0,-1):
        print("-",end="")
    b-=1
    
    for j in range(0,i*2-1):
        print("*",end="")
    print()
