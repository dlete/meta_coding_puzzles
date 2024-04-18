def getSum(A: int, B: int, C: int) -> int:
  """Given three integers A, B, and C, determine their sum.
  
  Constraints
    1 =< A, B, C =< 100
  """

  # Verify the arguments. If not valid, inform of the error and terminate. 
  try:
    my_arguments = [A, B, C]
    for argument_index, argument_value in enumerate([A, B, C]):  
      assert isinstance(argument_value, int), f"Argument {argument_index+1}, with value {argument_value}, is not an integer."
      assert (0 < argument_value and argument_value < 101), f"Argument {argument_index+1}, with value {argument_value}, is out of bounds."
  except AssertionError as err:
    print(err, "Please correct and try again.")
    exit()
     
  # Calculate the sum of the input values
  my_sum = A + B + C

  # Finish gracefully
  return my_sum


if __name__ == '__main__':
    A, B, C = 10, 11, 12
    # Error case: input data is not integer
    #A = 10.1
    # Error case: input data is out of bounds
    #A = 111
    #A = 0
    sum_value = getSum(A, B, C)  # to pass a specific logging level
    print("The sum of A, B, and C is:", sum_value)