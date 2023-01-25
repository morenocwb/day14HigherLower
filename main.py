from random import randint
from art import logo
from art import vs
from game_data import data

DATA_LENGTH = len(data) - 1
is_game_over = False
score = 0


# 1. Randomizar famoso do BD
def person_generated():
    person = [data[randint(1, DATA_LENGTH)]]
    return person



# 2. dar a escolha para o usuário votar em A ou B
def user_choice(person_A, person_B):
    global is_game_over
    global score
    user_pick = str(input("Which one has more IG followers? A or B:").lower())
    print(f"USER CHOSE {user_pick}")
    if int(person_A[0]["follower_count"]) > int(person_B[0]["follower_count"]):
        if user_pick == "a":
            score += 1
            print(f"You're Right! Current score: {score}")
            print(f"Compare A: {person_A[0]['name']}, {person_A[0]['description']} , {person_A[0]['country']}")
            return person_A
        else:
            is_game_over = True
            print(f"Sorry, you're Wrong!")
            return
    elif int(person_A[0]["follower_count"]) < int(person_B[0]["follower_count"]):
        if user_pick == 'b':
            score += 1
            print(f"You're Right! Current score: {score}")
            print(f"Compare A: {person_B[0]['name']}, {person_B[0]['description']} , {person_B[0]['country']}")
            return person_B
        else:
            is_game_over = True
            print(f"Sorry, you're Wrong!")
            return


def game():
    print(logo)
    round = person_generated()
    print(f"Compare A: {round[0]['name']}, {round[0]['description']} , {round[0]['country']}")
    while not is_game_over:
        print(vs)
        person_B = person_generated()
        print(f"Compare B: {person_B[0]['name']}, {person_B[0]['description']} , {person_B[0]['country']}")
        round = user_choice(round, person_B)


    print(f"Your Final Score is {score}")


game()
