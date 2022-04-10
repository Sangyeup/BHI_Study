import time
"""
Read the input from input.txt
Write your answer to output.txt
"""

input_f = open("input.txt", 'r')
lines = input_f.readlines()
input_f.close()
output_f = open("output_Nayeon.txt", 'w')

start = time.time()
# Iterate each test case in input.txt
for test_case in range(0, 20, 2):
    n = int(lines[test_case])    # n is the length of string
    s = lines[test_case+1]  # s is string
    
    Answer = 0
    
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
    # ci_i
    # ci_i+1
    # ci_i+2
    # ci_i+3
    for i in range(n):
        # ci_u
        c[i][i] = 1

        if i == n-1:
            break
        
        # ci_i+1
        if s[i] == s[i+1]:
            c[i][i+1] = 2
            
            if 0<i<n-2 :
                # ci_i+3
                if s[i-1] == s[i+2]:
                    c[i-1][i+2] = 4

        if i > n-3:
            continue
            
        # ci_i+2
        elif s[i] == s[i+2]:
            c[i][i+2] = 3

       # if i > n-4:
        #    continue
        
        # ci_i+3
        #elif (s[i] == s[i+3]) & (s[i+1] == s[i+2]):
         #   c[i][i+3] = 4



    # optimal substructure
    # ci_j = {ci+1_j-1 + 2                            (if i == j)}
    #        {max(ci+1_j-1, ci_j-1, ci+1_j)           (if i != j)}

    # size k : 4 ~ n-1
    for k in range(4, n):
        for i in range(n-k):
            j = i + k
            c_max = max([c[i][j-1], c[i+1][j], c[i+1][j-1]])

            if (s[i] == s[j]) & (c[i+1][j-1] > c[i+2][j-2]):
                #if c[i+1][j-1] > c[i+2][j-2]:
                c[i][j] = c[i+1][j-1] + 2
                #else: 
                 #   c[i][j] = c_max
            else:
                c[i][j] = c_max

    Answer = c[0][n-1]
    
    
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()