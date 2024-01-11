# Write code to output the star pattern shown below, using an if-else statement in combination with a single for loop:

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# I used the same logic presented on the open class (confess I was a bit stuck on this one)

pattern = "*"

for num in range (1,10):   # Defining the number of lines (9)
    to_print = pattern*num   # Creating the pyramid pattern
    if num >= 5:   # Defining the turning point
        count_down = 10 - num   # Defining the decrescent order from the turning point
        to_print = pattern*count_down   # Creating the decrescent order

    print(to_print)    

print ("")
        
# Other method I found is using the rows instead of the lines
    
rows = 5 # Defining the max point

for i in range(1, rows + 1): # Starting at 1 and adding every step further
    print('*' * i)  # Printing the first crescent half

for i in range(rows - 1, 0, -1): # Opposite logic 
    print('*' * i) # Printing the decrescent half

print ("\nThank you!\n")