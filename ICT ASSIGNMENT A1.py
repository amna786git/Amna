#take resistance and voltage as input from the user
R = int(input("enter the value of resistance (ohm) :"))
V = int(input("enter the vale of voltage (v) :"))
I = V/R # using formula of current 
if I>2: # the fuse will blow if current is greater than 2
   print("the fuse will blow")
else:
    print("the circuit is safe")
if R<=0:  # if resistance will be gless than or equal to zero it will print invalid
    print("invalid resistance ")
else:
    print("the current (A):" ,I)


