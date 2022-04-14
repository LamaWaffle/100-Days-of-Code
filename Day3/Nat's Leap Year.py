year = int(input("Which year do you want to check? "))
cond1= (year%4)
cond2= (year%100)
cond3= (year%400)

if cond1==0:
    if cond2<100:
        if cond3<400:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")