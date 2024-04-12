from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  """
  Fires a single shot at a random cell in a grid and returns the probability 
  that the cell hit by your shot contains a battleship.
  
  Constrains
    1 <= R, C <= 100
    0 <= G_i,j <= 1
    The return value must have an absolute or relative error of at most 
    10^(-6) to be considered correct.
  """

  # Verify the arguments. If not valid, inform of the error and terminate. 
  # verify len of C is more than N
  try:
    assert isinstance(R, int), f"The number of rows that you have provided, {R}, is not an integer."
    assert isinstance(C, int), f"The number of columns that you have provided, {C}, is not an integer."
    assert isinstance(G, list), f"The grid you have provided is not a list."
    # loop on G elements and verify each is a list
    # loop within each element and verify each element is an integer
    # loop within each element and verify each element is either 0 or 1"
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  
  # Auxiliary variables
  cells_in_grid = R*C
  ones_in_grid = 0
  for row in G:
    ones_in_row = sum(row)
    ones_in_grid = ones_in_grid + ones_in_row

  # Logic
  expected_probability = ones_in_grid / cells_in_grid
  #print("{:.8f}".format(expected_probability)) but this is a string

  # tidy up
  # Verify that the return value must have an absolute or relative error of at most 10^(-6) to be considered correct
  # Absolute error is the difference between a measured value and a true value. Relative error is the proportion of the absolute error relative to the measured value

  # Finish gracefully
  return expected_probability



if __name__ == '__main__':
    # Case, valid input
    print("Case: valid input")
    R = 2
    C = 3
    G = [
      [0, 0, 1],
      [1, 0, 1]
    ]
    my_probability = getHitProbability(R, C, G)
    print("Probability:", my_probability)
    print("\n")
