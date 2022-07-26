a=int(input("enter a number: "))
sum=0
for i in range(2,a*2+1,2):
    print(i,end=" ")
    sum=sum+i
print("total sum of:",sum)
