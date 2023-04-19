import random
print('sang')
print('KAGHAS')
print('gheichi')
player1 = (input('player 1 lotfan harkat khod ra entekhab konid: '))
randomnumber = random.randint(1,3)
if randomnumber==1:
    player2='sang' 
    print('entekhab player2=', player2)
elif randomnumber==2:
    player2='kaghaz'
    print('entekhab player2=', player2)
elif randomnumber==3:
    player2='gheichi'
    print('entekhab player2=', player2)
if player1==player2:
    print('mosavi')
elif player1 == 'sang' and player2 =='kaghaz' :
    print ('player 2 win')
elif player1 == 'sang' and player2 =='gheichi' :
    print ('player 1 win')
elif player1 == 'kaghaz' and player2 =='sang' :
    print ('player 1 win') 
elif player1 == 'kaghaz' and player2 =='gheichi' :
    print ('player 2 win')
elif player1 == 'gheichi' and player2 =='sang' :
    print ('player 2 win')
elif player1 == 'gheichi' and player2 =='kaghaz' :
    print ('player 1 win')
else:
    print ('ye chizi eshtebahe')