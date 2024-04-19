from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  """
  REMEMBER, you can deflate, but CANNOT inflate
  so, when going through the elements, if less than previous -> cannot touch!(??) and reset the radius to start counting from
  
  thought: Break into smaller lists? while it is bigger or equal add to partial list, otherwise start a new list

  in any case
    first figure if it is possible or impossible?
        impossible: if the last element is less or equal than the lenght of the list, then it is impossible
        and so on, repeat with each element
        potentially possible: otherwise it is potentially possible

  Approach
    Two lists and map. 

  Approach
    One list and comprehension?
    Start from the last element, or reverse the list  
  """
  print("last element of R", R[-1], "and N", N)
  # Case, impossible
  # Radius of bottom disk R[-1] is less than the number of disks N in the stack
  if R[-1] < N:
    return -1
  
  # Reverse the list
  # Auxiliary space: O(1) since it modifies the original list in place and does not create a new list.
  # https://www.geeksforgeeks.org/python-reversing-list/
  R.reverse()
  print("reversed list", R, "\n")
  
  # delete the bottom disk
  bottom_disk = R.pop(0)
  last_stable_index = 0
  deflated_disks = 0
  for i, r in enumerate(R):
    print("at loop start bottom disk is", bottom_disk, "top disk is", r, "list is", R)
    print("focus on", r)
    # Case: unstable
    if bottom_disk <= r:
      print("compare bottom disk", bottom_disk, "with top disk", r, "is UNSTABLE")
      R[i] = bottom_disk - 1
      print("after deflating the list looks like", R)
      # reset the bottom disk for the next iteration
      bottom_disk = R[i]
      # increase counter of deflated disks
      deflated_disks = deflated_disks + 1
    # Case: stable
    else:
      print("compare bottom disk", bottom_disk, "with top disk", r, "is STABLE")
      # reset the bottom disk for the next iteration
      bottom_disk = r
      # in case we need to come back and keep on deflating
      last_stable_index = i

    print("at loop END bottom disk is", bottom_disk, "list is", R)

  # End
  return deflated_disks


if __name__ == '__main__':
    
    # Sample test case #1
    N = 5
    R = [2, 5, 3, 6, 5]
    expected_return_value = 3
    my_calculation = getMinimumDeflatedDiscCount(N, R)
    print("Case: valid input")
    print("For N:", N, "disks", 
          ", and stack R:", R, ", the minimum number of disks to be deflated",
          " in order to have a stable stack is:", my_calculation)
    if my_calculation == expected_return_value:
      print(f"SUCCESS, your function has returned {my_calculation} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_calculation} and the correct value is {expected_return_value}") 
    print("\n")

    # Sample test case #2
    N = 3
    R = [100, 100, 100]
    expected_return_value = 2
    my_calculation = getMinimumDeflatedDiscCount(N, R)
    print("Case: valid input")
    print("For N:", N, "disks", 
          ", and stack R:", R, ", the minimum number of disks to be deflated",
          " in order to have a stable stack is:", my_calculation)
    if my_calculation == expected_return_value:
      print(f"SUCCESS, your function has returned {my_calculation} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_calculation} and the correct value is {expected_return_value}") 
    print("\n")

    # Sample test case #3
    N = 4
    R = [6, 5, 4, 3]
    expected_return_value = -1
    my_calculation = getMinimumDeflatedDiscCount(N, R)
    print("Case: valid input")
    print("For N:", N, "disks", 
          ", and stack R:", R, ", the minimum number of disks to be deflated",
          " in order to have a stable stack is:", my_calculation)
    if my_calculation == expected_return_value:
      print(f"SUCCESS, your function has returned {my_calculation} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_calculation} and the correct value is {expected_return_value}") 
    print("\n")