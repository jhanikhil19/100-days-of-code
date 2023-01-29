#Snake Water Gun Game
#Snake drinks water
#Water corrodes gun
#Gun kills Snake

#Play with the computer
#Use While or For loop


import random

list1=["Snake","Water","Gun"]
# Comp_choice=random.choice(list1)
comp=0 #score
usr=0 #score
n=5
for i in range (0,n):
    Comp_choice = random.choice(list1)
    user_choice = int(input("Enter your choice 1.Snake 2.Water 3.Gun"))
    if(Comp_choice=="Snake" and user_choice==1):
        print("Computer and User Entered the same value. Please try again.")
        # i+=i
    elif(Comp_choice=="Water" and user_choice==2):
        print("Computer and User Entered the same value. Please try again.")
        # i += i
    elif(Comp_choice=="Gun" and user_choice==3):
        print("Computer and User Entered the same value. Please try again.")
        # i += i
    elif(Comp_choice=="Snake" and user_choice==2):
        print("COMPUTER wins as SNAKE drank the water.")
        comp=comp+1
        # i += i
    elif (Comp_choice == "Snake" and user_choice == 3):
        print("USER wins as SNAKE KILLED BY GUN")
        usr = usr + 1
    elif (Comp_choice == "Water" and user_choice == 1):
        print("USER wins as SNAKE drank the water.")
        usr = usr + 1
    elif (Comp_choice == "Water" and user_choice == 3):
        print("COMPUTER wins as WATER destroys GUN.")
        comp = comp + 1
    elif (Comp_choice == "Gun" and user_choice == 1):
        print("COMPUTER wins as GUN kills SNAKE.")
        comp = comp + 1
    elif (Comp_choice == "Gun" and user_choice == 2):
        print("USER wins as WATER destroys GUN.")
        usr = usr + 1
    else:
        print("Invalid Input")

    print("*" * 10)
    print("Round #",i+1)
    print("Computer Score : ",comp)
    print("User Score : ",usr)
    print("*"*10)

if(comp>usr):
    print("COMPUTER WINS")
else:
    print("USER WINS")

