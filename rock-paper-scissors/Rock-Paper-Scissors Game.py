import random as rn
def human_input(hi):
    if hi in option:
        return hi
    else:
        print(" chaoise the valid input(1,2,3)")
        return None

option={1:'rock',2:'paper',3:'scissor'}
user_scor=0
com_scor=0
print("Simple Rock, Paper Scissors Game")
print("choice the option")
while True:
 print('1. Rock ')
 print('2. Paper ')
 print('3. Scissor ')
 human=int(input("Enter your choice: "))
 h=human_input(human)
 if h is None:
    continue
 user=(option[h])
 computer=rn.choice(list(option.keys()))
 computer=(option[computer])
 print(f"you are chosie {user}")
 print(f"computer is choise is {computer}")
 if user==computer:
    print("match is drow")
 elif(user=="rock" and computer=="scissor") or (user=="scissor" and computer=="paper") or (user=="paper" and  computer=="rock"):
    print("Your are win🏆🎉")
    user_scor +=1
 else:
    print("Computer is Win")
    com_scor+=1

 print(f"Your Scoer is 🫡 ={user_scor}")
 print(f'Computer Scoer is 🖥️ = {com_scor}')
 