import time
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

# p pattern 총 6가지
# p : (+1, 0, -1), (+1, -1, 0), (0, +1, -1), (0, -1, +1), (-1, +1, 0), (-1, 0, +1)

p = [[+1, 0, -1], [+1, -1, 0], [0, +1, -1], [0, -1, +1], [-1, +1, 0], [-1, 0, +1]]

# not compatible pair of p
# 3 가지씩 존재
# EX) (+1, 0, -1) : (+1, -1, 0), (-1, 0, +1), (0, +1, -1)
# 따라서 가능한 것 한 패턴마다 2가지 뿐
# compatible pairs 미리 계산해두자
# EX) (+1, 0, -1) -> (0, -1, +1), (-1, +1, 0) 두가지

p_comp = {0: [3, 4], 1: [2, 5], 2: [1,5], 3: [0, 4], 4: [0, 3], 5:[1, 2]}


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
   
    # w_i_p
    # i th column's score with pattern p
    # shape n*len(p)
    w = []
    for i in range(n): 
        # for i col of matrix
        w.append([])
        for j in range(len(p)):
            w[i].append(int(s[0][i])*p[j][0] + int(s[1][i])*p[j][1] + int(s[2][i])*p[j][2])
    
    # make matrix with list
    c = []

    for i in range(n):
        c.append([])
        for j in range(len(p)):
            c[i].append(0)    
            
    # Optimal substructure
    # max score until i col of s, when i col with pattern p 
    # c_i_p = {w_i_p                                                 (if i=0, first col)}
    #       = {w_i_p + max(until c_i-1_q, q compatible to p)         (if i>0, not first)}
    
    # initialization
    # i = 0, for first col
    # c_0_p = w_0_p
    c[0] = w[0]

    # i>0
    for i in range(1,n):
        for j in range(len(p)):
            # compatible q -> 2 cases
            # q from p_comp
            candidates = []
            for q in p_comp[j]:
                candidates.append(c[i-1][q])

            c[i][j] = max(candidates) + w[i][j]
    
    Answer = max(c[n-1])
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/4 + 1)) + " " + str(Answer) + "\n")
    
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()