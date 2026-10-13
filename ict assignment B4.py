voltages= [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
length=len(voltages)# gives the number of voltage values
current_streak=1 # current decreasing streak
longest_streak=1 # longest streat found

starting_volt=voltages[0] # starting voltage

ending_volt=voltages[0]# ending voltage 

current_start=voltages[0] # start of current streak

for i in range (1,length):
    if voltages[i]<voltages[i-1]:
        current_streak = current_streak+1 # increasing streak
    else:
        current_streak=1 # reset streak 
        current_start=voltages[i]# new start

    if current_streak>longest_streak:
        longest_streak = current_streak # update longest streak
        starting_volt = current_start # save starting voltage
        ending_volt=voltages[i] # save ending voltage 
#displaying output
print("longest continuos drop:", longest_streak, "readings")
print("started at:", starting_volt, "V")
print("ended at:", ending_volt, "V")
