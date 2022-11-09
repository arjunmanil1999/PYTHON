s=int(input("enter the first year:"))
t=int(input("Enter the second year:"))
if(s<t):
    print("leap years are:")
    for i in range(s,t):
        if(i%4==0 and i%100!=0):
            print(i,end=" ")
else:
    print("invalid dates")       


