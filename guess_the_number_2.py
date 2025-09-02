'''Greatings. This is an evelotion of the classic game guess the number
\033...\033[0m this kind of code cganges the color of the print function

'''
import random
print("This is a version of Guess The Number for Singleplayers Or Multiplayers")
number_of_gamers = int(input("\033[32mSo... How many peaple are going to play (max 5) ->\033[0m"))




#chose the mode of game
while number_of_gamers <= 0 or number_of_gamers > 5:
    print("\033[31mEnter a Valid option please\033[0m")
    number_of_gamers = int(input("\033[32mHow many peaple are going to play (max 5) ->\033[0m"))
#multiplayer mode    
if number_of_gamers >=2:
   #number of players in multiplayer
   print(f"---------This is a simple game of guessing the number\n---------Each round each player will be asked whats is number\n---------And the computer will say if its to high or to low\n---------Until someone gets it right!!! ")
   if number_of_gamers == 2:
    game_number = random.randint(0,200)
    print(f"---------There will be {number_of_gamers} playing therefor the range of guessing is from (0, 200)")
   elif number_of_gamers == 3:
    game_number = random.randint(0,300)
    print(f"---------There will be {number_of_gamers} playing therefor the range of guessing is from (0, 300)")
   elif number_of_gamers == 4:
    game_number = random.randint(0,400)
    print(f"---------There will be {number_of_gamers} playing therefor the range of guessing is from (0, 400)")
   else:
       game_number = random.randint(0,500)
       print(f"---------There will be {number_of_gamers} playing therefor the range of guessing is from (0, 500)")
   #setting the gamers name
   gametags = []
   for i in range(number_of_gamers):
       name = input(f"\033[33mEnter the gametag for player_{i+1}->\033[0m")
       gametags.append(name)
   print("Players registered -> " + ", ".join(gametags))
   guess = 0
   trys = 0
   winner = False
   # the multiplayer inded
   while winner == False:
    random.shuffle(gametags)
    for player in gametags:
        guess = int(input(f"\033[33m{player} whats your guess? ->\033[0m"))
        trys+=1
        if guess == game_number:
            print(f"\033[32mCongrats {player}!! you have guessed the right number {game_number}\033[0m")
            print(f"It took {trys} guesses")
            winner = True
            again = input("\033[33mDo you want to continue?\nY or N?? ->\033[0m").strip()

            while again.lower() not in ("y", "n"): 
                        again = input("\033[31mEnter a valid option\nY or N?? ->\033[0m").strip()

            if again.lower() == "y":
                print("OK")
                #reseting all game stats 
                if number_of_gamers == 2:
                    game_number = random.randint(0,200)
                elif number_of_gamers == 3:
                    game_number = random.randint(0,300)
                elif number_of_gamers == 4:
                    game_number = random.randint(0,400)
                else:
                    game_number = random.randint(0,500)
                guess = 0  
                trys = 0
                winner = False
            elif again.lower() == "n":
                    print("\033[32mThanks for playing!\033[0m")
                    break
        elif guess > game_number:
            print("\033[31mThat's to high\033[0m")
            
        elif guess < game_number:
            print("\033[34mThat's to low\033[0m")
            
        else:
            print(f"\033[31m{player} enter a valid guess\033[0m")
            guess = int(input(f"{player} whats your guess? ->"))
    
    
   
     
  

#single player mode    

else:
    print("---------Game of the guess the number\n---------If you are 7 numbers or less of finding the number \n---------there will be an message saying 'burning'\n---------If you are less than 20 numbers it will say 'hot'\n---------If not it will say 'cold' ")
    input("\033[33mALL GOOD? ->\033[0m")
    hiden_number = random.randint(1,100)
    gamers_guess = 0
    number_guesses = 0
    while True:

        while gamers_guess != hiden_number:

            gamers_guess = int(input("\033[33mWhat's your guess? ->\033[0m"))

            if gamers_guess <= (hiden_number+7) and gamers_guess >= (hiden_number-7):
                print("\033[31mBURNING🔥\033[0m")
                number_guesses += 1
            elif gamers_guess <= (hiden_number+20) and gamers_guess >= (hiden_number-20):
                print("\033[31mHOT🌡\033[0m")
                number_guesses += 1
            else:
                print("\033[34mCOLD❄\033[0m")
                number_guesses += 1
        print(f"\033[32mIt took you {number_guesses} guesses!!!\033[0m")        
        print("Congrats you guessed the number!!!!"+ str(hiden_number) +" was the number this time")
        again = input("\033[33mDo you want to continue?\nY or N?? ->\033[0m").strip()

        while again.lower() not in ("y", "n"): 
            again = input("\033[31mEnter a valid option\nY or N?? ->\033[0m").strip()

        if again.lower() == "y":
            print("OK")
            hiden_number = random.randint(1, 100) 
            gamers_guess = 0  
            number_guesses = 0
        elif again.lower() == "n":
            print("Thanks for playing!")
            break
