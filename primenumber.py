n=int(input("enter a number"))
flag =False
for i in range(2,n):
    if(n%i!=0):
        flag = False
    else:
        flag = True

if(not flag):
    print("Prime")
else:
    print("Not Prime")