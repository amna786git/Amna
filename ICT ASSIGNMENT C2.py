def parallel_resistance(R1,R2,R3):# evaluating the given funtion
    total = 0 # initializing the variable
    for r in (R1,R2,R3): # entering for loop for R equivilant
        total = total + 1/r
    return 1/total
# taking input of resistances fron user
R1 = int(input("enter the value of first resistor:"))
R2 = int(input("enter thw value of second resistor:"))
R3 = int(input("enter the value of third resistor:"))
# displaying output
print(parallel_resistance(R1,R2,R3))
