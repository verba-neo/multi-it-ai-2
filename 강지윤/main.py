# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.

def solution(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i

    return sum


if __name__ == '__main__':
    solution(100)


