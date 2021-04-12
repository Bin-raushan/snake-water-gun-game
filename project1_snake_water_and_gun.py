# Snake Water Gun or Rock Paper Scissors

import random
# If two values are equal, declare a tie!
def game_win(computer,you):
    if computer==you:
        return None
# all possiblities when computer choose gun
    elif computer=='g':
         if you=='w':
            return True
         elif you=='s':
            return False
# all possiblities when computer choose gun
    elif computer=='w':
         if you=='g':
            return False
         elif you=='s':
            return True
# all possiblities when computer choose gun            
    elif computer=='s':
         if you=='g':
            return True
         elif you=='w':
            return False
         
print("computer turn: snake(s),water(w),gun(g)? ")
random_no=random.randint(1,3)
if random_no == 1:
    computer = 's'
elif random_no == 2:
    computer = 'w'
elif random_no == 3:
    computer = 'g'
you=input("your turn: snake(s),water(w),gun(g)? ")
result=game_win(computer,you)
print("computer choose",computer)
print("you choose",you)
if result==None:
    print("It's a tie!")
elif result:
    print("Congratulation! You won the match")
else:
    print("sorry! You lost the match")
