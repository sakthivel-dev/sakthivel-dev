a=5
num =0
b = a
for i in range(1,a+1):
    for k in range(b,-1,-1):
        print(" ",end = "")
    b-=1
    for j in range(1,i+1):
        # num+=1
        print(i,end="  ")
    print()
