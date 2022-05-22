import random
import time
import os

def clear():
  os.system('clear')

def dealCard(hand,deck):
  loop1=1
  while loop1==1:
    x=random.randrange(10,124)
    if int(str(x)[-1]) in range(4):
      if x<100:
        x="0"+str(x)
      else:
        x=str(x)
      if deck[2][deck[0].index(x)]>0:
        deck[2][deck[0].index(x)]=deck[2][deck[0].index(x)]-1
        hand.append(x)
        loop1=0

def checkNatural(hand,deck,players):
  lst=[]
  for x in range (0, players):
    status = False
    if hand[x][1][0] == "0" and hand[x][1][1] == "1":
      if (hand[x][2][0]=="1"):
        status = True
    elif hand[x][2][0] == "0" and hand[x][2][1] == "1":
      if (hand[x][1][0]=="1"):
        status = True
    if status == True:
      # print (f"Player {x} has a natural!!!")
      lst.append(hand[x][0])
  if len(lst)==0:
    pass
  else:
    for x in range (len(lst)):
      print (f"{lst[x]} has a natural!!!")
    if len(lst)==1:
      print(f"{lst[0]} wins!!!!")
    else:
      for x in range (len(lst)):
        print (f"{lst[x]} wins!!!")
    return 1
  return 0

def checkBust(hand,deck,players):
  total=0
  if hand[-1]==-1:
# if stood, last index would be -1, and hence we cant calculate that too
    for x in range(1,len(hand)-1):
      value=deck[3][deck[0].index(hand[x])]
      if value==11:
        value=1
      total=total+value
    if total>21:
      return 0
    else:
      return 1

# did not stand
  else:
    for x in range(1,len(hand)):
      value=deck[3][deck[0].index(hand[x])]
      if value==11:
        value=1
      total=total+value
    if total>21:
      return 0
    else:
      return 1

def checkEnd(hands,players):
  status=False
  for x in range(0,players):
    if hands[x][-1]==-1 or hands[x][-1]==-2:
      status=True
    else:
      status = False
      break
  return status

def dealerPlay(hands,deck,players):
  total=0
  count=0
  if hands[0][-1]==-1 or hands[0][-1]==-2:
    pass
  else:
    for i in range(1,len(hands[0])):
      value=deck[3][deck[0].index(hands[0][i])]
      if value==11:
        count=count+1
      total=total+value
#Printing out dealer's cards
    print(f"Dealer {hands[0][0]}'s cards:'")
    for i in range(1,len(hands[0])):
      print(deck[1][deck[0].index(hands[0][i])])

#If dealer's hand is over 17, stand, if over 21, bust
    if total>=17:
      if total>21:
        if count==0:
          hands[0].append(-2)
          print("Dealer busted")
        else:
          total=total-10
          count=count-1
        
      else:
        print("Dealer will Stand")
        hands[0].append(-1)


    else:
      dealCard(hands[0],deck)
      
      if checkBust(hands[0],deck,players)==0:
        # if "010" in hands[0] or "011" in hands[0] or "012" in hands[0] or "013" in hands[0]:
        #   status = True
        #   while status == True:
            
        print(f"{hands[0][0]}'s hand:'")
        time.sleep(0.5)
        for i in range(1,len(hands[0])):
          print(deck[1][deck[0].index(hands[0][i])])
        print(f"{hands[0][0]} has gotten over 21!\n{hands[0][0]} has busted!")
        hands[0].append(-2)
        
      else:
        print(f"{hands[0][0]}'s hand:'")
        time.sleep(0.5)
        for i in range(1,len(hands[0])):
          print(deck[1][deck[0].index(hands[0][i])])
  time.sleep(1)

  
def playerPlay(hands,deck,players,x):
  if hands[x][-1]==-1 or hands[x][-1]==-2:
    pass
#pass if busted or stood
  else:
    print(f"{hands[x][0]} your hand is",end=' ')
    for y in range(1,len(hands[x])):
      print(deck[1][deck[0].index(hands[x][y])],end=' ')
    decision=input("would you like to stand('s') or hit('h')")
    
    if decision=='s':
      hands[x].append(-1)
      
    elif decision=='h':
      dealCard(hands[x],deck)
# if busted (0) print hand and update status
      if checkBust(hands[x],deck,players)==0:
        print(f"{hands[x][0]}'s hand:'")
        for i in range(1,len(hands[x])):
          print(deck[1][deck[0].index(hands[x][i])])
        print(f"{hands[x][0]} has gotten over 21!\n{hands[x][0]} has busted!")
        hands[x].append(-2)
