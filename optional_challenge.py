print("\n Welcome to the Beyoncé Fan Club!\n")

# Asking the user to choose between 4 valid options

print("\n Choose your favorite Beyoncé album:")
print("\n 1. 4")
print("\n 2. Beyoncé")
print("\n 3. Lemonade")
print("\n 4. Renaissance")

# Defining the output for the chosen option

while True:
    choice = input("\nEnter the number corresponding to your favorite album: ")
    if choice in ["5", "6", "7", "8"]: # Here is the runtime error, the index would be out of range and would give the error on those options
        break
    else:
        print("Invalid choice. Please enter a valid number.") # This message would appear for the possible correct input given before

albums = ["4", "Beyoncé", "Lemonade", "Renaissance"]
favorite_album = albums[int(choice)-1] 

print(f"\nYour favorite Beyoncé album is: {favorite_album}\n") 

# I could not think about a logical error to include in this program, besides that everybody should have a Beyoncé favourite album, logically. =)

print("\nThank you!\n")