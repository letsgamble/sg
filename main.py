def days_between_higher_temp(temperatures):
	counter = 1
	list_of_days = []
	for val in range(0, len(temperatures)):
		for val2 in range(val + 1, len(temperatures)):
			if temperatures[val] < temperatures[val2]:
				break
			elif temperatures[val] >= temperatures[val2]:
				counter += 1
				if counter == len(temperatures) - val:
					counter = 0
		list_of_days.append(counter)
		counter = 1
	return list_of_days


days_between_higher_temp([15, -1, 15, -1, -1, 10])
