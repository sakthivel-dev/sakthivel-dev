a=int(input("enter a number: "))
sum=0

for i in range(1,a*2+1):
    if(i%2!=0):
        print(i)
        sum=sum+i
print("total of odd number",sum)