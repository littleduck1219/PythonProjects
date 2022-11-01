# Caesar cipher 카이사르 암호

## RUN(실행) -> https://replit.com/@littleduck1219/caesar-cipher-4-start?v=1

## 동작방법

input 값으로 'encode', 'decode'와 'message', 'shift'를 입력하면 'shift' 만큼 변환되어 암호가 만들어진다.

message를 alphabet의 index와 대조 시키고 shift 값을 더하거나 뺴서 new_position에 답고 end_text에 담아 문자열을 완성시킨다. 이때 message값에 숫자나 특수문자가 있을시 변환하지 않고 그대로 반환한다.
암호를 완성한 후에 "Type 'yes' if you want to go again. Otherwise type 'no'"를 물어본후 yes 또는 no에 따라 프로그램을 재실행하거나 종료할 수 있다.

## 회고

이번 프로그래밍으로 고민 해야했던 부분은 alphabet은 26개 인데 입력값에 맞춰 26을 넘어가 면 다시 1부터 인식하기 위해 
shift = shift%26을 입력하였다. 나머지값으로 index를 선택하게 하였다.
두번째로 8번째 줄의 if 문에서 decode일시 shift_amount를 *= -1로 하여 encode, decode 모두에 적용할 수 있는 짧은 코드를 만들었는데 반복하면서 -1 * -1 상황이 발생해서 짝수 번째 글자는 -가 아닌 +로 되었고 그래서 if 문을 for 문 밖으로 꺼내면서 해결되었다. 배열을 이용한 좋은 코딩 활동이였다고 생각한다.