n=int(input())
sum =0.000000
for i in range(1,n+1):
    a = float((1/i)**i)
    sum = sum + a
print(sum)