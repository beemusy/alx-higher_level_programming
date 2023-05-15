#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    result_list = []
    for i, val in enumerate(my_list):
        if i == idx:
            continue
        result_list.append(val)
    return(result_list)
