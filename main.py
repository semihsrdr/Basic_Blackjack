import random
import time

game_continue=True

def get_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def sum_cards(cards):
    sum=0
    for i in cards:
        sum+=i

    return sum

def check_winner(crupier_cards,player_cards):
    if sum_cards(player_cards) > sum_cards(crupier_cards) and sum_cards(player_cards) <= 21:
        print("Player won")
        game_continue = False
    elif sum_cards(player_cards) > sum_cards(crupier_cards) and sum_cards(player_cards > 21):
        print("Crupier Won")
        game_continue = False

    elif sum_cards(crupier_cards) > sum_cards(player_cards) and sum_cards(crupier_cards) <= 21:
        print("Crupier won")
        game_continue = False

    elif sum_cards(crupier_cards) > sum_cards(player_cards) and sum_cards(crupier_cards) > 21:
        print("Player won")
        game_continue = False
    else:
        print("Draw")
        game_continue = False



print("Welcome to the blackjack...")
print()

player_cards=[]
crupier_cards=[]
for i in range(2):
    player_cards.append(get_card())
    crupier_cards.append(get_card())
print("Your cards are coming...")
time.sleep(0.5)
print("Your cards are :",player_cards,"and sum of your cards : ",sum_cards(player_cards))
time.sleep(1)
print("Crupier's cards are coming...")
print("Crupier's card is : ["+str(crupier_cards[0])+"]")
while game_continue:
    decision=input("Do you wanna hit or stand : ")
    if decision=="hit":
        player_cards.append(get_card())
        print("Your cards are :", player_cards, "and sum of your cards : ", sum_cards(player_cards))
        if sum_cards(player_cards)>21:
            print("You lost. Crupier Won")
            print("Crupier's cards were :", crupier_cards, "and sum of crupier's cards was:", sum_cards(crupier_cards))
            break
        check_winner(crupier_cards, player_cards)


    elif decision=="stand":
        print("Crupier's cards are :", crupier_cards,"and sum of crupiers cards :",sum_cards(crupier_cards))
        while sum_cards(crupier_cards)<sum_cards(player_cards) or sum_cards(crupier_cards)<17:
            print("Crupier getting card...")
            time.sleep(2)
            crupier_cards.append(get_card())
            print("Crupier's cards are :", crupier_cards, "and sum of crupiers cards :", sum_cards(crupier_cards))
            if sum_cards(crupier_cards)>21:
                break

        check_winner(crupier_cards, player_cards)
        break


