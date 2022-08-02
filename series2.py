#Sum of Series : 1 + 11 + 111 + 1111 +.......n
n=int(input("enter a number : "))
sum=1
tot=0
for i in range(1,n+1):
    sum=sum+(10**i)
    tot=tot+sum
print(tot)  
