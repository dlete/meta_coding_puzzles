from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  """
  Approach
    There is an auxiliary dictionary containing the previously eaten K x D_i. 
    Iterate over the dishes in the belt (D_j)
    If the dish is in the auxiliary list, pass. 
    Otherwise, remove the last D_i in the list + add the new D_j in 
      the first place + increase the counter of eaten dishes.
  
  Try
    ### TRY WITH A DICTIONARY INSTEAD OF A LIST FOR THE k_previous
    # https://www.geeksforgeeks.org/python-ordered-set/

    ### CONVERT THE LIST TO A SET BEFORE THE LOOKUP?
    ### THEN MODIFY HTE LIST/NOT?
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
  # Dictionary with the K previously eaten D_i dishes
  k_dict = {"d"+str(k+1):"" for k in range(K)}




  ###################
  # Logic, with map #
  ###################
  # Auxiliary function for the map
  def d_in_k(d):
    """Returns False/True if dish d is/not in the K dishes previously eaten
    """
    # Cast d from int to str because we will use it as a dictionary key
    d = str(d)

    ### Case: d is not in the list of previously eaten dish types
    if d not in k_dict:
      # append to the rightmost side (newest key)
      k_dict[d] = ""

      # remove the leftmost key (oldest key)
      # Find the which is the first key by converting the keys to a list, then
      # getting the first element of the list. Finally deleting the key.
      my_keys = list(k_dict.keys())
      k0 = my_keys[0]
      del k_dict[k0]

      # The dish d is NOT in the list of previously eaten, we will YES eat it
      return True
    
    ### Case: d is in the list of previously eaten dish types
    # The dish d is YES in the list of previously eaten, we will NOT eat it
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
    print("For N:", N, "dishes, belt:", D, 
          ", and K:", K, "types previously eaten", 
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
    print("For N:", N, "dishes, belt:", D, 
          ", and K:", K, "types previously eaten", 
          ", you end up eathing", my_max_eaten_dish_count, "dishes")
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
    print("For N:", N, "dishes, belt:", D, 
          ", and K:", K, "types previously eaten", 
          ", you end up eathing", my_max_eaten_dish_count, "dishes")
    try:
       assert (my_maximum_eaten_dish_count == expected_return_value), f"FAILURE, your function has returned {my_maximum_eaten_dish_count} and was expected to return {expected_return_value}"
    except AssertionError as err:
      print(err, "Please correct and try again.")
      pass
    print(f"SUCCESS, your function has returned {my_maximum_eaten_dish_count} and was expected to return {expected_return_value}")
    print("\n")