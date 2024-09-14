import random
def choice():
    print("\nRock, Paper, Scissors Game")
    print("Choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def computer_choice():
    b=random.choice([1, 2, 3])
    print("computer choice:",b)
    return b
def result(c,d):
    if c == d:
        return "Tie"
    elif (c== 1 and d== 3) or (c == 2 and d == 1) or (c == 3 and d == 2):
        return "Winner:User"
    else:
        return "Winner:Computer"
def game(ch,a):
    if(ch==1) and (a==2):
        print("\nYour choice:Rock")
        print("Computer's choice:Paper")
    elif(ch==1) and (a==3):
        print("\nYour choice:Rock")
        print("Computer's choice:Scissors")
    elif(ch==2) and (a==3):
        print("\nYour choice:Paper")
        print("Computer's choice:Scissors")
    elif(ch==3) and (a==2):
        print("\nYour choice:Scissors")
        print("Computer's choice:Paper")
    elif(ch==2) and (a==1):
        print("\nYour choice:Paper")
        print("Computer's choice:Rock")
    elif(ch==3) and (a==1):
        print("\nYour choice:Scissors")
        print("Computer's choice:Rock")
    elif(ch==1) and (a==1):
        print("\nYour choice:Rock")
        print("Computer's choice:Rock")
    elif(ch==2) and (a==2):
        print("\nYour choice:Paper")
        print("Computer's choice:Paper")
    else:
        print("\nYour choice:scissors")
        print("Computer's choice:Scissors")
        
def rps():
    choice()
    ch=get_user_choice()
    a=computer_choice()
    game(ch,a)
    print(result(ch,a))
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
    else:
        rps()
rps()
