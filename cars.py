from re import I


cars=["tata","range rover","suzuki","nissan","lambhorginie"]
while True:
    print("main menu")
    print("1.append to the array")
    print("2.remove from the array")
    print("3.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        number=int(input("how many cars:"))
        for i in range(number):
            newcar=input("enter the new car name:")
            cars.append(newcar)
        for i in cars:                
            print(i)
    elif choice==2:
        print("removing")
        rem=input("enter the car to be removed:")
        cars.remove(rem)
        for i in cars:
            print(i)
    elif choice==3:
        break
    else:
        print("sorry incorrect choice")
