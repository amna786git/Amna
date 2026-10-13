def decimal_to_binary(n):
    binary = "" # Stores the binary
    while n> 0: # repeat until n become zero
        reminder = n%2 # find the remainder when n id divided by 2
        binary = str(reminder) + binary # add the remainder to the begining
        n = n//2 # divides n by 2 and keeps only the whole number
    return binary
# displays output
print(decimal_to_binary(20))
print(decimal_to_binary(35))
