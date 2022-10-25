print("Welcome to the Life in Weeks") 
first_name = input("What is your first name?") # input first name
last_name = input("What is your last name?") # input last name
age = input("What is your current age?") # input your age

left = 90 - int(age) # this assuming your life is up to 90
print(f" {first_name} {last_name}\nyou have {left*365} days, {left*52} weeks, and {left*12} months left.")
