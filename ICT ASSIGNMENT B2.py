n = int(input("how many resistors?")) # taking number od resistors from user
total = 0 # initializing the value of variable
for i in range(1,n+1):
    R=int(input("enter R"+str(i)+":")) # coverting i as string to attach it with text around
    total += R
print("total resistance :" ,total, "ohm")# diplaying output
