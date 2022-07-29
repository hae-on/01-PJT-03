import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores= list(map(int,input().split()))
    # 0부터 100까지 카운트 할 배열을 설정합니다.
    score_list = [0] * 101

    #score_list 배열에 각 점수가 있으면 카운트 해줍니다.
    for score in scores:
        score_list[score] += 1

    # 그 중 가장 많이 나온 최빈수를 찾습니다.
    max_ = max(score_list)
    result = []

    # 최빈수의 i 값을 따로 배열에 넣어줍니다.
    for i in range(len(score_list)):
        if score_list[i] == max_:
            result.append(i)

    # 최빈수가 1개 이상인 경우 그 중 큰 수를 출력합니다.
    print(f'#{tc} {max(result)}')