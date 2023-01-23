#!/usr/bin/env python3
'''
func that is Complex types - list of floats
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Type annotated func sum_list which takes a
    list input_list of floats as argument and returns
    their sum as a float.
    '''
    return sum(input_list)
