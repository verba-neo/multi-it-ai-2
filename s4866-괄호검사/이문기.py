import sys
sys.stdin = open('input.txt')
T = int(input())
for _ in range(T):
	input_sentence = list(input())
	el = [] #extracted_list

	#괄호만 추출 하는 루프
	for k in input_sentence:
		if k == '(' or k == ')' or k == '[' or k == ']' or k == '{' or k == '}':
			el.append(k)

	#추출한 리스트의 길이 1/2
	length = int(len(el) / 2)
	i = 0

	# 추출된 리스트 길이의 1/2 만큼 반복
	for _ in range(length):
		# 1쌍의 괄호가 삭제 될때까지 반복
		while True:
			if el[i] == '(':
				if el[i+1] == ')':
					del el[i]
					del el[i]
					i = 0
					break
				else:
					i += 1
			elif el[i] == '[':
				if el[i+1] == ']':
					del el[i]
					del el[i]
					i = 0
					break
				else:
					i += 1
			elif el[i] == '{':
				if el[i+1] == '}':
					del el[i]
					del el[i]
					i = 0
					break
				else:
					i += 1
			else:
				i += 1
		# 삭제후 리스트 원소가 0개 or 1개일 경우 검사 종료
		if len(el) == 0 or len(el) == 1:
			break

	# 원소가 0개면 올바른 값 , 1개면 올바르지 않은 값
	if len(el) == 0:
		print('1')
	else:
		print('0')



