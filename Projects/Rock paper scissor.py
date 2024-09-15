import random

def play():
    user = input("Make a Choice 'r' for rock,'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "TIE" 
    
    if is_win(computer,user):
        return "WON"
    
    return "LOSE"

def is_win(player, opponent):
# return true if player wins
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') \
    or (player == 'p'and opponent == 'r'):
        return True

print(play())