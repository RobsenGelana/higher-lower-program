import random
from game_data import data
from art import logo, vs

def format_output(account):
    name_a = account['name']
    decr_a = account['description']
    country_a = account['country']
    return f"{name_a}, a {decr_a}, from {country_a}"
def check_user_input(guess, account_a, acoount_b):
    if account_a > acoount_b:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
current_score = 0
compare_b = random.choice(data)
end_game = False
while not end_game:
    compare_a = compare_b
    compare_b = random.choice(data)

    while compare_a == compare_b:
        compare_b = random.choice(data)

    format_a = print(f"Compare A: {format_output(compare_a)}")
    print(vs)
    format_b = print(f"Against B: {format_output(compare_b)}")

    user_guess = input("Who has more follower? Type 'A' or 'B': ").lower()
    account_a = compare_a['follower_count']
    account_b = compare_b['follower_count']
    result = check_user_input(user_guess, account_a, account_b)
    if result:
        current_score += 1
        print(f"You guessed right current score is: {current_score}")
    else:
        end_game = True
        print(f"You guessed wrong current score: {current_score}")
