import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for tc in range(1, T+1):
    str_ = input()
    # 거울에 비친 모습을 위해 문자열을 반대로 출력합니다.
    rev_str = str_[::-1]
    
    result = ''

    # 반대의 모습에서 또 좌우 대칭되므로 각 해당 글자로 변환해줍니다.
    for i in rev_str:
        if i == 'q':
            result += 'p'
        elif i == 'p':
            result += 'q'
        elif i == 'd':
            result += 'b'
        elif i == 'b':
            result += 'd'
    
    print(f'#{tc} {result}')
  