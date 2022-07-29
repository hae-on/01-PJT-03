import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())


for tc in range(1, T+1):
    side = list(map(int, input().split()))

    d = {}

    # 직사각형의 변을 딕셔너리 형태로 넣어줍니다.
    for i in side:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    result = ''

    # 직사각형이므로 두변의 길이가 같고, 다른 두변의 길이가 같습니다. 
    # 딕셔너리에서 value 값이 2라면 같은 변 길이는 이미 있다는 말입니다.
    # 1인 key를 출력하도록 합니다.
    # 만약 value 의 값이 3이라면 정사각형이라는 소리므로 key를 출력하면 됩니다.
    for key, value in d.items():
        if value == 1:
            result = key
        elif value == 3:
            result = key

    print(f'#{tc} {result}')