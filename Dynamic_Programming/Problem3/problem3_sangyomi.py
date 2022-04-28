import time

def pattern(a, b, c):
    result = []
    a = int(a)
    b = int(b)
    c = int(c)
    # OXS OSX SOX SXO XOS XSO order
    result.append(a-b)
    result.append(a-c)
    result.append(b-c)
    result.append(c-b)
    result.append(b-a)
    result.append(c-a)
    return result

def return_compatible(n):
    if n == 0:
        return [2, 5]
    elif n == 1:
        return [3, 4]
    elif n == 2:
        return [0, 5]
    elif n == 3:
        return [1, 4]
    elif n == 4:
        return [1, 3]
    elif n == 5:
        return [0, 2]
    else:
        print("Error")
        return

"""
Read the input from input.txt
Write your answer to output.txt
"""

input_f = open("input.txt", 'r')
lines = input_f.readlines()
input_f.close()
output_f = open("output.txt", 'w')
max_num = 1000000

start = time.time()
# Iterate each test case in input.txt
for test_case in range(0, 40, 4):
    n = int(lines[test_case])    # n is the length of string
    s = []
    s.append(lines[test_case+1].rstrip('\n').split(' '))  # s[0] is the first row of table
    s.append(lines[test_case+2].rstrip('\n').split(' '))  # s[1] is the second row of table
    s.append(lines[test_case+3].rstrip('\n').split(' '))  # s[2] is the second row of table
    Answer = 0
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    c = []      # c_ij is max sum of 0~i score whne ith's pattern is j

    # Initialize the matrix by c_ij = 0
    for i in range(n):
        c.append([])
        for j in range(6):
            c[i].append(0)

    # Calculate by using dynamic programming
    # Optimal substructure is
    # c_ij = max(c_i-1s + pattern(s_ij)) s and j are compatible
    # compatible pattern 
    # OXS OSX SOX SXO XOS XSO order
    # => (0, 2), (0, 5), (1, 3), (1, 4), (2, 0), (2, 5), (3, 1), (3, 4), (4, 1), (4, 3), (5, 0), (5, 2)
    
    c[0] = pattern(s[0][0], s[1][0], s[2][0])
    for i in range(1, n):
        for j in range(6):
            compatible = return_compatible(j)
            c[i][j] = max(c[i-1][compatible[0]], c[i-1][compatible[1]]) + pattern(s[0][i], s[1][i], s[2][i])[j]
    Answer = max(c[n-1])
    
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/4 + 1)) + " " + str(Answer) + "\n")
    s = []
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()