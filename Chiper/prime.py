# Write your code below this line ๐
def prime_checker(number):
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime == False:
        print("not prime")
    else:
        print("prime")


# Write your code above this line ๐
# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
