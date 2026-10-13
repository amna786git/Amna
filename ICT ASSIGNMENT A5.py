R1 = int(input("enter R1:"))
R2 = int(input("enter R2;")) # taking  value of R1 R2 and R3 from user
R3 = int(input("enter R3:"))
if R1<=R2 and R1<=R3:# applying condition for smallest for R1
    print("smallest = " ,R1,"ohm")
elif R2<=R1 and R2<=R3:# Applying smallest condition for R2
    print("smallest = " ,R2, "ohm")
else:
    print("smallest = " , R3, "ohm")
if R1>=R2 and R1>=R3:# Largest number condition for R1
    print("largest = " ,R1, "ohm")
elif R2>=R1 and R2>=R3:# Largest number condition for R2
    print("largest = " ,R2, "ohm")
else :
    print("largest = " ,R3, "ohm")
