# Write a program that continually aks a user to enter a number

num = 0 # The total sum of the numbers inputted

times_entry = 0 # To count how many numbers the user inputted

user_input = int(input("\n Please enter a number (-1 to exit): "))  # Asking the user to input the number

# Using while loop to create the program

while user_input != -1:
    num += user_input  # Calculating the sum of all numbers
    times_entry = times_entry + 1  # Calculating how many entries the user inputted

    user_input = int(input("\n Please enter a number (-1 to exit): ")) # Repeating the question until the loop breaks

    if user_input == -1:  
        average = num / times_entry  # Calculating the average of the numbers entered
        print (f"\n The average of the numbers you entered is: {average}")
        print (f"\n The total sum of the numbers entered is: {num}")
        
        break

print("\n Thank you!")