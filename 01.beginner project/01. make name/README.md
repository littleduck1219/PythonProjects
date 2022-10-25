## welcome to the life in Weeks

input으로 받은 입력값을 F-String을 이용하여 결합하여 출력하는 실습내용입니다.

```print("Welcome to the Life in Weeks")```<br>
welcome to the Life in Weeks를 출력합니다

```first_name = input("What is your first name?")``` #input first name<br>
first_name 이라는 변수에 input으로 성을 입력받습니다

```last_name = input("What is your last name?")``` # input last name<br>
last_name 이라는 변수에 input으로 이름을 입력받습니다.

```age = input("What is your current age?")``` # input your age<br>
age 라는 변수에 나이값을 입력 받습니다.

```left = 90 - int(age)``` # this assuming your life is up to 90<br>
left라는 변수에 최대 나이를 90세라고 가정하고 남은 값을 계산하여 저장합니다.

```print(f" {first_name} {last_name}\nyou have {left*365} days, {left*52} weeks, and {left*12} months left.")```<br>

F-String을 이용하기 위해 제일 앞단에 f를 입력하고 ""안에 입력을 시작하고 {}안에 변수를 입력하여 출력을 합니다.(1년 365일 52주 12개월 윤년은 무시하고 90세까지 산다고 가정합니다.)
