from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  """
  Approach
    There is an auxiliary list containing the previously eaten K x D_i. 
    Iterate over the dishes in the belt (D_j)
    If the dish is in the auxiliary list, pass. 
    Otherwise, remove the last D_i in the list + add the new D_j in 
      the first place + increase the counter of eaten dishes.
  """
  # Verify the arguments against the constraints.  
  # If not valid, inform of the error and terminate.
  try:
    assert isinstance(N, int), (f"The number of dishes, N, that you have provided, {N}, is not an integer.")
    assert isinstance(D, list), (f"The dishes in the belt, D, that you have provided, {D}, is not a list.")
    assert isinstance(K, int), (f"The number of previous dishes, K, that you have provided, {K}, is not an integer.")
    assert (1 <= N <= 500000), (f"The number of dishes that you have provided, {N}, is out of bounds.")
    assert (1 <= K <= N), (f"The values of previous dishes that you have provided, {K}, is out of bounds.")
    # D_i must be integers
    # D_i must be less than 1,000,000
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  
  # Initialize
  # List with the K previously eaten D_i dishes
  k_previous = ['a' for i in range(K)]

  # Logic, with map
  def d_in_k(d:int) -> bool:
    """Returns False/True if dish d is/not in the K dishes previously eaten
    """
    ### TRY WITH A DICTIONARY INSTEAD OF A LIST FOR THE k_previous
    # https://www.geeksforgeeks.org/python-ordered-set/

    ### CONVERT THE LIST TO A SET BEFORE THE LOOKUP?
    ### THEN MODIFY HTE LIST/NOT?
    if d not in k_previous:
      # That means that we eat the dish, return a True/1
      # Delete the last element of the list
      del k_previous[-1]
      # Append d at the beginning of the list
      k_previous.insert(0, d) 
      return True
    
    # Means that we do NOT eat the dish, return a False/0 
    return False

  # Build list with all the eaten dishes.
  # We need a list (not a map object) so that we can sum those values.
  my_eaten_dishes = list(map(d_in_k, D))

  # Sum all the rotations, cast to integer, and return
  return int(sum(my_eaten_dishes))


if __name__ == '__main__':
    
    # Case, valid input
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 1
    expected_return_value = 5
    my_max_eaten_dish_count = getMaximumEatenDishCount(N, D, K)
    print("Case: valid input")
    print("For N dishes:", N, "belt:", D, 
          ", and with K:", K, "types previously eaten", 
          ", you end up eathing", my_max_eaten_dish_count, "dishes")
    try:
       assert (my_max_eaten_dish_count == expected_return_value), (f"FAILURE, your function has returned {my_max_eaten_dish_count} and was expected to return {expected_return_value}")
    except AssertionError as err:
      print(err, "Please correct and try again.")
      pass
    print((f"SUCCESS, your function has returned {my_max_eaten_dish_count} and was expected to return {expected_return_value}"))
    print("\n")

    # Case, valid input
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 2
    expected_return_value = 4
    my_maximum_eaten_dish_count = getMaximumEatenDishCount(N, D, K)
    print("Case: valid input")
    print("For N dishes:", N, "belt:", D, 
          ", and with K:", K, "types previously eaten", 
          ", you end up eathing", my_maximum_eaten_dish_count, "dishes")
    try:
       assert (my_maximum_eaten_dish_count == expected_return_value), f"FAILURE, your function has returned {my_maximum_eaten_dish_count} and was expected to return {expected_return_value}"
    except AssertionError as err:
      print(err, "Please correct and try again.")
      pass
    print(f"SUCCESS, your function has returned {my_maximum_eaten_dish_count} and was expected to return {expected_return_value}")
    print("\n")

    # Case, valid input
    N = 7
    D = [1, 2, 1, 2, 1, 2, 1]
    K = 2
    expected_return_value = 2
    my_maximum_eaten_dish_count = getMaximumEatenDishCount(N, D, K)
    print("Case: valid input")
    print("For N dishes:", N, "belt:", D, 
          ", and with K:", K, "types previously eaten", 
          ", you end up eathing", my_maximum_eaten_dish_count, "dishes")
    try:
       assert (my_maximum_eaten_dish_count == expected_return_value), f"FAILURE, your function has returned {my_maximum_eaten_dish_count} and was expected to return {expected_return_value}"
    except AssertionError as err:
      print(err, "Please correct and try again.")
      pass
    print(f"SUCCESS, your function has returned {my_maximum_eaten_dish_count} and was expected to return {expected_return_value}")
    print("\n")