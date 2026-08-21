WINDOW_SIZE = 3
i = 0
j = WINDOW_SIZE - 1

lst = [4, 3, 5, 2, 6, 6]
lst_len = len(lst)

current_sum = 0

for	k in range(i, j+1):
	current_sum += lst[k]

print(current_sum)

while j+1 < lst_len:
	current_sum -= lst[i]
	i += 1

	j += 1
	current_sum += lst[j]
	
	print(current_sum)