#The following code can be treated as a Python beginner project

import random

def play():
    user = input("What do you choose \n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    #to check if a user inputs any character other than asked character
    if (user != 'r') and (user != 'p') and (user != 's'):
        print ("Wrong character entered, Try again: \n")
        return play()
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You wind the Game !! Congratulatoins'
    
    return 'You lost!'


#scenarious when user will win
#r>s, s>p, p>r

def is_win(player, opponent):
    #returns true if player wins
    if(player == 'r' and opponent =='s' ) or (player =='s' and opponent =='p')\
            or (player == 'p' and opponent =='r'):
            return True
    
print(play())
        