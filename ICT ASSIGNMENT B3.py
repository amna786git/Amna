readings = (3.3,3.1,3.4,2.9,3.6,3.0,3.2)
lenght = len(readings) # displaying number of voltages
count = 0  #initializing variable
highest = readings[0]
lowest = readings[0]# initializing higher and lowest reading
total = 0
for i in readings: # using if inside for loop to evaluate the given condition
    if i>3.2:
        count += 1
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i
    total += i
average=total/lenght
# displaying outputs
print("voltages greater than 3.2 =" ,count)
print("highest voltage:" ,highest, "V")
print("lowest voltage:" , lowest, "V")
print("average:" ,average,"V")
    
