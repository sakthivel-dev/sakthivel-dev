
for i in range(1,500):
    count = 0
    for j in range(1,i):
        if(i%j==0):
            count=count+j

    if(count==i):
        print("perfect number",i)
        