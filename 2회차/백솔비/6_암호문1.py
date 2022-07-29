import sys

sys.stdin = open("_암호문1.txt")

for tc in range(10):
    N = int(input())
    password = list(map(int, input().split()))
    command_len = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            # 명령문의 I 다음 글자가 x, 그 다음 글자가 y이므로 해당 식으로 설정해줍니다.
            x = int(command[i+1])
            y = int(command[i+2])
    
            for j in range(y):
                # insert(위치, 삽입할 내용)을 통해 password에 코드를 삽입해줍니다.
                password.insert(x+j, int(command[i+2+(j+1)]))
                print(j)

    # 배열 형태에서 벗어나기 위해 join을 사용해 result에 저장해줍니다.       
    result = ' '.join(map(str,password[:10]))

    # print(f'#{tc+1} {result}')