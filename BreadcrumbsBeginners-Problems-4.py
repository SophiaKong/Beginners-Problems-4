def check_password():
    correct_password = "my_password"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Enter Password: ")
        if password == correct_password:
            print("Correct Password")
            return
        else:
            attempts += 1
            print(f"Incorrect password. {max_attempts - attempts} attempts left.")

    print("Locked")


check_password()

def name_loop():
    num_times = int(input("Enter a number: "))
    name = input("Enter your name: ")

    for _ in range(num_times):
        print(name)


name_loop()

def multiplication_table():
    while True:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break
        print("Not a positive integer.")
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

multiplication_table()

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_number_check():
    num = int(input("Enter an integer: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

prime_number_check()

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz()