# if did not bust, show hand and continue
      else:
        print(f"{hands[x][0]}'s hand:'")
        for i in range(1,len(hands[x])):
          print(deck[1][deck[0].index(hands[x][i])])

# def dealerCheck(hand,total,deck):
#   if total>=17:
#     if total>21:
#       if count==0:
#         hands[0].append(-2)
#       else:
#         total=total-10
        
                
#     else:
#       hands[0].append(-1)

def thePlay(deck,hands,players):
  while True:
    if checkEnd(hands,players)==True:
      break
    for x in range(1,players+1):
  
  #Dealer's Play
            
      if x == players:
        dealerPlay(hands,deck,players)
      
  #Regular Player's Play
  
  # [-1] is stand, [-2] is bust
                    
      else:
        playerPlay(hands,deck,players,x)


def mainmenu():

  loop=1
  deck=[["010","011","012","013","020","021","022","023","030","031","032","033","040","041","042","043","050","051","052","053","060","061","062","063","070","071","072","073","080","081","082","083","090","091","092","093","100","101","102","103","110","111","112","113","120","121","122","123","130","131","132","133"],["A Clubs","A Diamonds","A Hearts","A Spades","2 Clubs","2 Diamonds","2 Hearts","2 Spades","3 Clubs","3 Diamonds","3 Hearts","3 Spades","4 Clubs","4 Diamonds","4 Hearts","4 Spades","5 Clubs","5 Diamonds","5 Hearts","5 Spades","6 Clubs","6 Diamonds","6 Hearts","6 Spades","7 Clubs","7 Diamonds","7 Hearts","7 Spades","8 Clubs","8 Diamonds","8 Hearts","8 Spades","9 Clubs","9 Diamonds","9 Hearts","9 Spades","10 Clubs","10 Diamonds","10 Hearts","10 Spades","J Clubs","J Diamonds","J Hearts","J Spades","Q Clubs","Q Diamonds","Q Hearts","Q Spades","K Clubs","K Diamonds","K Hearts","K Spades"],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,]]

  while loop==1:
    time.sleep(2)
    clear()
    option = int(input("Welcome to BlackJack!\n1: Start a Game\n2: Exit Game\n"))

    if option==2:
      loop==0
      break


    elif option==1:
      players = int(input("Please enter the number of players (2-7): "))
      

      if players<2 or players>7:
        pass



      else:
        
#initializing lists
        hands=[]
        for x in range(players):
          hands.append([])
        for x in range(players):
          if x == 0:
            name = input("Dealer please enter your name: ")
          else:
            name = input(f"Player {x} please enter your name: ")
          hands[x].append(name)
#dealing cards
        
        for x in range(2):
          for y in range(players):
            dealCard(hands[y],deck)

# print(hands)
      
        time.sleep(1)
        print("\nFirst round of dealing:\n")
        time.sleep(1)
        for x in range(players):
          print(f"{hands[x][0]}: {deck[1][deck[0].index(str(hands[x][1]))]}")
          time.sleep(0.5)
        time.sleep(1)
        print("\nSecond round of dealing:\n")
        time.sleep(1)
        for x in range(players):
          if x==0:
            print(f"{hands[x][0]}: {deck[1][deck[0].index(str(hands[x][1]))]} FACE DOWN")
          else:
            print(f"{hands[x][0]}: {deck[1][deck[0].index(str(hands[x][1]))]} {deck[1][deck[0].index(str(hands[x][2]))]}")
          time.sleep(0.5)
        print("\n")
        natural = checkNatural(hands,deck,players)
        if natural==1:
          return 0

# ^^ printing hand

        thePlay(deck,hands,players)

# Calculating scores
        max=0
        winner=[]
        for x in range(0,players):
          if hands[x][-1]==-2:
            pass
          else:
            total=0
            for y in range(1,len(hands[x])-1):
              total=deck[3][deck[0].index(str(hands[x][y]))]+total

            while total > 21:
              total=total-10
            
            # if total>21:
            #   total=total-10
            if total>max:
              max=total
            print(f"{hands[x][0]}: {total}")  
            
        for x in range(0,players):
          if hands[x][-1]==-2:
            pass
          else:
            total=0
            for y in range(1,len(hands[x])-1):
              total=deck[3][deck[0].index(str(hands[x][y]))]+total
              
            if total>21:
              total=total-10
            if total==max:
              winner.append(hands[x][0])
              

        for x in winner:
          print(f"{x} has won the game with a total of {max}!")
        abc=input("Enter a key to continue")

    else:
      print("Please enter '1' or '2'\n")
        
mainmenu()
