def partition(input, l, r, debug = False):
  pivot = input[l]
  print l
  print r

  #analyzed_point = 0
  split_point = l + 1

  for analyzed_point in range(split_point, r):
    if input[analyzed_point] < pivot:
      big_val = input[split_point]
      small_val = input[analyzed_point]
      input[split_point] = small_val
      input[analyzed_point] = big_val
      split_point += 1

  swap_val = input[split_point - 1]
  input[split_point - 1] = pivot
  input[l] = swap_val

  #partition(input, split_point, r)



def quicksort(input, debug = False):
  #quicksort_helper(input, 0, len(input))
  partition(input, 0, len(input), debug)



#test = [1]
#test = [5,3,1,8,2,47,12]
test = [2,4,1,3]
quicksort(test, False)
print test


  # if debug: print ("sorting initial input:",input)
  # if len(input) > 1:
  #   size_boundary = l

  #   for analyzed_boundary in range(l, len(input)):
  #     if input[analyzed_boundary] < input[l - 1]:
  #       big_val = input[size_boundary]
  #       small_val = input[analyzed_boundary]
  #       input[size_boundary] = small_val
  #       input[analyzed_boundary] = big_val
  #       size_boundary += 1

  #   swap_val = input[size_boundary - 1]
  #   input[size_boundary - 1] = input[l - 1]
  #   input[l - 1] = swap_val

  #   return analyzed_boundary