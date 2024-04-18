from typing import List
import operator
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  """
  Approach
    Build a list with all the starting points
    Build a list with all the ending points. Already given as argument C
    Build a list with the elementwise substraction of the ending and starting lists
    Transform the elementwise list: 
      if abs of the element is less than N/2 (short path) -> keep
      if abs of the element is more than N/2 (long path) -> find the complementatry module
    Sum all the elements of the list
  """
  
  # Verify the arguments against the constraints.  
  # If not valid, inform of the error and terminate.
  try:
     assert isinstance(N, int), f"The number of markers in the wheel, N, that you have provided, {N}, is not an integer."
     assert isinstance(M, int), f"The lenght of the sequence, M, that you have provided, {M}, is not an integer."
     assert isinstance(C, list), f"The sequence, C, that you have provided, {C}, is not a list."
     assert (3 <= N <= 50000000), f"The number of markers in the wheel that you have provided, {N}, is out of bounds."
     assert (1 <= M <= 1000), f"The lenght of the sequence that you have provided, {M}, is out of bounds."
     # C_i must be integers
     # C_i must be less than N
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  
  # Logic, with map
  # Build list of starting and ending points
  # Remove the last element and insert 1 into the first position
  list_starts = C[:-1]
  list_starts.insert(0, 1)
  list_ends = C

  # Auxiliary function 
  def mod_or_comp(a:int, b:int) -> int:
    """Returns the shortest path between a and b

    Since the arguments a and b are lower than N, their substraction (lets 
    call it S) will also be lower than N. 
    So, we take the absolute value of the substraction and analyse it:
      * if S is less than half of N, then that is the shortest path
      * if S is more than half of N, the path in the oposite direction will be shorter 
    """    
    # abs(operator.sub(a, b)) does not work in the grader, why?
    # operator.abs(operator.sub(a, b)) does not work in the grader, why?
    if (abs(a - b) < N/2):
      return abs(a-b)
    return (N - abs(a-b))
  
  # Build list with all the rotations
  # we need to do it so that we can sum those values.
  rotations = list(map(mod_or_comp, list_ends, list_starts))

  # Sum all the rotations and cast to integer
  my_min_code_entry_time = int(sum(rotations))

  # End
  return my_min_code_entry_time


if __name__ == '__main__':
    
    # Case, valid input
    N = 3
    M = 3
    C = [1, 2, 3]
    expected_return_value = int(2)
    my_min_code_entry_time = getMinCodeEntryTime(N, M, C)
    print("Case: valid input")
    print("For N:", N, "markers in the wheel", 
          ", and sequence M:", M, "C:", C, "the minimum number of seconds",
          "required to select all M of the code's integers in order is", my_min_code_entry_time) 
    if my_min_code_entry_time == expected_return_value:
      print(f"SUCCESS, your function has returned {my_min_code_entry_time} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_min_code_entry_time} and the correct value is {expected_return_value}") 
    print("\n")


    # Case, valid input
    N = 10
    M = 4
    C = [9, 4, 4, 8]
    expected_return_value = 11
    my_min_code_entry_time = getMinCodeEntryTime(N, M, C)
    print("Case: valid input")
    print("For N:", N, "markers in the wheel", 
          ", and sequence M:", M, "C:", C, "the minimum number of seconds",
          "required to select all M of the code's integers in order is", my_min_code_entry_time) 
    if my_min_code_entry_time == expected_return_value:
      print(f"SUCCESS, your function has returned {my_min_code_entry_time} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_min_code_entry_time} and the correct value is {expected_return_value}") 
    print("\n")
