def days_between_higher_temp(temperatures):
	counter = 1
	list_of_days = []
	for val in range(0, len(temperatures) - 1):
		for val2 in range(val + 1, len(temperatures) - 1):
			if temperatures[val] < temperatures[val2]:
				break
			else:
				counter += 1
				if counter == len(temperatures) - val:
					print(val2)
					counter = 0
		list_of_days.append(counter)
		counter = 1
	list_of_days.append(0)
	return list_of_days


print(days_between_higher_temp([0, -1, -15, -15, -8, 23]))
