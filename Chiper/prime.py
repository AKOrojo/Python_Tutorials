# Write your code below this line 👇
def prime_checker(number):
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime == False:
        print("not prime")
    else:
        print("prime")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
