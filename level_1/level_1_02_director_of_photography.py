# Imports, Python native
from typing import List

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  """
  Questions
    Why do we need N? We can extract N anyway from the argument C anyway.

  Approach
    Find out number of 'photographs'
      Scan for string P*A*B from right to left
      Scan for string B*A*P from left to right
    Determine how many of the 'photographs' are 'artistic'
  """
  # Sanitize
  # remove leading/trailing spaces from string
  C = C.strip()
   
  # # Verify the arguments against the constraints. 
  # If not valid, inform of the error and terminate.
  try:
     assert isinstance(N, int), f"The number of characters, N, that you have provided, {N}, is not an integer."
     assert isinstance(C, str), f"The number of photo set, C, that you have provided, {C}, is not an integer."
     assert isinstance(X, int), f"The value of X that you have provided, {X}, is not an integer."
     assert isinstance(Y, int), f"The value of X that you have provided, {Y}, is not an integer."
     assert (1 <= N <= 200), f"The number of cells that you have provided, {N}, is out of bounds."
     assert (1 <= X <= Y <= N), f"The values of X and Y that you have provided, {X} and {Y}, are out of bounds."
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  

  # Auxiliary functions
  def getPhotographs(C: str, L: str) -> List[str]:
    """Returns a list of the occurrences of a pattern within a string

    Arguments
      C is the photograph set
      L is the layout to look for
    """

    # Build dictionary with the indexes of the P, A, and B in the photo set 
    my_indices = {}
    for l in L:
       my_indices[l] = [i for i, c in enumerate(C) if c == l]
    #print("Indices: Each letter of the layout appears in these indexes", my_indices)

    # Initialize the list of photographs that we will return
    photographs = []

    # Look for the pattern L in the string C
    # (iterate letters of PAB if going forward, or BAB if backwards)
    for i, c in enumerate(L):
      #print("working on character", c)
      #print("Character", c, "has indexes", my_indices[c])

      # Initialize for each character
      photographs_iteration = []

      # For the first character in the layout L, all the indixes are valid
      #if c == 'P':  # improve to L[0]
      if c == L[0]:
        for c_index in my_indices[c]:
          photographs_iteration.append(str(c_index))
        #print("Initial pattern looks like", photographs_iteration)

      # For all the other characters in L that are not the first
      #if c != 'P':  # improve to L[0]
      if c != L[0]:
        #print("character", c, "has indexes", my_indices[c])
        for c_index in my_indices[c]:
          #print("focusing on index", c_index)
          for photograph in photographs:
            #print("analysing pattern", photograph)
            if c_index > int(photograph[-1]):
              #print(str(c_index), "is bigger than the last character of the photograph", photograph[-1])
              photograph = photograph + (str(c_index))
              photographs_iteration.append(photograph)
            else:
              pass
              #print(str(c_index), "is lower or equal than the last character of the photograph", photograph[-1])
            #print("after analysing index", c_index, "the pattern now looks like", photograph)

      photographs = photographs_iteration
      #print("after iterating character", c, "photographs_iteration look like", photographs_iteration, "\n")

    # Remove patterns that are shortern than the layout
    #print("photographs look like", photographs)
    for photo_index, photo_value in enumerate(photographs):
      #print("photo index", photo_index, "photo value", photo_value)
      if len(photo_value) == len(L):
        pass
      else:
        photographs.pop(photo_index)

    #print("photographs looks like", photographs)
    return photographs
  
  
  def isPhotographArtistic(abc: str, ab: int, bc: int) -> bool:
    """Returns whether a photograph is artistic or not

    Arguments
      abc, layout
      ab, distance that must be between the first and second character
      bc, distance that must be between the second and third character
    """
    dist_a_b = abs(int(abc[1]) - int(abc[0]))
    dist_b_c = abs(int(abc[2]) - int(abc[1]))
    #print("Distance from first to second is", dist_a_b, "and the constraint is:", ab, "<=", dist_a_b, "<=", bc)
    #print("Distance from second to third is", dist_b_c, "and the constraint is", ab, "<=", dist_b_c, "<=", bc)
    if (ab <= dist_a_b <= bc) and (ab <= dist_b_c <= bc):
      photographIsArtistic = True
      #print("Photograph", abc, "is YES artistic")
    else:
      photographIsArtistic = False
      #print("Photograph", abc, "is NOT artistic")
    return photographIsArtistic
  

  # Logic
  # Find all the photographs
  characters_forwards = C
  pattern_forwards = 'PAB'
  #print("Photo set forwards", characters_forwards)
  #print("Layout forwards", pattern_forwards)
  photographs_forwards = getPhotographs(characters_forwards, pattern_forwards)
  #print("There are these photographs forwards", photographs_forwards, "\n")

  #characters_backwards = ''.join(list(reversed(C)))
  characters_backwards = C
  pattern_backwards = 'BAP'
  #print("Photo set backwards", characters_backwards)
  #print("Layout backwards", pattern_backwards)
  photographs_backwards = getPhotographs(characters_backwards, pattern_backwards)
  #print("There are these photographs backwards", photographs_backwards, "\n")


  # Determine how many of the photographs are artistic
  photographs_artistic = []

  for photograph in photographs_forwards:
    #print("Is forward photograph", photograph, "artistic?")
    artistic = isPhotographArtistic(photograph, X, Y)
    if artistic == True:
      photographs_artistic.append(photograph)
  for photograph in photographs_backwards:
    #print("Is backward photograph", photograph, "artistic?")
    artistic = isPhotographArtistic(photograph, X, Y)
    if artistic == True:
      photographs_artistic.append(photograph)
  #print("Overall, forward and backward, have found these artistic photographs", photographs_artistic)

  # Remove duplicates
  photographs_artistic = set(photographs_artistic)
  #print("Removing duplicates, have found these artistic photographs", photographs_artistic)

  my_artistic_photograph_count = int(len(photographs_artistic))
  #print("Number of artistic photographs", my_artistic_photograph_count)
  
  # End
  return my_artistic_photograph_count


if __name__ == '__main__':
    
    # Case, valid input
    N = 10
    C = 'APABA'
    X = 1
    Y = 2
    my_artistic_photograph_count = getArtisticPhotographCount(N, C, X, Y)
    print("Case: valid input")
    print("For N", N, "and string:", C, 
          "with distances X and Y", X, "and", Y, 
          ", there are", my_artistic_photograph_count, "artistic pictures")
    print("\n")
    

    # Case, valid input
    N = 5
    C = 'APABA'
    X = 2
    Y = 3
    my_artistic_photograph_count = getArtisticPhotographCount(N, C, X, Y)
    print("Case: valid input")
    print("For N", N, "and string:", C, 
          "with distances X and Y", X, "and", Y, 
          ", there are", my_artistic_photograph_count, "artistic pictures")
    print("\n")

    
    # Case, valid input
    N = 8
    C = '.PBAAP.B'
    X = 1
    Y = 3
    my_artistic_photograph_count = getArtisticPhotographCount(N, C, X, Y)
    print("Case: valid input")
    print("For N", N, "and string:", C, 
          "with distances X and Y", X, "and", Y, 
          ", there are", my_artistic_photograph_count, "artistic pictures")
    print("\n")
    
