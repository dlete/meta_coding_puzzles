def getWrongAnswers(N: int, C: str) -> str:
  """
  Returns a string with N characters, the ith of which is the answer you 
  should give for question i in order to get it wrong (either "A" or "B").
  
  Constrains
    1 =< N =< 100
    C_i ∈ {"A", "B"}
  """

  # Auxiliary variables
  answer_options = ["A", "B"]
  length_of_c = len(C)
  c_as_a_list = list(C)

  # Verify the arguments. If not valid, inform of the error and terminate. 
  # verify len of C is more than N
  try:
    assert isinstance(N, int), f"The number of questions that you have provided, {N}, is not an integer."
    assert (0 < N < 101), f"The number of questions that you have provided, {N}, is out of bounds."
    assert (N <= length_of_c), f"The number of questions ({N}), is more than the number of characters in C ({length_of_c})."
    for character_index, character_value in enumerate(C):
      assert (character_value in answer_options), f"The character {character_value}, in position {character_index+1}, of the argument '{C}' is not valid."
  except AssertionError as err:
    print(err, "Please correct and try again.")
    return None
     
  # Logic
  # Initialize the return as an empty list
  wrong_answers = []

  for question_index in range(N):
    #print(question_index)
    #print(c_as_a_list[question_index])

    character_i = c_as_a_list[question_index]
    if character_i == "A":
      wrong_answers.append("B")
    if character_i == "B":
      wrong_answers.append("A")
  # tidy up
  wrong_answers_string = "".join(wrong_answers)

  # Finish gracefully
  return wrong_answers_string



if __name__ == '__main__':
    # Case, valid input
    print("Case: valid input")
    N = 3
    C = "ABBA"
    wrong_answers = getWrongAnswers(N, C)
    print("Valid answers:", C)
    print("Number of questions:", str(N))
    print("Wrong answers:", wrong_answers)
    print("\n")

    # Case, invalid. The "N" given is not an integer
    print("Case: invalid input. The 'N' given is not an integer")
    N = 7.3
    C = "ABBA"
    wrong_answers = getWrongAnswers(N, C)
    print("Valid answers:", C)
    print("Number of questions:", str(N))
    print("Wrong answers:", wrong_answers)
    print("\n")

    # Case, invalid. The number of questions that you have provided, {N}, is out of bounds.
    print("Case: invalid input. The number of questions that you have provided, {N}, is out of bounds.")
    N = 111
    C = "ABBA"
    wrong_answers = getWrongAnswers(N, C)
    print("Valid answers:", C)
    print("Number of questions:", str(N))
    print("Wrong answers:", wrong_answers)
    print("\n")

    # Case, invalid. Number of questions higher than characters in C
    print("Case: invalid input. Number of questions higher than characters in C")
    N = 7
    C = "ABBA"
    wrong_answers = getWrongAnswers(N, C)
    print("Valid answers:", C)
    print("Number of questions:", str(N))
    print("Wrong answers:", wrong_answers)
    print("\n")

    # Case, invalid. Invalid characters in the string C
    print("Case: invalid input. Invalid characters in the string 'C'")
    N = 3
    C = "AXXA"
    wrong_answers = getWrongAnswers(N, C)
    print("Valid answers:", C)
    print("Number of questions:", str(N))
    print("Wrong answers:", wrong_answers)
    print("\n")

        # Case, invalid. Invalid characters in the string C
    print("Case: invalid input. Invalid characters in the string 'C'")
    N = 3
    C = "ABXA"
    wrong_answers = getWrongAnswers(N, C)
    print("Valid answers:", C)
    print("Number of questions:", str(N))
    print("Wrong answers:", wrong_answers)
    print("\n")
