from typing import List
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
  1 2 3 4 5 6 7 8 9 10
    M       M
  Break in table sections: begin to first M, first M to second M, second M to xth M, etc., last M to table end
  Analyze each table section on its own
  Count the results of each table section

  Example
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

  # Verify the arguments. If not valid, inform of the error and terminate. 
  # verify len of C is more than N
  try:
    assert isinstance(1, int), f"Assertion error"
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  
  # Auxiliary variables
  table_sections = getTableSections(N, K, S)

  # Logic
  # Initialize
  """
  aditional_diners_table = 0
  for table_section in table_sections:
    additional_diners_section = getAdditionalDiners(K, table_section, 1)
    aditional_diners_table = aditional_diners_table + additional_diners_section 

  # tidy up
  max_additional_diners_count = aditional_diners_table
  #print("max_additional_diners_count", max_additional_diners_count)

  # Finish gracefully
  return max_additional_diners_count
  """
  return table_sections


def getNumberOfSections(N: int, S: List[int]) -> int:
  number_of_sections = len(S) + 1
  for diner in S:
    if diner == 1:
      number_of_sections = number_of_sections - 1
    if diner == N:
      number_of_sections = number_of_sections - 1
  return number_of_sections


def getTableSections(N: int, K: int, S: List[int]) -> List[List[int]]:
  # Sanitize, sort the list 
  S = sorted(S)

  # Auxiliary variables
  number_of_sections = getNumberOfSections(N, S)

  # Initialize
  list_of_sections = []
  additional_diners_table = 0

  # Logic
  # Treat the first and last section as particular cases. 
  # Build a list for each section. 
  # Append the section lists to the overall list of sections
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
    list_of_sections.append(section_list)
    print("section with index", section_index, 
          "has seats list", section_list, 
          "and", reserved_ends, "reserved ends \n")
    additional_diners_section = getAdditionalDiners(K, section_list, reserved_ends)
    additional_diners_table = additional_diners_table + additional_diners_section
    #print("additional_diners_section", additional_diners_section)
  
  # end
  return additional_diners_table


def getAdditionalDiners(K: int, S: List[int], R: int) -> int:
  """
  R is the number of reserved seats, already allocated. 
  Constraint: 1<= R <= 2
  """
  # Initialize and auxiliary variables
  additional_diners = 0
  seats = (S[-1]-S[0]) + 1
  valid_seats = seats - R

  if valid_seats <= K:
    additional_diners = 0
  else:
    additional_diners = int(valid_seats/(K+1))

  print("list", S, "has", seats, "seats. And", valid_seats, "are valid")
  #print("For a K:", K, "that allows this number of diners:", additional_diners)

  #end
  return additional_diners

if __name__ == '__main__':
    # Case, valid input
    print("Case: valid input")
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Seats:", N)
    print("Diners:", S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")
