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

mul_table = [[1, 1, 0], [2, 1, 0], [0, 2, 2]]
st2num_dict = {'a': '0', 'b': '1', 'c': '2' }

def st2num(st):
    num_string = []
    for i in range(len(st)):
        num_string.append(st2num_dict[st[i]])
    return num_string

def dp(num_string, s, e, num):

    if s == e:
        if int(num_string[s]) == num:
            dp_table[num][s][e] = 1
        else:
            dp_table[num][s][e] = 0
    if (e - s) == 1:
        mul_num = mul_table[int(num_string[s])][int(num_string[e])]
        if mul_num == num:
            dp_table[num][s][e] = 1
        else:
            dp_table[num][s][e] = 0



    for i in range(s, e + 1):
        if num == 0:
            dp_table[num][s][e] += dp(num_string, s, i, 2)* dp(num_string, i+1, e, 0)
            dp_table[num][s][e] += dp(num_string, s, i, 0)* dp(num_string, i+1, e, 2)
            dp_table[num][s][e] += dp(num_string, s, i, 1)* dp(num_string, i+1, e, 2)
        elif num == 1:
            dp_table[num][s][e] += dp(num_string, s, i, 0)* dp(num_string, i+1, e, 0)
            dp_table[num][s][e] += dp(num_string, s, i, 1)* dp(num_string, i+1, e, 1)
            dp_table[num][s][e] += dp(num_string, s, i, 0)* dp(num_string, i+1, e, 1)
        elif num == 2:
            dp_table[num][s][e] += dp(num_string, s, i, 1)* dp(num_string, i+1, e, 0)
            dp_table[num][s][e] += dp(num_string, s, i, 2)* dp(num_string, i+1, e, 1)
            dp_table[num][s][e] += dp(num_string, s, i, 2)* dp(num_string, i+1, e, 2)
    
    if dp_table[num][s][e] >= 0 :
        return dp_table[num][s][e]
    

# Iterate each test case in input.txt
for test_case in range(0, 20, 2):
    n = int(lines[test_case])    # n is the length of string
    s = lines[test_case+1].rstrip()  # s is string

    # Answer[0] is the number of a
    # Answer[1] is the number of b
    # Answer[2] is the number of c
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    dp_table = [[[ 0 for i in range(255)] for i in range(255)] for i in range(3)]
    num_string = st2num(s)
    
    num_a = dp(num_string, 0, n-1, 0)
    num_b = dp(num_string, 0, n-1, 1)
    num_c = dp(num_string, 0, n-1, 2)

    Answer = [num_a, num_b, num_c]
    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer[0]) + " " + str(Answer[1]) + " " + str(Answer[2]) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()