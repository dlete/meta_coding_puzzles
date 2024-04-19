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
  # Write your code here
  return 0