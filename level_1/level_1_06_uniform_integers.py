
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    """
    1 000 000 000 000
    100 000 000 000

    A = 75
    B = 300
    B - A = 275

    A to next 10**i
    100 to 300

    A = 75
    B = 327
    75 to 99 (100-1)
    100 to 300
    300 to 327

     75 - 100
     100 - 


     75, 13000
     75 to 99
     100 to 1 00 00   (100-999 1000-9999 10000)
     100 to 1 00 0    (100-999 1000)
     3000

    76
    389
    """
    BA = 275
    """
    print("With FOR")
    tens = [10**i for i in range(1, 12, 1)]
    for t in tens:
       print(BA, "modulo", t, "is:", BA % t)   
    
    print("with WHILE")
    i = 1
    t = 10
    while not ((BA % t) >= BA):
       print(BA, "modulo", t, "is:", BA % t)
       print("have to analyse", BA%t)
       BA = BA - (BA % t)
       
       i = i + 1
       t = t**i
    """

    """
    #print(len(str(BA)))
    for t in range(1, len(str(BA))+1, 1):
        modulo = 10**t
        print("modulo", modulo)
        print(BA, "modulo", modulo, "is:", BA % modulo)
        print("have to analyse", BA%modulo)
        BA = BA - (BA % modulo)
    """
    # CASE: A == B
    #if A == B:
    #   return 1
    
    power_of_A = len(str(A))
    power_of_B = len(str(B))
    
    print("the powers of", A, "and", B, "are", power_of_A, "and", power_of_B)

    block_i_start = A
    block_i_end = pow(10, power_of_A) - 1
    print("block_i goes from", block_i_start, "to", block_i_end)
    #int((99-75)/11)+1
    #int((end-start)/ "1" repeated x times power of A)

    big_endian_b = str(B)[0]
    #print(big_endian_b)
    block_ii_start = pow(10, power_of_A)
    block_ii_end = int(big_endian_b) * (pow(10, power_of_B-1))
    print("block_ii goes from", block_ii_start, "to", block_ii_end)
    # 9 times the number of powers in between
    # if it is 1300?
    # 100 to 1 00 00   (100-999 1000-9999 10000)
    # 100 to 1 00 0    (100-999 1000)
    # start and end are in different powers
    # if they are in the same power, then there is no block ii?

    block_iii_start = int(big_endian_b) * (pow(10, power_of_B-1))
    block_iii_end = B
    print("block_iii goes from", block_iii_start, "to", block_iii_end)
    # same than block_i?
    # #int((99-75)/11)+1
    #int((end-start)/ "1" repeated x times power of A)

    return 0


if __name__ == '__main__':
    case = "Sample test case #1"
    A = 75
    B = 327
    expected_return_value = 5
    my_calculation = getUniformIntegerCountInInterval(A, B)
    print(case)
    print("For the numbers A:", A, "and B:", B, "the number of uniform integers is", my_calculation)
    if my_calculation == expected_return_value:
      print(f"SUCCESS, your function has returned {my_calculation} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_calculation} and the correct value is {expected_return_value}") 
    print("\n")

    case = "Sample test case #2"
    A = 75
    B = 300
    expected_return_value = 5
    my_calculation = getUniformIntegerCountInInterval(A, B)
    print(case)
    print("For the numbers A:", A, "and B:", B, "the number of uniform integers is", my_calculation)
    if my_calculation == expected_return_value:
      print(f"SUCCESS, your function has returned {my_calculation} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_calculation} and the correct value is {expected_return_value}") 
    print("\n")

    case = "Sample test case #3"
    A = 999999999999
    B = 999999999999
    expected_return_value = 1
    my_calculation = getUniformIntegerCountInInterval(A, B)
    print(case)
    print("For the numbers A:", A, "and B:", B, "the number of uniform integers is", my_calculation)
    if my_calculation == expected_return_value:
      print(f"SUCCESS, your function has returned {my_calculation} and was expected to return {expected_return_value}")
    else:
      print(f"FAILURE, your function has returned {my_calculation} and the correct value is {expected_return_value}") 
    print("\n")