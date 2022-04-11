import time
"""
Read the input from input.txt
Write your answer to output.txt
"""

input_f = open("input.txt", 'r')
lines = input_f.readlines()
input_f.close()
output_f = open("output_dy.txt", 'w')

def f(seq):
    if len(seq) == 0:
        return 0
    elif len(seq) == 1:
        return 1
    else:
        if seq[0] == seq[-1]:
            return f(seq[1:-1]) + 2
        return max(f(seq[1:]), f(seq[:-1]))

start = time.time()
# Iterate each test case in input.txt
for test_case in range(0, 4, 2):
    n = int(lines[test_case])    # n is the length of string
    s = lines[test_case+1]  # s is string
    
    Answer = 0
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    
    Answer = f(s)
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()