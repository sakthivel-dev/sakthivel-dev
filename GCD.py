a=int(input())
b=int(input())
if(a<b):
    min = a
else:
    min = b

for i in range(min,0,-1):
    if(a%i==0 and b%i==0):
        print("the number",i)
        break




    