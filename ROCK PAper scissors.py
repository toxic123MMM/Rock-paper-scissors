import random
options=["Rock","Paper","Scissors"]
user_choice=input("Choose rock,paper or scissor: ")
Computer_choice=random.choice(options)
print("you choose: ",user_choice)
print("computer choose",Computer_choice)

if user_choice==Computer_choice:
    print("its a tie")
elif user_choice=="Rock" and Computer_choice=="Scissors":
    print("Rock smashes Scissors so you win")
elif user_choice=="Paper" and Computer_choice=="Rock":
    print("paper covers rock so you win")
elif user_choice=="Scissors" and Computer_choice=="Paper":
    print("Scissors cuts paper so you win")
else:
    print("you lose")