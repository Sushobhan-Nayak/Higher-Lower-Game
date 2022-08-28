from art import logo,vs
from data import data
import random as rdm

print(logo)
should_continue=True
score=0
num1=rdm.randint(0,49)
num2=rdm.randint(0,49)
while should_continue:
    num1=num2
    num2=rdm.randint(0,49)
    print(f"COMPARE A: {data[num1]['name']} , a {data[num1]['description']} from {data[num1]['country']}.")
    print(vs)
    print(f"COMPARE B: {data[num2]['name']} , a {data[num2]['description']} from {data[num2]['country']}.")
    ask=input("Who has more followers on instagram ? Type A or B. ")
    if ask=="A" and data[num1]['follower_count']>data[num2]['follower_count']:
        score += 1
        print(f"You are right , current score {score}.")
    elif ask=="B" and data[num1]['follower_count']<data[num2]['follower_count']:
        score += 1
        print(f"You are right , current score {score}.")
    else:
        should_continue=False

print(f"Your final score is {score}.")