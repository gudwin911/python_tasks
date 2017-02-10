import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = lower_letters.upper()
numbers = "0123456789"
symbols = "~!@#$%^&*()_+=-\|/,.?<>[]{}:;`\"\' "
lst =[lower_letters, upper_letters, numbers, symbols]

def ask_password():
    while True:
        choice = input("Choose a power of Your password: "
                       "enter 'weak' for a simple pass, or a number from 7 to 14 for a strong one --> ").lower()
        if choice in ["w", "we", "wea", "weak"]:
            return "weak"
        elif choice in ["7", "8", "9", "10", "11", "12", "13", "14"]:
            return int(choice)
        print("Try again")

def random_symbol(lst):
    return random.choice(random.choice(lst))

def generator(power):
    password = ""
    if power == "weak":
        password = random.choice(["qwerty", "football", "welcome", "abc123", "login", "123456", "starwars", "passw0rd"])
    else:
        for i in range(power):
            password += random_symbol(lst)
    print("Your password is:", password)

generator(ask_password())