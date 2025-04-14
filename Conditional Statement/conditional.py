#Ex1 Basic if statement
number = int(input("enter number:"))
if number>0:
    print("positive")

#Ex2  Voting Eligibility
age = int(input("enter their age:"))
if age >= 18:
    print("you can vote!")

#Ex3
age = int(input("Please enter your age:"))
if age < 12:
    print("child")
elif 12 <= age <= 17:
    print("teen")
elif 18 <= age <= 64:
    print("adult")
else:
    print("senior")

#Ex4
number = int(input("enter a number:"))
