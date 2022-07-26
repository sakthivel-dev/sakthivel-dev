number=int(input("enter a number: "))
for i in range(1,10+1):
    for j in range(1,number+1):
        print(f"{j}*{i}={j*i}",end=" ")
    print("\n")           