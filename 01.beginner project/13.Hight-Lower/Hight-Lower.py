from art import logo
from art import vs
from game_data import data
import random
from replit import clear

  
def format_data(account):
  """account data를 형식에 반영합니다."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
  """guess 값이 follower 수의 대소와 비교하여 정답인지 확인합니다."""
  if a_follower_count > b_follower_count:
    return guess=="a"
  else:
    return guess=="b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_b = random.choice(data)
  
  while game_should_continue:
    #game_data에서 랜덤으로 데이터를 뽑습니다.
    account_a = account_b 
    account_b = random.choice(data)
    #a,b가 같은 경우 b를 재 생성 합니다.
    if account_a == account_b:
      account_b = random.choice(data)
    
    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' ore 'B' : ").lower()
    
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    
    if is_correct:
      score += 1
      print(f"You're right! Current score : {score}.")
    else:
      game_should_continue = False
      print(f"Sorry that's wrong. Final score : {score}.")
    

game()
