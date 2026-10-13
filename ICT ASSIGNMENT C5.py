def star_to_delta(Ra,Rb,Rc): #evaluating the given function
 RNumerator = Ra*Rb + Rb*Rc + Ra*Rc
 Rab= RNumerator/Rc
 Rbc= RNumerator/Ra
 Rca= RNumerator/Rb
# rounding off the value of Rab Rbc and Rca upto 2 decimal places
 Rab=round(Rab,2)
 Rbc=round(Rbc,2)
 Rca=round(Rca,2)
 return Rab,Rbc,Rca
# taking input from the user
R1=int(input("enter the value of resistance R1:"))
R2=int(input("enter the value of resistance R2:"))
R3= int(input("enter the value of resistance R3:"))
# displaying output
print(star_to_delta(R1,R2,R3))
