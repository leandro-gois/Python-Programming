# Different types of decisions
score = 85

# Simple condition
if score >= 90:
    print("Excellent work!")

# Alternative choice
if score >= 70:
    print("You passed!")
else:
    print("You need to study more.")

# Multiple options
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
    
print(f"Your grade is: {grade}")

