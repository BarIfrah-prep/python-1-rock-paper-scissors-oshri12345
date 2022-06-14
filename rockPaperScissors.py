
import random
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
       "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")
qr = int(input("if you want to play again press 5, "))
w = 0
while w == 0:
    player1 = input("what your name ? ,   ")
    player2 =  " the computer "

    oshri = int(input(f"Hey {player1} please choose, 1 for `Rock` , 2 for `Paper` , 3 for `Scissors`,    "))
    asher = random.randint(1,3)
    if w == 0:


       if oshri == 1 and asher == 2:
        print(f"{player1} choos `Rook` and {player2} choos `Paper` , {player2} the winner !")
       elif oshri == 1 and asher == 3:
          print(f"{player1} choos `Rook` and {player2} choos `Scissors` , {player1} the winner !")
          continue
       if oshri == 2 and asher == 1:
          print(f"{player1} choos `Paper` and {player2} choos `Rock` , {player1} the winner !")
       elif oshri == 2 and asher == 3:
          print(f"{player1} choos `Paper` and {player2} choos `Scissors` , {player2} the winner !")
          continue
       if oshri == 3 and asher == 1:
          print(f"{player1} choos `Scissors` and {player2} choos `Rock` , {player2} the winner !")
       elif oshri == 3 and asher == 2:
          print(f"{player1} choos `Scissors` and {player2} choos `Paper` , {player1} the winner !")
          continue
       if oshri == asher:
          print("Draw! please try again")
       elif oshri > 3 or asher > 3:
          print("wrong choice please try again")
          continue
       qr = int(input("to play again press 5, "))
       if qr == 5:
          print("let's play again")
       else:
           w += 1
