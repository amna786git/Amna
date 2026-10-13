one = 0
five = 0  # initializing the value of 1% and 5% tolrances and rejected resitances
rejected = 0
while True:
    R = int(input("enter the value of resistor :")) # taking input from user
    if R>=90 and R<=101 :# evaluating condition for 1% tolrence resistance
        one +=1
    elif R >=95 and R<=105:# evaluating condition for 5% tolrence resistance

        five += 1
    else:
        rejected += 1
    if R == 0:
        break
    # displaying output
print("1% tolerance resistors:" , one )
print("5% tolerance resistors:" , five)
print("rejected resistors:" , rejected)
