a=int(input("enter a number:"))
flag=False
for i in range(a,2,-1):
    for j in range(2,i):
        if(i%j==0):
            flag=True
            break
if(not flag):
    print("the prime number")
else:    
    print("the not prime number")