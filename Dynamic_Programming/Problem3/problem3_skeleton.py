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
    
    
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/4 + 1)) + " " + str(s) + "\n")
    s = []
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()