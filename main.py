import random

'''
-1 for snake
0 for water
1 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": -1, "w": 0, "g": 1}
reverseDict = {-1: "Snake", 0: "Water", 1: "Gun"}

You = youDict[youstr]

print(f'Computer chose {reverseDict[computer]}\n You chose {reverseDict[You]}')

if(computer == You):
    print("It's a Draw!")
else:
    if(computer == -1 and You == 0):
        print("You Lose!")
    elif(computer == -1 and You == 1):
        print("You Win!")
    elif(computer == 0 and You == -1):
        print("You Win!")
    elif(computer == 0 and You == 1):
        print("You Lose!")
    elif(computer == 1 and You == -1):
        print("You Lose!")
    elif(computer == 1 and You == 0):
        print("You Win!")
    else:
        print("Something went wrong!")
