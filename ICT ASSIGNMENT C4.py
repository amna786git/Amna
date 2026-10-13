def loaded_divider(vs,r1,r2,rl):
      unloaded_voltage= vs*(r2/(r1+r2))#using the formula of voltage divider
      parallel = 1/(1/rl+1/r2 )# using the formula for parallel equivalent
      loaded_voltage = vs*(parallel/(parallel+r1))
      return(unloaded_voltage,loaded_voltage)
# taking input from user
vs = int(input("enter the value of source voltage:"))
r1 = int(input("enter the value of r1:"))
r2 = int(input("enter the value of r2:"))
rl = int(input("enter the value of rl:"))
# displaying output
loaded_voltage,unloaded_voltage = loaded_divider(vs,r1,r2,rl)
print("loaded voltage:" ,loaded_voltage)
print("unloaded voltage:" , unloaded_voltage)
