#o display the sum of the series [ 9 + 99 + 999 + 9999 ...]
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    sum = sum + ((10**i)-i)
print("The sum of the sarise = ",sum)
