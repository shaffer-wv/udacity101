def fibonacci(n):
    current = 0
	after = 1
	for i in range(0, n):
		current, after = after, current + after
	return current