year = int(input("Which year do you want to check? "))
cond1= (year%4)
cond2= (year%100)
cond3= (year%400)

if cond1==0:
    if cond2>1:
        if cond3>1:
            print("Not Leap year.")
        else:
            print("Leap year.")
    else:
        print("leap year.")
else:
    print("Not leap year.")