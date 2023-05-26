'''
Find the majority element, which appears more than half
the time, given a list of elements.
'''

import math

def find_majority_element(element_list: list) -> int:
    ''' Find the majority element in an element_list '''
    reccurring = []
    sum_nums = 0
    for element in element_list:
        i = 0
        found = False
        for rec_element in reccurring:
            if rec_element[0] == element:
                reccurring[i][1] += 1
                found = True
            i += 1
        if not found:
            reccurring.append([element, 1])
        sum_nums += 1
    list_len = len(element_list)
    for rec_element in reccurring:
        if rec_element[1] > math.floor(list_len / 2.0):
            return rec_element[0]
    return None

print(find_majority_element([1,2,1,1,3,4,0,2,2,2,2,2,2]))
