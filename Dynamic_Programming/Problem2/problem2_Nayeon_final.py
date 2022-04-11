import time
import numpy as np
"""
Read the input from input.txt
Write your answer to output.txt
"""

input_f = open("input.txt", 'r')
lines = input_f.readlines()
input_f.close()
output_f = open("output_Nayeon_final.txt", 'w')

start = time.time()
# Iterate each test case in input.txt
for test_case in range(0, 20, 2):
    n = int(lines[test_case])    # n is the length of string
    s = lines[test_case+1]  # s is string
    s = s.rstrip("\n")
    # Answer = 0
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    
    # make matrix with list
    c = []

    for i in range(n):
        c.append([])
        for j in range(n):
            c[i].append(0)
    
    # initialize matrix c
    # ci_i & ci_i+1
    for i in range(n-1):
        # ci_i
        c[i][i] = 1
        
        if i > n-2:
            break
        # ci_i+1
        if s[i] == s[i+1]:
            c[i][i+1] = 2
        else:
            c[i][i+1] = 1
            
        
    # optimal substructure
    # ci_j = {ci+1_j-1 + 2                  (if i == j)}
    #        {max(ci_j-1, ci+1_j)           (if i != j)}

    # size(k+1) : 3 ~ n
    # k : 2 ~ n-1
    # i : 0 ~ n-k
    for k in range(2, n):
        for i in range(n-k):
            j = i + k
            #c_max = max([c[i+1][j], c[i][j-1]])

            if s[i] == s[j] :
                c[i][j] = c[i+1][j-1] + 2

            else:
                c[i][j] = max([c[i+1][j], c[i][j-1]])

    Answer = c[0][n-1]
    
    
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()