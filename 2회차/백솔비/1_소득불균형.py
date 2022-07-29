import sys

sys.stdin = open("_소득불균형.txt")

T  = int(input())

for tc in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    
    # 전체 평균을 구해줍니다.
    avg = int(sum(income) / len(income))

    cnt = 0

    # 평균보다 같거나 작은 인원을 세줍니다.
    for i in income:
        if i <= avg:
            cnt +=1

    print(f'#{tc} {cnt}')