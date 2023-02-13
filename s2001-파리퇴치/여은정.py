import sys
sys.stdin = open('./input.txt')  #  test case 읽어 오기 

def flyCatch():
    T = int(input()) # 숫자로 데이터 인풋 
    for tc in range(1, T+1):
        
        N,M = map(int,input().split())
        #print(f'N:{N}')
        #print(f'M:{M}')
        # 2차원 배열 만들기 
        arr = [[0 for j in range(N)] for i in range(N)]
        
        
        # 배열 정렬하기 
        for i in range(0, N):
            #temparr = list(map(int, input().split()))
            arr[i] = list(map(int, input().split()))
            # 
        # print(arr)
        
        sumValue = 0
        # 파리 잡고 
        for j in range(M-1, 2*M-1):
            if (j < N) :
                for k in range(M-1, 2*M-1):
                    # print(f'[{j}][{k}]')
                    if (k < N ) :
                        # print(arr[j][k])
                        sumValue+= arr[j][k]
                
        print(f'#{tc} {sumValue}')

flyCatch() 
    
	