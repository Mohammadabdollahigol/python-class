print('sang')
print('KAGHAS')
print('gheichi')


player1 = str(input('player 1 lotfan harkat khod ra entekhab konid: '))
player2 = str(input('player 2 lotfan harkat khod ra entekhab konid: '))
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
 