import time
"""
Read the input from input.txt
Write your answer to output.txt
"""

input_f = open("input.txt", 'r')
lines = input_f.readlines()
input_f.close()
output_f = open("output.txt", 'w')

start = time.time()
# Iterate each test case in input.txt
for test_case in range(0, 20, 2):
    n = int(lines[test_case])    # n is the length of string
    s = lines[test_case+1]  # s is string
    
    Answer = 0
    s = s.rstrip('\n')
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    c = []      # c_ij is the length of the longest palindrome in s's i to j sequence

    # Initialize the matrix by c_ij = 1 (if j >= i)
    # Initialize c_ij = 0 (if j < i) dynamic programming calculation
    for i in range(n):
        c.append([])
        for j in range(n):
            if j >= i:
                c[i].append(1)
            else:
                c[i].append(0)

    # Calculate by using dynamic programming
    # Optimal substructure is
    # c_ij = {  1       (if i == j)
    #        {  c_i+1j-1 + 2      (if i != j, s_i == s_j)       <= This formula is also correct for j=i+1 because c_ij (j<i) was initialized to 0 earlier
    #        {  max(c_i+1j, c_ij-1)      (if i != j, s_i != s_j)
    for j in range(1, n):
        for i in range(n - j):
            if s[i] == s[i+j]:
                c[i][i+j] = c[i+1][i+j-1] + 2
            else:
                c[i][i+j] = max(c[i+1][i+j], c[i][i+j-1]) 
    Answer = c[0][n-1]
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()