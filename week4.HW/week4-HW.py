# Problem 1: Letter Grade Calculator
# ----------------------------------
# Ask the user for a score from 0 to 100 and print the letter grade:
#   - 90 to 100  -> A
#   - 80 to 89   -> B
#   - 70 to 79   -> C
#   - 60 to 69   -> D
#   - below 60   -> F
# Constraint: Do NOT use 'and'. Use the natural order of elif to
# handle the ranges.

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Problem 2: Leap Year Checker
# ----------------------------
# A year is a leap year if:
#   - It is divisible by 4, AND
#   - It is NOT divisible by 100, UNLESS it is divisible by 400.
# Ask the user for a year and print "Leap Year" or "Not a Leap Year".
# Constraint: You may NOT use 'and' or 'or'. Use nested if statements.


year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")


# Problem 3: Triangle Type
# ------------------------
# Ask the user for the three sides of a triangle (a, b, c). Print:
#   - "Equilateral" if all three sides are equal.
#   - "Isosceles"   if exactly two sides are equal.
#   - "Scalene"     if no sides are equal.
# Constraint: NO logical operators. Use nested if-else.
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a == b:
    if b == c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if a == c:
        print("Isosceles")
    else:
        if b == c:
            print("Isosceles")
        else:
            print("Scalene")


# Problem 4: Number Sign and Magnitude
# ------------------------------------
# Ask the user for a number and print:
#   - "Negative large"  if the number is less than -100
#   - "Negative small"  if the number is between -100 and 0 (not 0)
#   - "Zero"            if the number is exactly 0
#   - "Positive small"  if the number is between 0 and 100 (not 0)
#   - "Positive large"  if the number is greater than 100
# Constraint: NO logical operators. Use ordered elif branches.

number = int(input("Enter a number: "))

if number < -100:
    print("Negative large")
elif number < 0:
    print("Negative small")
elif number == 0:
    print("Zero")
elif number <= 100:
    print("Positive small")
else:
    print("Positive large")


#     Problem 5: Ticket Price Calculator
# -----------------------------------
# A cinema charges tickets based on age and day:
#   - Age below 12         -> 20 SAR
#   - Age 12 to 17         -> 35 SAR
#   - Age 18 to 59         -> 50 SAR
#   - Age 60 or above      -> 25 SAR
# Additionally, on "Tuesday", every ticket gets a 10 SAR discount
# (minimum price must not go below 10 SAR).
# Ask the user for age and day, then print the final ticket price.
# Constraint: NO logical operators. Use nested conditions.

age = int(input("Enter your age: "))
day = input("Enter the day: ")

if age < 12:
    price = 20
else:
    if age < 18:
        price = 35
    else:
        if age < 60:
            price = 50
        else:
            price = 25

if day == "Tuesday":
    price = price - 10

    if price < 10:
        price = 10

print("Final ticket price:", price, "SAR")


# Problem 6: Rock, Paper, Scissors
# --------------------------------
# Ask two players to enter their choice: "rock", "paper", or
# "scissors". Print the result:
#   - "Tie"            if both chose the same
#   - "Player 1 wins"  if Player 1 beats Player 2
#   - "Player 2 wins"  otherwise

# Game rules:
#   - rock      beats  scissors
#   - scissors  beats  paper
#   - paper     beats  rock

# Constraint: NO logical operators. Use if-elif-else with nested
# if-else inside each branch.

player1 = input("Player 1: ").lower()
player2 = input("Player 2: ").lower()

if player1 == player2:
    print("Tie")

elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins")
    else:
        print("Player 2 wins")

elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")

else:
    if player2 == "paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")

# Problem 7: Loan Eligibility
# ---------------------------
# A bank decides on a loan based on three factors:
#   - Age must be between 21 and 65 (inclusive).
#   - The applicant must have a job (answer "yes" or "no").
#   - Monthly income (in SAR) determines the result:
#        income >= 5000          -> "Approved"
#        income between 3000 and 4999 -> "Approved with conditions"
#        income below 3000       -> "Rejected: low income"

# If age is outside 21–65            -> "Rejected: age not eligible"
# If applicant has no job             -> "Rejected: no job"

# Ask the user for age, income, and job status, then print the
# result.

# Use logical operators for the age range, and nested if statements
# for the job check and income tiers.

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
job = input("Do you have a job? (yes/no): ").lower()

if age >= 21 and age <= 65:

    if job == "yes":

        if income >= 5000:
            print("Approved")

        elif income >= 3000:
            print("Approved with conditions")

        else:
            print("Rejected: low income")

    else:
        print("Rejected: no job")

else:
    print("Rejected: age not eligible")
