import time
import numpy as np
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
    s = s.rstrip("\n")
    
    #Answer = [0, 0, 0]
    # Answer[0] is the number of a
    # Answer[1] is the number of b
    # Answer[2] is the number of c
    
    """
    YOUR CODE HERE 
    Save your answer to the list variable Answer.
    """
    # num, n, string 인자로 받으면
    # num : index of abc
    # n : length of the string
    # string : abc string

    arr = np.zeros((3,n,n))
    abc = [[1, 1, 0], [2, 1, 0], [0, 2, 2]]
    abc_idx = {'a':0, 'b':1, 'c':2}

    for num in range(3):
        # 초기화
        # 자기 자신 & 이웃하는 것들
        for j in range(n):
            if num == abc_idx[s[j]]:
                arr[num, j, j] = 1
            if j == n-1:
                break
            elif num == abc[abc_idx[s[j]]][abc_idx[s[j+1]]]:
                arr[num, j, j+1] = 1

        # size
        for k in range(1,n):
            for l in range(n-k):
                r = l+k 
                for i in range(l, r):
                    # a
                    if num == 0:
                        arr[num, l, r] += arr[2, l, i]*arr[0, i+1, r]
                        arr[num, l, r] += arr[0, l, i]*arr[2, i+1, r]
                        arr[num, l, r] += arr[1, l, i]*arr[2, i+1, r]

                    # b
                    elif num == 1:  
                        arr[num, l, r] += arr[0, l, i]*arr[0, i+1, r]
                        arr[num, l, r] += arr[0, l, i]*arr[1, i+1, r]
                        arr[num, l, r] += arr[1, l, i]*arr[1, i+1, r]

                    # c
                    elif num == 2:
                        arr[num, l, r] += arr[1, l, i]*arr[0, i+1, r]
                        arr[num, l, r] += arr[2, l, i]*arr[1, i+1, r]
                        arr[num, l, r] += arr[2, l, i]*arr[2, i+1, r]


    Answer = [arr[0,0,n-1], arr[1,0,n-1], arr[2,0,n-1]]

    
    # Print the answer to output.txt
    output_f.write("#" + str(int(test_case/2 + 1)) + " " + str(Answer[0]) + " " + str(Answer[1]) + " " + str(Answer[2]) + "\n")
end = time.time()
output_f.write(f"{end - start:.5f} sec")
output_f.close()

