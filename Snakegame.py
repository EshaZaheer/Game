# Snake gun and water game...
# it takes 2 players user and computer

import random  #random is used to generate randome values

computer = random.randint(0,2) #the computer variable will generate random value in range 0-2

print('Welcome To The Snake water and gun Game \n 0 = snake \n 1 = water \n 2 = gun')

valid_choice = [0,1,2]

a = 1

# this while will continue the game
while True:
    # this while will continue untill the user enter valid input
    while (a == 1):
            #try is use to capture invalid input
            try: 
                user = int(input('Enter your move: '))
                if user not in valid_choice:
                 print('please enter range 0-2')
                 a = 1
                else:
                 break
            except ValueError as e:
                print(e)
                      
        
    
    # f string is used
    print(f"computer => {computer} ")

    #the result for the game
    if(user == computer):
        print('Its a Draw')
    elif(user == 0 and computer == 1):
        print("You Win")
    elif(user == 0 and computer == 1):
        print("You Win")
    elif(user == 0 and computer == 1):
        print("You Win")
    else:
        print('You Lose')
