A = int(input("enter a bit A:"))# taking A as input from user
B = int(input("enter a bit B:"))# taking B as input from user
if A!=0 and A!=1 or B!=0 and B!=1 :
    print(" the bits must be 0 and 1 ")#output if A and B are other than 0 or 1 
else:
    if A==1 and B==1: # displaying AND operation
        print("AND = 1")
    else :
        print("AND = 0")
    if A!=0 or B!=0 : # displaying OR operation
        print("OR = 1")
    else:
        print("OR = 0")
    if A!=B : # displaying XOR operation
        print("XOR = 1")
    else:
        print("XOR = 0")

    
 
              
