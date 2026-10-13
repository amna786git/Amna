# putting given values of r and v
r = 6
v = 12
# evaluating the given functions
def ohms_current(v,r): 
    I = v/r # usinf formula of current 
    return I
def power_dissipated(I,r):
    P = I*I*r # using formula of power 
    return P
I =ohms_current(v,r) # defining the value of I
# displaying output
print(ohms_current(v,r))
print(power_dissipated(I,r))
