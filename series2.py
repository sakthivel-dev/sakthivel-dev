#Sum of Series : 1 + 11 + 111 + 1111 +.......n
n=int(input("enter a number : "))
sum=1
tot=0
for i in range(1,n+1):
    sum=sum+(10**i)
    tot=tot+sum
<<<<<<< HEAD
print(tot)    
=======
print(tot)  
>>>>>>> f12d16a72ad3b3d08a69a16cf818ea08581b9821
