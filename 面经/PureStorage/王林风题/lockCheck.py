def check_log_history(events):
	stack = []
	visited = set()
	for index, event in enumerate(events):
		operator, lock = event.split()
		if operator == "ACQUIRE":
			if lock not in visited:
				stack.append(lock)
				visited.add(lock)
				print('in')
			else:
				return index + 1
		elif operator == 'RELEASE':
			if not stack or lock != stack.pop():
				return index + 1
			else:
				visited.discard(lock)

	return len(events) + 1 if (stack or visited) else 0
