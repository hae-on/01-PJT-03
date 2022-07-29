import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for tc in range(1, T+1):
    card_number = input()

    conditional1 = ''

    # 첫번째 조건에 따라 첫번째숫자가 3, 4, 5, 6, 9로 시작하는지 체크해줍니다.
    if card_number[0] == '3' or card_number[0] == '4' or card_number[0] == '5' or card_number[0] == '6' or card_number[0] == '9':
        conditional1 = 1
    else:
        conditional1 = 0

    conditional2 = ''
    # 두번째 조건에 따라 '-'를 제외한 글자수가 16개인지 체크해줍니다.
    newCard_number = card_number.replace('-', '')

    if len(newCard_number) != 16:
        conditional2 = 0
    else:
        conditional2 = 1

    # 조건 1, 2 두개가 모두 1인 경우만 출력합니다.
    print(f'#{tc} {conditional1&conditional2}')

  