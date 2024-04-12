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
  """

  # Verify the arguments. If not valid, inform of the error and terminate. 
  # verify len of C is more than N
  try:
    assert isinstance(1, int), f"Assertion error"
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
  
  # Auxiliary variables
  print("Seats:", N)
  print("Diners:", S)
  table_sections = calculateTableSections(N, K, S)
  #number_of_sections = calculateNumberOfSections(N, S)

  # Logic

  # tidy up
  max_additional_diners_count = 33

  # Finish gracefully
  return max_additional_diners_count

def getNumberOfSections(N: int, S: List[int]) -> int:
  number_of_sections = len(S) + 1
  for diner in S:
    if diner == 1:
      number_of_sections = number_of_sections - 1
    if diner == N:
      number_of_sections = number_of_sections - 1
  return number_of_sections


def calculateTableSections(N: int, K: int, S: List[int]) -> int:
  # Sanitize, sort the list 
  S = sorted(S)

  # Auxiliary variables
  number_of_sections = getNumberOfSections(N, S)

  # Initialize
  table_begin = 1
  table_end = N
  diner_index = 0
  diner_value = S[diner_index]
  section_begin = table_begin
  
  for section_index in range(number_of_sections):
    if diner_index < len(S):
      section_end = diner_value-1
    else:
      section_end = table_end
    table_section = [section_begin, section_end]
    print("table section", section_index, "is", table_section)

    # initialize next interation
    section_begin = int(section_end + 1)
    diner_index = int(diner_index + 1)
    #diner_value = S[diner_index]

    if diner_index > len(S):
      diner_value = table_end
      #break
    print("increased diner index", diner_index)
    #diner_value = S[diner_index]
    #print("incresed diner value", diner_value)



  
  list_of_sections = []
  return list_of_sections


if __name__ == '__main__':
    # Case, valid input
    print("Case: valid input")
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    my_max_additional_diners = getMaxAdditionalDinersCount(N, K, M, S)
    print("Maximum number of additional diners:", my_max_additional_diners)
    print("\n")
