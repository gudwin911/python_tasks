import random

upper_letters = lower_letters.upper()
symbols = "~!@#$%^&*()_+=-\|/,.?<>[]{}:;`\"\' "
lst =[lower_letters, upper_letters, numbers, symbols]

def ask_password():
    choice = input("Choose a power of Your password: weak(simple word), middle(10 symbols) or strong(14 symbols) ").lower()
    if choice in ["w", "we", "wea", "weak"]:
        return 5
    elif choice in ["m", "mi", "mid", "midd", "middl", "middle"]:
        return 10
    elif choice in ["s", "st", "str", "stro", "stron", "strong"]:
        return 14
    else:
        return 0

def random_list(lst):
    return random.randint(0, len(lst)-1)

def random_symbol(lst):
    return random.choice(lst[random_list(lst)])

def generator(power):
    password = ""
    if power == 5:
        password = random.choice(["qwerty", "football", "welcome", "abc123", "login", "123456", "starwars", "passw0rd"])
    elif power == 0:
        print("Please, enter 'weak', 'middle' or 'strong'")
        generator(ask_password())
    else:
        for i in range(power):
            password += random_symbol(lst)
    print("Your password is: ", password)

#ask_password()


generator(ask_password())
