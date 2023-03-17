import itertools


def solution(ability, number):
	a = ability
	n = number
	for k in range(n):
		c = list(itertools.combinations(a, n))
		m = 0
		man1 = 0
		man2 = 0
		for i in c:
			j = sum(i)
			if i == c[0]:
				m = j
				man1 = i[0]
				man2 = i[1]
			elif j < m:
				m = j
				man1 = i[0]
				man2 = i[1]
		idx = a.index(man1)
		idx_2 = a.index(man2)
		while idx_2 == idx:
			idx_2 = a.index(man2)

		a[idx] = m
		a[idx_2] = m
	return sum(a)


abilities = [10, 3, 7, 2]
numbers = 2

print(solution(abilities, numbers))

