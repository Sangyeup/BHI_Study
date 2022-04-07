import time
"""
Read the input from input.txt
Write your answer to output.txt
"""

def make_matrix(x):
    if x == 'a':
        return [1, 0, 0]
    elif x == 'b':
        return [0, 1, 0]
    elif x == 'c':
        return [0, 0, 1]

# x is the list of c_ik, y is the list of c_k+1j
def table_matrix(x, y):          
    a = x[2]*y[0] + x[0]*y[2] + x[1]*y[2]
    b = x[0]*y[0] + x[0]*y[1] + x[1]*y[1]
    c = x[1]*y[0] + x[2]*y[1] + x[2]*y[2]
    return [a, b, c]

input_f = open("input.txt", 'r')
lines = input_f.readlines()
input_f.close()
output_f = open("output.txt", 'w')

start = time.time()
# Iterate each test case in input.txt
for test_case in range(0, 20, 2):
    n = int(lines[test_case])    # n is the length of string
    s = lines[test_case+1]  # s is string
    s = s.rstrip('\n')
    Answer = [0, 0, 0]
    # Answer[0] is the number of a
    # Answer[1] is the number of b
    # Answer[2] is the number of c
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    c = []      # c_ij is [num_a, num_b, num_c] form list which stores each number of s's i to j sequence 
    
    # Initialize the matrix 
    for i in range(len(s)):
        c.append([])
        for j in range(len(s)):
            c[i].append([0, 0, 0])
    
    # Get c_ii by using make_matrix function
    for i in range(len(s)):
        c[i][i] = make_matrix(s[i])     
    
    # Get c_ii+1 
    for i in range(len(s)-1):
        c[i][i+1] = table_matrix(c[i][i], c[i+1][i+1])

    # Calculate by using dynamic programming
    # Optimal substructure is
    # c_ij = {  make_matrix(c_ij)       (if i == j)
    #        {  Σ table_matrix(c_ik, c_k+1j)     (if i != j)
    for j in range(2, len(s)):
        for i in range(len(s) - j):
            c[i][i+j] = [0, 0, 0]
            for k in range(j):
                temp = table_matrix(c[i][i+k], c[i+k+1][i+j])
                c[i][i+j][0] += temp[0]
                c[i][i+j][1] += temp[1]
                c[i][i+j][2] += temp[2]

    # Store the answer
    Answer = c[0][len(s)-1]

    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer[0]) + " " + str(Answer[1]) + " " + str(Answer[2]) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()

