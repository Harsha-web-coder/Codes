##rock paper scissor 2
def get_winner(p1, p2):
   if p1 == 'rock' and p2 == 'paper':
       return'Second player wins!'
   elif p1 == 'rock' and p2 == 'scissors':
       return 'First player wins!'
   elif p1 == 'paper' and p2 == 'rock':
       return 'First player wins!'
   elif p1 == 'paper' and p2 == 'scissors':
       return'Second player wins!'
   elif p1 == 'scissors' and p2 == 'rock':
       return'Second player wins!'
   elif p1 == 'scissors' and p2 == 'paper':
       return 'First player wins!'
   else:
       return 'Tie'
 
player1 = input('First player: rock, paper or scissors: ')
player2 = input('Second Player: rock, paper or scissors: ')
print(get_winner(player1, player2))