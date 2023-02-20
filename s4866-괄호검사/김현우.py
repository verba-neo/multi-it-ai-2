testCase = int(input())

for i in range(testCase):
    string = input()
    stack = []
    check = []
    for j in string:
        if j == '{' or j == '(': #열린 괄호라면 input
            stack.append(j)
        elif len(stack) == 0 and j=='}' or len(stack) == 0 and j==')': #스택안에 아무것도 없는데 만났을때
            check.append(0) #check 에 append 이후 break
            break
        elif len(stack)>0:
            if j == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    check.append(0)
                    break
            elif j == ')':
                if stack[-1] =='(':
                    stack.pop(-1)
                else:
                    check.append(0)
                    break
    if len(stack)==0 and len(check)==0:
        check.append(1)
    elif len(stack)!=0:
        check.append(0)
    print('#'+str(i+1)+' '+str(check[-1]))
주어진
입력에서
괄호
{}, ()
가
제대로
짝을
이뤘는지
검사하는
프로그램을
만드시오.

예를
들어
{( )}
는
제대로
된
짝이지만, {(})
는
제대로
된
짝이
아니다.입력은
한
줄의
파이썬
코드일수도
있고, 괄호만
주어질
수도
있다.

정상적으로
짝을
이룬
경우
1, 그렇지
않으면
0
을
출력한다.

print(‘{‘) 같은
경우는
입력으로
주어지지
않으므로
고려하지
않아도
된다.

[입력]

첫
줄에
테스트
케이스
개수
T가
주어진다.
1≤T≤50

다음
줄부터
테스트
케이스
별로
온전한
형태이거나
괄호만
남긴
한
줄의
코드가
주어진다.

[출력]

각
줄마다
"#T"(T는
테스트
케이스
번호)를
출력한
뒤, 답을
출력한다.

입력
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
sample_input.txt
출력
# 1 1
# 2 1
# 3 0