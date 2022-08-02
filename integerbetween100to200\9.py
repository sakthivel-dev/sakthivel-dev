min=int(input("enter a min number: "))
max=int(input("enter a max number: "))

for i in range(min,max+1):
    if(i%9==0):
        print(i)
