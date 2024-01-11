# Initialize an empty list to store the scores
scores = []

# Get scores from the user for each test
for i in range(1, 5):
    while True:
        try:
            score = float(input(f"\n Enter the score for Test {i}: "))
            break  # Exit the loop if input is a valid float
        except ValueError:
            print(" Invalid input. Please enter a valid number.")

    scores.append(score)

# Calculate the average score
average_score = sum(scores) * len(scores) # Here is the logical error, the average should be sum(scores) / len(scores)

# Display the results
print("\n Test Scores:")
for i, score in enumerate(scores, start = 1):
    print(f"\n Test {i}: {score}")

print(f"\n The average score is: {average_score:.2f}\n")

print ("\n Thank you!\n")