from typing import List, Tuple
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  """
  About
    A cafeteria table consists of a row of N seats, numbered from 1 to N from 
    left to right. Social distancing guidelines require that every diner be 
    seated such that K seats to their left and K seats to their right (or all 
    the remaining seats to that side if there are fewer than K) remain empty.
    
    There are currently M diners seated at the table, the ith of whom is in 
    seat S_i. No two diners are sitting in the same seat, and the social 
    distancing guidelines are satisfied.

    Determine the maximum number of additional diners who can potentially sit 
    at the table without social distancing guidelines being violated for any 
    new or existing diners, assuming that the existing diners cannot move and 
    that the additional diners will cooperate to maximize how many of them can 
    sit down.
  
  Constraints
    1 =< N =< 10^(15)
    1 =< K =< N
    1 =< M =< 500,000
    M =< N
    1 =< S_i =< N

  Approach
    Break the table in sections. 
    Each section goes from reserved seat (or table begin) to reserved seat (or table end).
    Analyze each section on its own.
    Calculate the number of additional seats per section. 
    Add the additional seats of all the sections, and return that value.

  Example #1
    Baseline:
      1 2 3 4 5 6 7 8 9 10
        M       M
    
    Sections
      1 2
      2 3 4 5 6
      6 7 8 9 10
    
    Diners per section
      1 2
      0 M        -> 0 diners

      2 3 4 5 6
      M   d   M  -> 1 diner

      6 7 8 9 10
      M   d   d  -> 2 diners

      End situation
      1 2 3 4 5 6 7 8 9 10
        M   d   M   d   d



  """

  # Sanitize, sort the list 
  S = sorted(S)

  # Verify the arguments. If not valid, inform of the error and terminate.
  try:
    assert (1 <= N <= pow(10, 15)), f"The number of seats (N) that you have provided, {N}, is out of bounds."
    assert (1 <= K <= N), f"The number of free seats between diners (K) that you have provided, {K}, is out of bounds."
    assert (1 <= M <= 500000), f"The number of initial diners (M) that you have provided, {M}, is out of bounds."
    assert (M <= N), f"The number of initial diners (M: {M}) cannot be bigger than the number of seats (N: {N})."
    for S_i in S:
      assert (1 <= S_i <= N), f"The seat of current diners (S_i: {S_i}) cannot be bigger than the number of seats (N: {N})."
      assert isinstance(S_i, int), f"The occupied seat number, S_i, that you have provided, {S_i}, is not an integer."
    assert isinstance(N, int), f"The number of seats, N, that you have provided, {N}, is not an integer."
    assert isinstance(K, int), f"The number of free seats between diners, K, that you have provided, {K}, is not an integer."
    assert isinstance(M, int), f"The number of already seated diners, M, that you have provided, {M}, is not an integer."
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  
  # Auxiliary functions
  def getNumberOfSections(N: int, S: List[int]) -> int:
    """Returns the number of sections into which a table can be broken into.
    """
    number_of_sections = len(S) + 1
    for diner in S:
      if diner == 1:
        number_of_sections = number_of_sections - 1
      if diner == N:
        number_of_sections = number_of_sections - 1
    #print("getNumberOfSections. Table N with", N, "seats, with seats", S, "already occupied, can be broken into", number_of_sections, "sections")

    # Finish
    return number_of_sections
  
  def getTableSections(N: int, K: int, S: List[int]) -> List[Tuple[List[int], int]]:
    """Returns a list of tuples with list of seats and number of reserved seats per section

      Approach
        Treat the first and last section as particular cases. 
        Build a tuple for each section. 
        The tuple contains: list of seats, and number of reserved seats
        Append the section tuple to the list of sections 
        Return the list of sections
    """
    # Verify
    # That S is sorted
    # Constraints?

    # Sanitize, sort the list 
    #S = sorted(S)

    # Auxiliary variables
    number_of_sections = getNumberOfSections(N, S)

    # Initialize
    list_of_sections = []

    # Logic
    for section_index in range(number_of_sections):
      if section_index == 0:
        #print("first section, with index", section_index)
        section_begin = 1
        section_end = S[0]
        reserved_ends = 1
      elif section_index == (number_of_sections-1):
        #print("last section, with index", section_index)
        section_begin = S[-1]
        section_end = N
        reserved_ends = 1
      else:
        #print("middle section, with index", section_index)
        section_begin = S[section_index-1]
        section_end = S[section_index]
        reserved_ends = 2
      
      section_list = [section_begin, section_end]
      section_tuple = (section_list, reserved_ends)
      list_of_sections.append(section_tuple)
      #print("getTableSections: section with index", section_index, 
      #      "has seats", section_list, 
      #      "and", reserved_ends, "reserved ends.")
      
    # end
    return list_of_sections
  

  def getAdditionalDiners(K: int, S: List[int], R: int) -> int:
    """
    R is the number of reserved seats, already allocated. 
    Constraint: 1<= R <= 2
    """
    # Initialize and auxiliary variables
    additional_diners = 0
    seats = (S[-1]-S[0]) + 1
    if R == 2:
      valid_seats = seats - R - K
    else:
      valid_seats = seats - R

    if valid_seats <= K:
      additional_diners = 0
    else:
      additional_diners = int(valid_seats/(K+1))

    #print("getAdditionalDiners: list", S, "has", seats, "seats,", valid_seats, "are valid. It can fit", additional_diners, "additional diners")

    #end
    return additional_diners

  # Auxiliary variables
  # Find out the sections into which this table can be broken into
  table_sections = getTableSections(N, K, S)

  # Initialize
  # Value that the function will return
  additional_diners_table = 0

  # Logic
  # Go through each section that we have broken the table into
  # Find out how many additional diners can each section accomodate
  # Add the number of additional diners for each section
  # Return the aggregated value of the additional diners in all the sections
  for table_section in table_sections:
    # table_section is a tuple. 
    # The first element is a list with the first and last seats of the section
    # The second element is the number of seats already in use
    section_seats_list = table_section[0]
    section_seats_reserved = table_section[1]
    additional_diners_section = getAdditionalDiners(K, section_seats_list, section_seats_reserved)
    additional_diners_table = additional_diners_table + additional_diners_section

  # end
  return additional_diners_table


if __name__ == '__main__':
    # Case, valid input
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")

    # Case, valid input
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")

    # Case, ERROR. N out of bounds
    N = pow(10, 33)
    K = 2
    M = 3
    S = [11, 6, 14]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")

        # Case, ERROR. K out of bounds
    N = 15
    K = 33
    M = 3
    S = [11, 6, 14]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")

    # Case, ERROR. M out of bounds
    N = 15
    K = 2
    M = 777777
    S = [11, 6, 14]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")

    # Case, ERROR. Constraint M <= N is breached 
    N = 15
    K = 2
    M = 77
    S = [11, 6, 14]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")

    # Case, ERROR. Constraint 1 <= S_i <= N is breached
    N = 15
    K = 2
    M = 3
    S = [11, 66, 14]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Case: valid input")
    print("Total seats:", N, "/// seats between diners:", K, "/// seats already occupied:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")