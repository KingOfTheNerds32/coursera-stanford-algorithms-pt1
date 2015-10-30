import math
def merge_sort(input, debug = False):
	if debug: print ("Splitting", input)
	if len(input) > 1:
		mid_length = len(input)//2 
		left_half = input[:mid_length]
		right_half = input[mid_length:]

		# print left_half
		# print right_half

		merge_sort(left_half, debug)
		merge_sort(right_half, debug)

		l = 0
		r = 0
		k = 0

		if debug: print("before combining", left_half, right_half)
		while l < len(left_half) and r < len(right_half):
			if left_half[l] < right_half[r]:
				input[k] = left_half[l]
				l += 1
			else:
				input[k] = right_half[r]
				r += 1
			k += 1
			if debug: print ("combining both sides", input[k - 1],input)

		while l < len(left_half):
			input[k] = left_half[l]
			l += 1
			k += 1
			if debug: print("left half:", input[k-1], input)

		while r < len(right_half):
			input[k] = right_half[r]
			r += 1
			k += 1
			if debug: print("right half", input[k-1], input)



test = [3,1,2,1,78,47,12]
merge_sort(test, debug=False)
print test