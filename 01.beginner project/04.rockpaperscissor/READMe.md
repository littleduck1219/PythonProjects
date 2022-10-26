## 04.rock_paper_scissor

### random을 import하여 random숫자를 받아 직접 입력한 값과 조건문을 사용하여 가위바위보 프로그램을 코딩하였습니다.

### ->> 실행 : https://replit.com/@littleduck1219/04rock-paper-scissors?v=1


import random 

rsp = [rock, paper, scissors]
그림으로 호출하기 위해 리스트에 변수로 이미지를 담기.

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if user_choice > 2 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(rsp[user_choice])

각 0,1,2에 따른 바위, 보, 가위로 변환(정수형으로 받는다)
조건문을 사용하여 만약 사용자가 2이상의 숫자를 입력하면 패배로 간주하고 종료 -


  computer_choice = random.randint(0, 2)
  print(f'Computer chose {rsp[computer_choice]}')
  
  if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose!")
  elif computer_choice == 2 and user_choice == 0:
    print('You win!')
  elif computer_choice == 0 and user_choice ==2:
    print('You lose!')
  elif computer_choice > user_choice:
    print('You lose!')
  elif computer_choice < user_choice:
    print('You win!')
  elif computer_choice == user_choice:
    print("It's a draw")

가위 바위 보의 승리, 패배 조건을 입력하여 승패가 가려 질 수 있도록 입력한다.

### 회고

11번쨰 줄의 if 문을 입력 하지 않고 아래 조건들을 쭉 나열했더니 14번의 user_choice에서 index error가 발생하였다.
14번째 줄은 사용자의 이미지를 출력하는 줄 이다. 해결하기 위해서 if문으로 전체 범위에대한 조건문을 입력하였고 true 값으로 범위를 벗어나는 값을 주었고 범위 값을 입력하면 아래 코드로 실행이 되도록 하였다.
그렇게 했더니 사용자의 값이 두번 출력되는 일이 발생하였고, 해결학 위해서 이후 모든 코드를 14번째 줄 아래로 두어 두번 실행되지 않게 하였다.