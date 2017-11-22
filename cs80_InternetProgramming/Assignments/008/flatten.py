# n = [[1, 2], [3, 4]]
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

results = []

def flatten(lists):
	for arr in lists:
		for numbers in arr:
			results.append(numbers)
	return results

print(flatten(n))