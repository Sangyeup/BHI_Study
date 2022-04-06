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
    
    Answer = [0, 0, 0]
    # Answer[0] is the number of a
    # Answer[1] is the number of b
    # Answer[2] is the number of c
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    
    
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer[0]) + " " + str(Answer[1]) + " " + str(Answer[2]) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()