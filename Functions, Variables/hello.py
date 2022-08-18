# Ask users name
name = input("Whats your name? ")

# Say hello to user
print(f"hello, \"{name}\"")

# Ask users age
age = int(input("Whats your age? "))

# Say users age
if age < 2:
    print(f"You are {age} year old")
else:
    print(f"You are {age} years old")
