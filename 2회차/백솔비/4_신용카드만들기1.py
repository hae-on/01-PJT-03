import sys

sys.stdin = open("_신용카드만들기1.txt")

T= int(input())

for tc in range(1, T+1):

    N = list(map(int,input().split()))

    # 짝수와 홀수번째를 나누어 배열에 담아줍니다. 0부터 시작하므로 짝수와 홀수를 실제와는 반대?입니다.
    odd = N[0::2]
    even = N[1::2]

    # 홀수에 *2를 곱해주고 더한 값을 구하고, 짝수에 합을 구해줍니다.
    odd_ = map(lambda x: x*2, odd)
    result_odd = sum(list(odd_))
    result_even = sum(even)

    #둘을 더해줍니다.
    whole_sum = result_odd + result_even
   
    answer = ''

    # 만약 10으로 나누어떨어지면 N은 0입니다.
    # 나누어 떨어지지 않는다면 10에서 10으로 나눈 나머지 값을 빼주면 N의 값이 나옵니다.
    if whole_sum % 10 == 0:
        answer = 0
    else :
        answer = 10 - whole_sum % 10
    
    print(f'#{tc} {answer}')