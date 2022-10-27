## 05.paswword generator

### 각 문자, 특수문자, 숫자의 갯수를 입력받아 랜덤 조합으로 비밀번호를 생성합니다.

### ->> 실행 : https://replit.com/@littleduck1219/password-generator-start?v=1

리스트를 생성하여 각각 영어 대소문자, 특수문자, 숫자를 입력해 놓고

input으로 숫자를 입력받아 해당하는 갯수만큼 출력하여 랜덤으로 조합하는 프로그램입니다.

import random<br>

letters = [<br>
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',<br>
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',<br>
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',<br>
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'<br>
]<br>
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']<br>
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']<br>
<br>
print("Welcome to the PyPassword Generator!")<br>
nr_letters = int(input("How many letters would you like in your password?\n"))<br>
nr_symbols = int(input(f"How many symbols would you like?\n"))<br>
nr_numbers = int(input(f"How many numbers would you like?\n"))<br>
<br>
password = []<br>
<br>
for nl in range(1, nr_letters + 1):<br>
    password += random.choice(letters)<br>
for nr in range(1, nr_symbols + 1):<br>
    password += random.choice(symbols)<br>
for nn in range(1, nr_numbers + 1):<br>
    password += random.choice(numbers)<br>
<br>
random.shuffle(password)<br>
print("".join(password))<br>

### 회고

크게 어렵지 않았으나 마지막에 랜덤으로 비밀번호를 조합하기위하여 suffle을 처음 사용하였고,
suffle을 사용하기위해서 password를 단순 문자열로 만들었던 것을 list로 변경하였습니다.
이때 까지 배운내용을 간단하게 복습하기 좋은 코딩작업이였습니다.